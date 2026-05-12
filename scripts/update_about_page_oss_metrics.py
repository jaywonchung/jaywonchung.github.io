"""This script in-place updates about.html with the latest OSS metrics.

Assumptions:
- The path to the about page is "about.html"
- Each repo is ordered in the same order in the about page as in `REPOS`
- "fa-code-branch" appears exactly `len(REPOS)` times in the about page, and the entire line that contains "fa-code-branch" will be replaced by the filled in `HTML_TEMPLATE`
"""

import requests

REPOS = [
    "ml-energy/zeus",
    "cornserve-ai/cornserve",
    "gpu2grid/openg2g",
    "jaywonchung/BERT4Rec-VAE-Pytorch",
    "jaywonchung/reason",
    "jaywonchung/pegasus",
]

HTML_TEMPLATE = """                      <span class="resume-paper-venue mb-1" data-gh-repo="{repo}">(<i class="far fa-star"></i><span class="oss-stars">{stars}</span> <i class="fas fa-code-branch"></i><span class="oss-forks">{forks}</span>)</span>
"""


def get_github_repo_stars_and_forks(repo):
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["stargazers_count"], data["forks_count"]

def main():
    repo_metrics = [(repo, *get_github_repo_stars_and_forks(repo)) for repo in REPOS]

    with open("about.html", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if "fa-code-branch" in line:
            repo, stars, forks = repo_metrics.pop(0)
            lines[i] = HTML_TEMPLATE.format(repo=repo, stars=stars, forks=forks)

    with open("about.html", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
