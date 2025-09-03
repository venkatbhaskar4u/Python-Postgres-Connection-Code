import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"  # Free test API

def basic_get():
    """Fetch list of posts (GET request)"""
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("GET Success! Number of posts:", len(response.json()))
    else:
        print("GET Failed:", response.status_code)

def basic_post():
    """Create a new post (POST request)"""
    data = {"title": "Demo Post", "body": "This is a test.", "userId": 1}
    response = requests.post(API_URL, json=data)
    print("POST result status:", response.status_code)
    print("POSTed data:", response.json())

def basic_put():
    """Update a post (PUT request)"""
    update_id = 1
    data = {"title": "Updated Title", "body": "Updated content.", "userId": 1}
    response = requests.put(f"{API_URL}/{update_id}", json=data)
    print("PUT result status:", response.status_code)
    print("Updated data:", response.json())

def basic_delete():
    """Delete a post (DELETE request)"""
    delete_id = 1
    response = requests.delete(f"{API_URL}/{delete_id}")
    print("DELETE result status:", response.status_code)
    print("Delete response:", response.text)

if __name__ == "__main__":
    basic_get()
    basic_post()
    basic_put()
    basic_delete()
