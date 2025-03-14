import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Delete post with ID 1

response = requests.delete(url)

if response.status_code == 200:
    print("Post Deleted Successfully!")
else:
    print("Failed to delete post. Status Code:", response.status_code)