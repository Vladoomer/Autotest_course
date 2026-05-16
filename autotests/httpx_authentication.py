import httpx

login_payload = {
  "email": "user@example.com",
  "password": "str"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response :",login_response_data)
print("Login status code:", login_response.status_code)

access_token_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=access_token_headers)
get_me_response_data = get_me_response.json()
print(get_me_response_data)
print(get_me_response.status_code)