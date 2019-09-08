import requests
import mydata


query = mydata.query
headers = mydata.headers


def make_request(json):   # A simple function to use requests.post to make the API call.
    global headers
    response = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {json['query']}. "
                        f"{json['variables']}.")


def get_all_repos():
    global query
    json = {
        "query": query, "variables": {}
    }

    result = make_request(json)
    ans = result['data']['search']['nodes']
    end_cursor = result['data']['search']['pageInfo']['endCursor']
    query = query.replace("first:100", "first:100{AFTER}")

    for i in range(0, 10):
        if result['data']['search']['pageInfo']['hasNextPage']:
            new_query = query.replace("{AFTER}", f", after:\"{end_cursor}\"")
            json = {
                "query": new_query, "variables": {}
            }
            result = make_request(json)
            end_cursor = result['data']['search']['pageInfo']['endCursor']
            ans += result['data']['search']['nodes']

    return ans
