#Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей
import requests
import time

token = "ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae"

#функция для определенения, в каких группах состоит юзер
def user_groups(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_id': user_id
        }
    url = "https://api.vk.com/method/groups.get"
    response = requests.get(url, params=params, timeout=30).json()
    user_groups_list = response['response']['items']
    time.sleep(1)
    return(user_groups_list)

#функция для определения id его друзей
def user_friends(user_id):
    params = {
        'access_token': token,
        'v': 5.92,
        'user_ids': user_id
        }
    url = 'https://api.vk.com/method/friends.get'
    response = requests.get(url, params=params, timeout=30).json()
    friends_list_id = response['response']['items']
    return(friends_list_id)


#user = input("Введите id пользователя ")
#но пока лень, поэтому
user = 171691064
#в каких группах состоит юзер?
user_groups_list = user_groups(user)
print(user_groups_list)

#сколько у него друзей
friends_list_id = user_friends(user)

#берем id каждого друга юзера
for friend in friends_list_id:
    try:
      #получаем группы, в которых он состоит
        friend_group_list = user_groups(friend)
        #print(friend)
        #print(friend_group_set)
    except KeyError:
        friend_group_set = {}
    #берем группы исходного пользователя, находим пересечения и удаляем их
    result=list(set(user_groups_list) - set(friend_group_list))
    print(result)
    user_groups_list = result

print(user_groups_list)

#Вывести финальный списко групп в json
#для каждой группы получить шапку
#записать в файл

#groups.json