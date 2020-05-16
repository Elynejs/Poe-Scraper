import json, requests, time

def fetch_id():
    with open('next_change_id.txt', 'r') as f:
        next_change_id = f.read()
        return next_change_id


def fetch_data(id):
    r = requests.get(f'http://api.pathofexile.com/public-stash-tabs/?id={id}')
    next_id = r.json()['next_change_id']
    with open(f'{id}.json', 'w', encoding='utf-8') as f:
        json.dump(r.json(), f)
    with open('next_change_id.txt', 'w') as f:
        f.write(next_id)
    return r.json()

def compute_data(raw):
    print('Number of fetched stashes : ' + len(raw['stashes']))

next_change_id = fetch_id()
raw = fetch_data(next_change_id)
compute_data(raw)

