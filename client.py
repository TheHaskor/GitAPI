import requests
import json
import http.server


# web_server for TC plugin https://plugins.jetbrains.com/plugin/9076-web-parameters
# this plugin allows us to get all git branches as a pretty list gui param

token = '<enter Git token>'
user = '<enter Git user>'

request_headers = {'Authorization': f'token {token}'}

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


def get_branches_names(response):
    return [item['name'] for item in response]


def create_scheme_dictionary(branches):
    # TC plugin requires a specific json structure. this function convert to it's structure
    post_dict = dict()
    all_options = []
    for branch in branches:
        temp_dict = {'key': branch, 'value': branch}
        all_options.append(temp_dict)
    post_dict['options'] = all_options
    return post_dict


def get_branches(repo):
    branches = []
    page = 0
    while True:
        try:
            response = requests.get(f'https://api.github.com/repos/{user}/{repo}/branches?per_page=100&page={page}',
                                    headers=request_headers).json()
            if not response:
                # no more branches
                break
        except Exception as e:
            print(str(e))
            break
        branches.extend(get_branches_names(response))
        page += 1
    return json.dumps(create_scheme_dictionary(branches))



