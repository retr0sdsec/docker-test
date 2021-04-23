import requests
import json
import req_test

res = []

for issue_id in req_test.keys:
    res.append(req_test.send_request(issue_id))

jsonResponse = []

for response in res:
    jsonResponse.append(json.loads(response.text))

lgt = []

for index in jsonResponse:
    lgt.append(len(jsonResponse))

nums = range(lgt[0] - 1)

types = []

for index in nums:
    if jsonResponse[index]['fields']['customfield_11803']['requestType']['name'] == "General question":
        types.append('https://jira.activeplatform.com/browse/' + jsonResponse[index]['key'])
