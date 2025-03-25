# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"  # Delete post with ID 1

# response = requests.delete(url)

# if response.status_code == 200:
#     print("Post Deleted Successfully!")
# else:
#     print("Failed to delete post. Status Code:", response.status_code)


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Get post with ID 1

response = requests.get(url)

if response.status_code == 200:
    print("Post Data:", response.json())  # Display the response data
else:
    print("Failed to fetch data. Status Code:", response.status_code)

# Output:
# Post Data: {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit repellat nihil\nmolestiae consequatur omnis quas\nest"
# }
