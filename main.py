import requests
from pprint import pprint


def get_token():
    # сервисный ключ приложения
    return '7ed4aba27ed4aba27ed4aba2bb7eb128fd77ed47ed4aba225b3ebce15d56c9a7c2db644'


# Класс - Пользователь ВК
class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.url = 'https://vk.com/id{}'.format(user_id)

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

    def __and__(self, other):
        result = list()
        for user_id in set(self.friends_get()).intersection(set(other.friends_get())):
            result.append(User(user_id))

        return result

    def request(self, method):
        return requests.get(
            'https://api.vk.com/method/{}'.format(method),
            {
                'access_token': get_token(),
                'v': 5.80,
                'user_id': self.user_id
            }
        )

    def friends_get(self):
        response = self.request('friends.get')

        return response.json()['response']['items']


def main():
    # main_user_id = input('Введите ID первого пользователя')
    first_user_id = 1594412

    first_user = User(first_user_id)

    # main_user_id = input('Введите ID второго пользователя')
    second_user_id = 608077

    second_user = User(second_user_id)

    # получаем список общих друзей
    print('Список общих друзей:')
    pprint(first_user & second_user)


main()
