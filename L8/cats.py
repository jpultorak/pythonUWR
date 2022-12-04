import requests
import prywatne

# for ids corresponding to breeds see function avaliable_breeds() below   
# to use without api key, remove headers
def get_cat_images(breeds = None):
    # use API key to authenticate (allows for more functionality)
    headers = {'x-api-key' : prywatne.api_key}
    if breeds is not None:
        breeds = ','.join(breeds)
 
    # for some reason limit is always either 1 or 10, no in betweens
    # seems to be bug on APIs' side
    query_params = {"limit":10, 'breed_ids' : breeds}

    r = requests.get("https://api.thecatapi.com/v1/images/search", params=query_params, headers=headers) 
    data = r.json()
    for id,d in enumerate(data):
        print(f"{id}: {d['url']}")

# prints breed names and corresponding ids
# no Api required
def avaliable_breeds():
    all_breeds = requests.get("https://api.thecatapi.com/v1/breeds")
    breeds = all_breeds.json()

    res = [{x : breed[x] for x in ['name', 'id']} for breed in breeds]
    for id, info in enumerate(res):
        print(f"{id}: {info['name']}  {info['id']}")

if __name__ == '__main__':
    # avaliable_breeds()
    get_cat_images(['sibe', 'crex'])
