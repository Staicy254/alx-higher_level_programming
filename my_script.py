import urllib.request

print("Script is running...")
username = 'your_username'  # Replace 'your_username' with the actual GitHub username
token = 'your_token'        

url = f'https://api.github.com/users/{username}'
header = {'Authorization': f'Bearer {token}'}

# Construct the request
req = urllib.request.Request(url, headers=header)

# Send the request and retrieve the response
with urllib.request.urlopen(req) as response:
    r = response.read()
    head = response.headers

# Print the response body and headers
print("Response body:")
print(r)
print("\nResponse headers:")
print(head)
