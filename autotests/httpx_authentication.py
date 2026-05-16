import httpx

login_payload = {
  "email": "user@example.com",
  "password": "str"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response :",login_response_data)
print("Login status code:", login_response.status_code)

refresh_token_payload = {
    "refreshToken": login_response_data['token']['refreshToken']
}
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_token_payload)
refresh_response_data = refresh_response.json()
print("Refresh response :",refresh_response_data)
print("Refresh status code:", refresh_response.status_code)