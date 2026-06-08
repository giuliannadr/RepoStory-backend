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
        
def get_user_repos(username: str):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [
                {
                    "name": repo.get("name"),
                    "description": repo.get("description"),
                    "language": repo.get("language"),
                    "stargazers_count": repo.get("stargazers_count"),
                    "html_url": repo.get("html_url"),
                    "updated_at": repo.get("updated_at")
                }
                for repo in data
            ]
        else:
            return {"error": "Repos not found"}