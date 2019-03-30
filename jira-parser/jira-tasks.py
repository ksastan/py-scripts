import json
import requests


def load_json(url):
    return (requests.get(url, auth=('jira-user', 'jira-password'), verify=False)).text


if __name__ == '__main__':
    url = 'https://jira-url/rest/api/latest/search?jql=project=TS+AND+assignee=null+AND+status!=Closed'
    data = json.loads(load_json(url))
    iss = []
    for i in range(len(data['issues'])):
            iss_string_prior = data['issues'][i]['fields']['priority']['name']
            iss_string_summ = data['issues'][i]['fields']['summary']
            if iss_string_prior == "Normal":
                iss_string_prior = '<font color="green">' + iss_string_prior + "</font>"
            if iss_string_prior == "Critical":
                iss_string_prior = '<font color="red">' + iss_string_prior + "</font>"
            if iss_string_prior == "Major":
                iss_string_prior = '<font color="red">' + iss_string_prior + "</font>"
            if iss_string_prior == "Blocker":
                iss_string_prior = '<font color="red">' + iss_string_prior + "</font>"
            iss_string = "<li><b>" + iss_string_prior + "</b>" + " " + iss_string_summ + "</li>"
            iss.append(iss_string)

    htmfile = open("issues.htm","w")
    style = '<link rel="stylesheet" href="/css/prtg1.css?prtgversion=18.2.40.1683+&language=en"> <link rel="stylesheet" type="text/css" href="/css/print.css?version=18.2.40.1683+" media="print"  /> <style type="text/css"> .hidefornoneadmins{display:none!important;} .hideforreadonly { display:none!important; } </style>\
	<div class="top10listcontainer" style="background:#a5a5a5;overflow:hidden;font-size:23px";>\
        <p>&nbsp&nbsp&nbsp<span id="datetime"></span></p>\
        <script> var dt = new Date(); document.getElementById("datetime").innerHTML = dt.toLocaleTimeString(); </script>'
    htmfile.write(style)
    for item in iss:
        htmfile.write(item)
    htmfile.close()
