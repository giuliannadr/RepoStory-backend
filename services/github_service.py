import requests

def get_user_info(username: str):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data.get("name"),
                "public_repos": data.get("public_repos"),
                "location": data.get("location")
            }
        else:
            return {"error": "User not found"} 