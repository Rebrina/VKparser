import requests
import time
import json
from tqdm import tqdm

token = "ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae"

def user_groups(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_id': user_id
    }
    url = "https://api.vk.com/method/groups.get"
    response = requests.get(url, params=params, timeout=30).json()
    user_groups_list = response["response"]["items"]
    time.sleep(0.5) 
    return user_groups_list

def user_friends(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
    }
    url = 'https://api.vk.com/method/friends.get'
    response = requests.get(url, params=params, timeout=30).json()    
    friends_list_id = response['response']['items']
    return friends_list_id

def group_info(group_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'group_ids': group_id,
        'fields': 'members_count'
    }
    url = 'https://api.vk.com/method/groups.getById'
    response = requests.get(url, params=params, timeout=30).json()
    group_info_list = response['response']
    return group_info_list

def get_result(user_groups_list):
    result_all = []
    for group in user_groups_list:
        i = 0        
        group_info_1 = group_info(group)
        group_info_formated = {'name': group_info_1[i]['name'], 'gid': group_info_1[i]['id'],
                           'members_count': group_info_1[i]['members_count']}
        result_all.append(group_info_formated)
        i += 1        
    return result_all

def get_file(user):
    user_groups_list = user_groups(user)

    friends_list_id = user_friends(user)

    for friend in tqdm(friends_list_id):
        try:
            friend_group_list = user_groups(friend)
        except KeyError:
            friend_group_set = {}
        user_groups_list = list(set(user_groups_list) - set(friend_group_list))

    result = get_result(user_groups_list)

    with open('groups.json', 'w') as f:
        json.dump(result, f)


if __name__ == "__main__":
    user = int(input("Введите ID пользователя: "))

    get_file(user)
