import requests

# GET запрос
post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response = requests.get(url)

print("GET Response:")
print(response.json())

# проверка статуса
if response.status_code >= 400:
   print(f"Error: {response.status_code} - {response.text}")

# создание класса "ToDo"
class ToDo:
   def __init__(self, userId, id, title, completed):
      self.userId = userId
      self.id = id
      self.title = title
      self.completed = completed

# создание нового объекта класса ToDo
new_todo_object = ToDo(userId=1, id=1, title="example user", completed=True)

# POST запрос
ToDo_dict = {
   "userId": new_todo_object.userId,
   "title": new_todo_object.title,
   "completed": new_todo_object.completed
}

post_url = 'https://jsonplaceholder.typicode.com/todos'
post_response = requests.post(post_url, json=ToDo_dict)

print("\nPOST Response:")
print(post_response.json())

# проверка статуса
if post_response.status_code >= 400:
   print(f"Error: {post_response.status_code} - {post_response.text}")

# изменение данных
new_todo_object.completed = False
ToDo_dict["completed"] = new_todo_object.completed

# PUT запрос
put_url = f'https://jsonplaceholder.typicode.com/todos/{new_todo_object.id}'
put_response = requests.put(put_url, json=ToDo_dict)

print("\nPUT Response :")
print(put_response.json())

# Проверка статуса
if put_response.status_code >= 400:
   print(f"Error: {put_response.status_code} - {put_response.text}")