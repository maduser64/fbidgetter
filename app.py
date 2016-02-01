from flask import Flask, jsonify, render_template, request
import urllib2, requests, json
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")


@app.route("/uuid", methods=['POST'])
def find_uuid():
	url = request.form['url']
	eid = find_uuid_from_url(url)
	name = get_name_from_id(eid)
	data = {
	"url": url,
	"eid": eid,
	"name": name
	}
	return jsonify(**data)


def find_uuid_from_url(url):
	response = urllib2.urlopen(url)
	html = response.read()
	eid_index = html.find("entity_id")
	if eid_index == -1:
		eid = "N/A"
	else:
		eid_substr = html[eid_index + 12 : eid_index + 40]
		eid = eid_substr[:eid_substr.index('"')]
	return eid


def get_name_from_id(uuid):
	app_id = "269885496365658"
	app_secret = "d6fb43b77ac2e35a7237729ed22b3d6f"
	url = "https://graph.facebook.com/v2.5/" + uuid + "?access_token=" + app_id + "|" + app_secret
	user = requests.get(url).content
	user = json.loads(user)
	return user["name"]

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="3000")
