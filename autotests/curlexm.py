import requests

# URL с корректным UUID (или замените на нужный)
url = "http://127.0.0.1:8000/api/v1/files/d2ee880b-981d-424c-bb17-f9514589"

# Заголовки
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA2LTExVDA4OjIxOjI1LjIxNzAwOCIsInVzZXJfaWQiOiJkMmVlODgwYi05ODFkLTQyNGMtYmIxNy1mOTUxNGQ3YzQ1NTkifQ.AXEXk0rwL5QUM1CU3GnbJOGHzeP6SV_JS4NBulpGJYk"
}

# Отправляем GET-запрос
response = requests.get(url, headers=headers)

# Выводим результат
print("Status code:", response.status_code)
print("Response headers:", dict(response.headers))
print("Response text:", response.text)

# Если ответ в JSON, можно его распарсить
try:
    print("Response JSON:", response.json())
except:
    print("Response is not valid JSON")