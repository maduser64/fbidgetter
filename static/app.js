function findUUID(){
	var input = $("#profile_links").val();
  var profile_links = input.split(',');
  profile_links = profile_links.map(jQuery.trim);
  users = profile_links.map(getUser);
  console.log(users);
}

function getUser(profile_link){
  var userId = getUserIdFromUrl(profile_link);
  var data = $.post("/uuid", {url: profile_link}, function(response, status){
    $("#uuid").append("<div class='user'><p>UUID: " + response["eid"] + "</p><p>Profile URL: " + response.url + "</div")
    $("#csvuuid").append(response["eid"] + ",")
    return response;
  });
  return data;
}

function getUserIdFromUrl(urlStr){
  var userId;
  urlVars = getUrlVars(urlStr);
  if (urlVars["id"]) {
    userId = urlVars["id"];
  } else{
    userId = getUrlEnd(urlStr);
  }
  return userId;
}

function getUrlEnd(urlStr){
  return urlStr.split("/").pop();
}

function getUrlVars(urlStr){
  var vars = [], hash;
  var hashes = urlStr.slice(urlStr.indexOf('?') + 1).split('&');
  for(var i = 0; i < hashes.length; i++)
  {
      hash = hashes[i].split('=');
      vars.push(hash[0]);
      vars[hash[0]] = hash[1];
  }
  return vars;
}