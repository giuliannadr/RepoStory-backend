from groq import Groq
from core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_repo_story(stats, commits):
    prompt = f"""
You are a professional software project analyzer for technical recruiters.
Given real data from a GitHub repository, generate an honest and professional description of what problem this project solved and how.

Repository Stats:
{stats}

Recent Commits:
{commits}

Analysis requirements:
- Describe what the project is and what it does
- Identify the real technical problem it solves (only from evidence in the data, never invent)
- Detect the stack from commit messages and stats
- Calculate and include these metrics:
  * Project duration in weeks (from first to last commit)
  * Commit frequency (commits per week)
  * Percentage of commits per author
  * Most common commit types (feat, fix, refactor, chore, etc.)
  * Whether commit messages follow Conventional Commits standard (yes/no)
  * Collaboration level (solo project or team, how many contributors)

Respond strictly in this format:
- **What is it?**: One sentence
- **What problem does it solve?**: One sentence with real evidence from the data
- **Stack**: Detected technologies list
- **Metrics**:
  * Duration: X weeks
  * Commit frequency: X commits/week
  * Authors: name (X% of commits), name (X% of commits)
  * Commit types: feat (X%), fix (X%), other (X%)
  * Conventional Commits: yes/no
- **For the recruiter**: Two sentences max highlighting real technical value

Important: Never invent information not present in the data. If something cannot be determined, say "Not enough data".
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content