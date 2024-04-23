"""This script in-place updates about.html with the latest OSS metrics.

Assumptions:
- The path to the about page is "about.html"
- Each repo is ordered in the same order in the about page as in `REPOS`
- "fa-code-branch" appear exactly `len(REPOS)` times in the about page, and the entire line that contains "fa-code-branch" will be replaced by the filled in `HTML_TEMPLATE`
- "Number of stars and forks are as of" appears exactly once in the about page, and the entire line that contains "Number of stars and forks are as of" will be replaced by the filled in `LAST_UPDATED_TEMPLATE`
"""

import requests
from datetime import datetime

REPOS = [
    "jaywonchung/bert4rec-vae-pytorch",
    "jaywonchung/reason",
    "ml-energy/zeus",
    "jaywonchung/pegasus",
]

HTML_TEMPLATE = """                      <span class="resume-paper-venue mb-1">(<i class="far fa-star"></i>{stars} <i class="fas fa-code-branch"></i>{forks})</span>
"""
LAST_UPDATED_TEMPLATE = """                  <div class="mb-3"><i>Number of stars and forks are as of {date}.</i></div>
"""


def today() -> str:
    """Returns today's date in a format like Febraury 13th, 2024."""
    date = datetime.now()

    month = date.strftime("%B")
    
    day = date.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    
    year = date.strftime(", %Y")
    
    return f"{month} {day}{suffix}{year}"

def get_github_repo_stars_and_forks(repo):
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["stargazers_count"], data["forks_count"]

def main():
    stars_and_forks = [get_github_repo_stars_and_forks(repo) for repo in REPOS]

    with open("about.html", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "fa-code-branch" in line:
            stars, forks = stars_and_forks.pop(0)
            lines[i] = HTML_TEMPLATE.format(stars=stars, forks=forks)
        elif "Number of stars and forks are as of" in line:
            lines[i] = LAST_UPDATED_TEMPLATE.format(date=today())

    with open("about.html", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
