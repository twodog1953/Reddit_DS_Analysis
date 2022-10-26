import requests


# login credentials
def start(pus, token, username, pw):
    auth = requests.auth.HTTPBasicAuth(pus, token)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': pw
    }

    # requests and api
    headers = {'User-Agent': 'nm$l/1.0'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    # while the token is valid (~2 hours) we just add headers=headers to our requests
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

    return headers
