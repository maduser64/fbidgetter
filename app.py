from flask import Flask, jsonify, render_template, request
import urllib2
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")


@app.route("/uuid", methods=['POST'])
def find_uuid():
	url = request.form['url']
	eid = find_uuid_from_url(url)
	data = {
	"url": url,
	"eid": eid
	}
	return jsonify(**data)


def find_uuid_from_url(url):
	response = urllib2.urlopen(url)
	html = response.read()
	eid_index = html.find("entity_id")
	if eid_index == -1:
		raise Exception
	eid_substr = html[eid_index + 12 : eid_index + 40]
	eid = eid_substr[:eid_substr.index('"')]
	return eid

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="3000")