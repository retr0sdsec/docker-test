import requests
import json
import pprint
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

worklogs = []

for index in nums:
    if jsonResponse[index]['fields']['worklog']['total'] == 0:
        worklogs.append('https://jira.activeplatform.com/browse/' + jsonResponse[index]['key'])


