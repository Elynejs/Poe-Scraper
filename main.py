import json, requests, time

def fetch_id():
    with open('next_change_id.txt', 'r') as f:
        next_change_id = f.read()
        print(next_change_id)
        return next_change_id


def fetch_data(next_change_id):
    r = requests.get(f'http://api.pathofexile.com/public-stash-tabs/?id={next_change_id}')
    data = r.json()['next_change_id']
    print(r.json())
    with open(f'{next_change_id}.json', 'w', encoding='utf-8') as f:
        json.dump(r.json(), f, ensure_ascii=False, indent=4)
    with open('next_change_id.txt', 'w') as f:
        f.write(data)


next_change_id = fetch_id()
fetch_data(next_change_id)

