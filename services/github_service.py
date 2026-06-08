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
        
def get_repo_commits(username: str, repo_name: str):
        url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [
                {
                    "sha": commit.get("sha"),
                    "author": commit.get("commit", {}).get("author", {}).get("name"),
                    "message": commit.get("commit", {}).get("message"),
                    "date": commit.get("commit", {}).get("author", {}).get("date")
                }
                for commit in data
            ]
        else:
            return {"error": "Commits not found"}
        
def get_repo_stats(username: str, repo_name: str):
        url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.get(url)
        commits = get_repo_commits(username, repo_name)
        if response.status_code == 200:
            data = response.json()
            return {
                "total commits": len(commits),
                "different authors": len(set(commit.get("author") for commit in commits)),
                "first and last commit": {
                    "first": commits[-1] if commits else None,
                    "last": commits[0] if commits else None
                },
                "recent commit message": commits[0].get("message") if commits else None,
                
            }
        else:
            return {"error": "Repo not found"}
