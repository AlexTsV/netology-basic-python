import requests
import time
from tqdm import tqdm
import json


class User:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def parametres(self):
        param = {
            'v': 5.92,
            'access_token': self.token,
            'user_id': self.user_id,
        }
        return param

    def get_user_groups(self):
        group_list = []
        response = requests.get('https://api.vk.com/method/groups.get', usr.parametres())
        for key, value in response.json().items():
            for k, v in value.items():
                if k == 'items':
                    group_list = v
        return set(group_list)

    def get_friends(self):
        friends_list = []
        response = requests.get('https://api.vk.com/method/friends.get', usr.parametres())
        for key, value in response.json().items():
            for k, v in value.items():
                if k == 'items':
                    friends_list = v
        return friends_list

    def friends_groups(self):
        print('Собираем группы всех друзей пользователя:')
        friends_list = self.get_friends()
        all_groups = []
        counter = 0
        for i in tqdm(friends_list):
            params = {
                'v': 5.92,
                'access_token': self.token,
                'user_id': i,
            }
            try:
                response = requests.get('https://api.vk.com/method/groups.get', params)
                for key, value in response.json().items():
                    if key == 'response':
                        for k, v in value.items():
                            if k == 'items':
                                for group_id in v:
                                    all_groups.append(group_id)
                    else:
                        counter += 1
                        raise Warning

            except Warning:
                while counter == 1:
                    time.sleep(1)
                    response = requests.get('https://api.vk.com/method/groups.get', params)
                    for key, value in response.json().items():
                        if key == 'response':
                            for k, v in value.items():
                                if k == 'items':
                                    for group_id in v:
                                        all_groups.append(group_id)
                            counter = 0
                        else:
                            for k, v in value.items():
                                if k == 'error_msg' and v != 'Too many requests per second':
                                    counter = 0
        return set(all_groups)

    def unique_user_groups_info(self):
        unique_groups = usr.get_user_groups().difference(usr.friends_groups())
        list_unique_groups = []
        for i in unique_groups:
            list_unique_groups.append(str(i))
        str_unique_groups = ','.join(list_unique_groups)
        params = {
            'v': 5.92,
            'access_token': self.token,
            'id': self.user_id,
            'group_ids': str_unique_groups,
            'fields': 'members_count',
        }
        time.sleep(1)
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        unique_user_groups = json.loads(response.text)
        for key, value in unique_user_groups.items():
            for v in value:
                v.pop('screen_name')
                v.pop('is_closed')
                v.pop('type')
                v.pop('photo_50')
                v.pop('photo_100')
                v.pop('photo_200')
                with open('groups.json', 'w', encoding='utf-8') as f:
                    json.dump(value, f, ensure_ascii=False)


usr = User('ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae', '171691064')
usr.unique_user_groups_info()
