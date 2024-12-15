import requests

url = 'https://api.github.com/repos/argoproj/argo-cd/pulls'

response = requests.get(url)

if response.status_code == 200:

    pull_requests = response.json()

    pr_creators = {}

    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print(f"PR Creator counts: {pr_creators}")

    for creator, count in pr_creators.items():
        print(f"Creators: {creator}: {count} PRs")

else:
     print(f"Failed to make connection. Status Code: {response.status_code}")
