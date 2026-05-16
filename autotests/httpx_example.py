import httpx
#
# response = httpx.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(response.status_code)
# print(response.json())
#
#
# data  = {
#     "title" : "Новая задача",
#     "completed": False,
#     "userId": 10
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.headers)
# print(response.status_code)
# print(response.json())

# data = {
#     "username" : "vlad",
#     "password" : "12345"
# }
#
# response = httpx.post('https://httpbin.org/post', data=data)
# print(response.headers)
# print(response.status_code)
# print(response.json())
#
# headers = {
#     "Authorization": "Bearer 12345"
# }
#
# response = httpx.get('https://httpbin.org/get', headers=headers)
#
# print('*' * 50)
# print(response.request.headers)
# print(response.json())

# data = {
#     "userId" : 1
# }
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=data)
# print("*"*50)
# print(response.url)
# print(response.json())

# files = {
#     "file" : ("filte1.txt", open("filte1.txt", "rb"))
# }
#
# response = httpx.post('https://httpbin.org/post', files=files)
# print(response.json())
#
# with httpx.Client() as client:
#     response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(response1.json())
# print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer Mozilla/5.0"})
response = client.get('https://httpbin.org/get')

print(response.json())
try:
    response = httpx.get('https://httpbin.org/invalid-get')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")