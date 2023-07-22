import requests
import json


def upload(token: str, file_name: str, data: str, repo: str, owner: str):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        "message": f"push file: {file_name}",
        "content": data,
    }

    data = json.dumps(data)

    response = requests.put(f'https://api.github.com/repos/{owner}/{repo}/contents/{file_name}', headers=headers, data=data)
    if response.status_code != 201:
        return response
    return response

def getContents(token: str, repo: str, owner: str) -> list:
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/contents/', headers=headers)
    if response.status_code == 200:
        _ = []
        if response.content:
            data = json.loads(response.content)
            for i in data:
                _.append(i['name'])
            return json.dumps(_)
        return _
    raise Exception(f"there where an error to github: {response.status_code}")
