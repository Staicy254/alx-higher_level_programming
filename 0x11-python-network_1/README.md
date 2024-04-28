# Fetching Internet Resources with Python

## urllib

- Use `urllib.request.urlopen()` to fetch internet resources.
- Decode the body response using `.read()` and appropriate encoding (e.g., `.decode('utf-8')`).

## requests

- **Requests is Way Simpler Than Urllib**
- Import `requests` package to simplify HTTP requests.

### Making HTTP Requests

- **GET Request:**
  ```python
  import requests
  response = requests.get('http://example.com')
POST/PUT/etc. Requests:
python
Copy code
import requests
payload = {'key': 'value'}
response = requests.post('http://example.com', data=payload)
Fetching JSON Resources
Use .json() method to fetch JSON resources directly:
python
Copy code
import requests
response = requests.get('http://example.com/api/data')
json_data = response.json()
Manipulating Data from an External Service
Once data is fetched, manipulate it using Python's data manipulation tools (e.g., dictionaries, lists, etc.).
Additional Notes
Always handle errors and exceptions when making HTTP requests.
Check the documentation of the specific package (urllib or requests) for more advanced features and options.
