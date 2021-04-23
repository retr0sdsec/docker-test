import requests
import json
import pprint

#url = 'https://jira.activeplatform.com/rest/api/2/search?jql=project%20%3D%20SAP%20AND%20assignee%20in%20("sergey.malakhov%40activeplatform.com")%20AND%20updatedDate%20>%3D%20startOfDay()%20AND%20updatedDate%20<%3D%20endOfDay()%20order%20by%20lastViewed%20DESC'

url = 'https://jira.activeplatform.com/rest/api/2/search?jql=project%20%3D%20SAP%20AND%20assignee%20in%20("sergey.malakhov%40activeplatform.com")%20AND%20updatedDate%20>%3D%20startOfMonth()%20AND%20updatedDate%20<%3D%20endOfMonth()%20order%20by%20lastViewed%20DESC'

headers = {
            'Authorization': 'Basic c2VyZ2V5Lm1hbGFraG92QGFjdGl2ZXBsYXRmb3JtLmNvbTpCR25hbG9vQSY1c0Z0WDhS',
                'Content-Type': 'application/json',
                }

response = requests.get(url=url, headers=headers)

jsonResponse = json.loads(response.text)

lgt = len(jsonResponse['issues'])                                                                                                                                      

nums = range(lgt - 1)

keys = []

for num in nums:
    keys.append(jsonResponse['issues'][num]['key'])

def send_request(issue_id):
    url = 'https://jira.activeplatform.com/rest/api/2/issue/' + issue_id

    headers = {
            'Authorization': 'Basic c2VyZ2V5Lm1hbGFraG92QGFjdGl2ZXBsYXRmb3JtLmNvbTpCR25hbG9vQSY1c0Z0WDhS',
                'Content-Type': 'application/json',
                }

    response = requests.get(url=url, headers=headers)

    return response

#for num in nums:
#    pprint.pprint(jsonResponse['issues'][num]['key'])
#types = jsonResponse['fields']['customfield_11803']['requestType']['name']

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#print(jsonResponse)
