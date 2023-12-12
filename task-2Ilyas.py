# # #task 2.1, 2.2
# import requests
# import random
#
# # рандомный айди 1 - 826
# random_id = random.randint(1, 826)
#
# # GET запрос
# url = f'https://rickandmortyapi.com/api/character/{random_id}'
# response = requests.get(url)
# data = response.json()
# print(data)
# print(data.keys())

# #task 2.3
# import requests
# import random
# import json

# # рандомный айди 1 - 826
# random_id = random.randint(1, 826)

# #  GET запрос
# url = f'https://rickandmortyapi.com/api/character/{random_id}'
# response = requests.get(url)
# data = response.json()

# print(data)
# print(data.keys())

# # сохранение ответа json в файл
# filename = f'info_character_{random_id}.json'
# with open(filename, 'w') as file:
#    json.dump(data, file)

# print(f'\nJSON response saved: {filename}')

# #task 2.4
# import requests
# import random

# # рандомный айди 1 - 826
# random_id = random.randint(1, 826)

# # GET запрос
# url = f'https://rickandmortyapi.com/api/character/{random_id}'
# response = requests.get(url)
# data = response.json()

# # извлечение урла эпизодов
# episode_urls = data.get("episode", [])

# episode_ids = [url.split("/")[-1] for url in episode_urls]

# # создание файла "all_episodes_with_character_{character_id}" и добавление урла
# filename = f'all_episodes_with_character_{random_id}.txt'
# with open(filename, 'a') as file:
#    for episode_url in episode_urls:
#       file.write(f"{episode_url}\n")

# print(f'Episode URLs appended to file: {filename}')

# #task 2.5
# import requests

# url = "https://rickandmortyapi.com/api/episode/1"
# response = requests.get(url)
# data = response.json()
# for key, value in data.items():
#    print(f"{key}: {type(value).__name__}")

# #task 2.6
# class Episode:
#    def __init__(self, episode_id, name, air_date, episode, characters, url, created):
#       self.episode_id = episode_id
#       self.name = name
#       self.air_date = air_date
#       self.episode = episode
#       self.characters = characters
#       self.url = url
#       self.created = created

# import requests

# # GET запрос для 1 эпизода
# url = 'https://rickandmortyapi.com/api/episode/1'
# response = requests.get(url)
# data = response.json()

# #создание объекта
# ep_object = Episode(
#    data['id'],
#    data['name'],
#    data['air_date'],
#    data['episode'],
#    data['characters'],
#    data['url'],
#    data['created']
# )

# print(f"id: {ep_object.episode_id}")
# print(f"Name: {ep_object.name}")
# print(f"Date: {ep_object.air_date}")
# print(f"Code: {ep_object.episode}")

# #task 2.7
# class Episode:
#    def __init__(self, episode_id, name, air_date, episode, characters, url, created):
#       self.episode_id = episode_id
#       self.name = name
#       self.air_date = air_date
#       self.episode = episode
#       self.characters = characters
#       self.url = url
#       self.created = created

# import requests

# ep_ids = [1, 2, 3, 4, 5, 6, 7]

# def get_ep_data(id):
#    url = f"https://rickandmortyapi.com/api/episode/{id}"
#    response = requests.get(url)

#    if response.status_code == 200:
#       return response.json()
#    else:
#       print("error")
#       return None

# episodes_list = []

# for id in ep_ids:
#    data = get_ep_data(id)

#    if data:
#       episode = Episode(
#          data['id'],
#          data['name'],
#          data['air_date'],
#          data['episode'],
#          data['characters'],
#          data['url'],
#          data['created']
#       )
#       episodes_list.append(episode)
#       print(f"Episode {episode.episode_id}: {episode.name} - Date: {episode.air_date}")

# #task 2.8
# class Episode:
#    def __init__(self, episode_id, name, air_date, episode, characters, url, created):
#       self.episode_id = episode_id
#       self.name = name
#       self.air_date = air_date
#       self.episode = episode
#       self.characters = characters
#       self.url = url
#       self.created = created

#    def info(self):
#       print(f"Episode {self.episode_id}: {self.name} - Date: {self.air_date}")
#       print(f"Episode number: {self.episode}")
#       print(f"Episode URL: {self.url}")
#       print("------")

# import requests

# ep_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_episode_data(id):
#    url = f"https://rickandmortyapi.com/api/episode/{id}"
#    response = requests.get(url)

#    if response.status_code == 200:
#       return response.json()
#    else:
#       print("error")
#       return None

# episodes_list = []

# for id in ep_ids:
#    episode_data = get_episode_data(id)

#    if episode_data:
#       episode = Episode(
#             episode_data['id'],
#             episode_data['name'],
#             episode_data['air_date'],
#             episode_data['episode'],
#             episode_data['characters'],
#             episode_data['url'],
#             episode_data['created']
#       )
#       episodes_list.append(episode)

# for episode in episodes_list:
#    episode.info()

# #task 2.9
# import requests

# url = 'https://rickandmortyapi.com/api/character/1'
# response = requests.get(url)

# if response.status_code == 200:
#    data = response.json()
#    print(data)
# else:
#    print(f"Error: {response.status_code} - {response.text}")

# #task 2.10, 2.11, 2.12, .13
# import requests
# class Character:
#    def __init__(self, name="", status="", gender="", episode="", url=""):
#       self.name = name
#       self.status = status
#       self.gender = gender
#       self.episode = episode
#       self.url = url

#    def info_from_api(self, character_id):
#       url = f'https://rickandmortyapi.com/api/character/{character_id}'
#       response = requests.get(url)

#       character_data = response.json()

#       self.name = character_data.get('name', "")
#       self.status = character_data.get('status', "")
#       self.gender = character_data.get('gender', "")
#       self.episode = character_data.get('episode', "")
#       self.url = character_data.get('url', "")

#    def info(self):
#       print(f"Name: {self.name}")
#       print(f"Status: {self.status}")
#       print(f"Gender: {self.gender}")
#       print(f"Episode: {self.episode}")
#       print(f"URL: {self.url}")

# random_character = Character()
# random_character.info_from_api(1)
# random_character.info()
# result = random_character.info
# print(result)