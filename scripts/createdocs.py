#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    createDocs() utility to create docs from submissions
"""
__author__ = "prakashsellathurai"
__copyright__ = "Copyright 2022"
__version__ = "1.0.1"
__email__ = "prakashsellathurai@gmail.com"

import datetime
import json
import os
import sys
import random
import re
import subprocess

from string import Template
from bs4 import BeautifulSoup


SUBMISSION_FOLDER = "./leetcode-submissions"
DOCS_FOLDER = "./docs"

PROBLEM_TEMPLATE_PATH = "./scripts/ProblemTemplate.txt"

SUBMISSION_FOLDER_PATH = os.path.join(os.getcwd(), SUBMISSION_FOLDER)
DOCS_PATH = os.path.join(os.getcwd(), DOCS_FOLDER)
PROBLEMS_FOLDER_PATH = os.path.join(os.getcwd(), "./source/problems/")
INDEX_FILE_PATH = os.path.join(os.getcwd(), "./source/_static/index.html")
IGNORED_PATHS = [".git", ".github",".deepsource.toml"]


def to_doc(problem):
    """converts problem to doc

    Args:
        problem (dict): problem data

    Returns:
        str: doc string
    """
    site_base = "https://prakashsellathurai.com/leetcode-solutions/problems"
    json_ld = {
        "@context": "https://schema.org",
        "@type": "QAPage",
        "mainEntity": {
            "@type": "Question",
            "name": problem["title"],
            "text": problem["description_text"],
            "url": problem["leetcodeurl"],
            "answerCount": 1,
            "datePublished": problem["datePublished"],
            "author": {
                "@type": "Organization",
                "name": "LeetCode",
                "url": "https://leetcode.com"
            },
            "acceptedAnswer": {
                "@type": "Answer",
                "text": problem["code"],
                "url": f"{site_base}/{problem['title_slug']}/",
                "datePublished": problem["datePublished"],
                "upvoteCount": 0,
                "author": {
                    "@type": "Person",
                    "name": "Prakash Sellathurai",
                    "url": "https://github.com/prakashsellathurai"
                }
            }
        }
    }

    file_buffer = open(PROBLEM_TEMPLATE_PATH, "r")
    template_string = file_buffer.read()
    file_buffer.close()
    template = Template(template_string)
    return template.substitute(
        {
            "title_slug": problem["title_slug"],
            "leetcodeurl": problem["leetcodeurl"],
            "content": problem["content"],
            "lang": problem["lang"],
            "code": problem["code"],
            "structured_data": json.dumps(json_ld, indent=2),
        }
    )


def get_lang(folder_path, title_slug):
    """get lang from title_slug"""

    folder_path = os.path.join(folder_path, title_slug)
    pyfiles = [file for file in os.listdir(folder_path) if file.endswith(".py")]
    codefilename =os.path.join(folder_path, pyfiles[0]) if pyfiles else ""
    if os.path.isfile(codefilename):
        return "Python", codefilename
    else:
        return "", None
    
def getReadme(folder_path, title_slug):
    lang, codeFilename = get_lang(folder_path, title_slug)
    if codeFilename is None:
        return None
    codeFilePath = os.path.dirname(codeFilename)
    readme_filename = os.path.join(codeFilePath, "README.md")
    return readme_filename

def get_git_date(submodule_path, file_path):
    try:
        relative_path = os.path.relpath(file_path, submodule_path)
        result = subprocess.run(
            ["git", "-C", submodule_path, "log", "--reverse", "--format=%cI",
             "--follow", "--", relative_path],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split('\n')[0]
    except Exception:
        pass
    return None


def main():
    """reads submissions and creates docs"""

    problems = []
    cache = {}
    slugs = os.listdir(SUBMISSION_FOLDER_PATH)
    total_items = len(slugs)
    for i,title_slug in enumerate(slugs):
        if title_slug in IGNORED_PATHS:
            continue

        lang, codefilename = get_lang(SUBMISSION_FOLDER_PATH, title_slug)

        if codefilename is None:
            # print(f"No code file found for {title_slug}")
            continue

        try:
            with open(codefilename, 'r') as file_buff:
                code = file_buff.read()
        except FileNotFoundError:
            # print("Code file Not found error " + str(title_slug))
            continue

        readme_filename = getReadme(SUBMISSION_FOLDER_PATH, title_slug)
        try:
            with open(readme_filename, 'r', encoding="utf-8") as file_buff:
                readme_file_contents = file_buff.read()
        except FileNotFoundError:
            # print(f"Readme file Not found error {title_slug}")
            readme_file_contents = ""

        soup = BeautifulSoup(readme_file_contents, "html.parser")
        tag_list = soup.findAll("h2")  # Specify the tag
        try:
            title = tag_list[0].string
        except IndexError:
            # print("error at " + str(title_slug))
            title = title_slug

        leetcodeurl = "https://leetcode.com/problems/" + title_slug
        readme_file_contents = readme_file_contents.split("<hr>", 1)[-1]
        try:
            prob_id = int(str(tag_list[0].string).split(".")[0])
        except IndexError:
            prob_id = [int(s) for s in re.findall(r"\d+", title_slug)][0]
        except ValueError:
            prob_id = generateOrPullProblemId(title_slug)

        if title_slug not in cache:
            description_text = BeautifulSoup(readme_file_contents, "html.parser").get_text()
            problems.append(
                {
                    "title": title,
                    "title_slug": title_slug,
                    "leetcodeurl": leetcodeurl,
                    "lang": lang,
                    "code": code,
                    "content": readme_file_contents,
                    "description_text": description_text,
                    "id": prob_id,
                    "codefilename": codefilename,
                }
            )
        cache[title_slug] = True
        update_progress(i + 1, total_items, message="Collecting problems")
        
    problems.sort(key=lambda x: x["id"])
    today = datetime.date.today().isoformat()
    for i, problem in enumerate(problems):
        git_date = get_git_date(SUBMISSION_FOLDER_PATH, problem["codefilename"])
        problem["datePublished"] = git_date if git_date else today
        update_progress(i + 1, len(problems), message="Fetching submission dates")

    print("total Problems : ", len(cache))
    print("ignored : ", len(os.listdir(SUBMISSION_FOLDER_PATH)) - len(cache))
    if not os.path.isdir(PROBLEMS_FOLDER_PATH):
        os.makedirs(PROBLEMS_FOLDER_PATH)

    for file_name in os.listdir(PROBLEMS_FOLDER_PATH):
        os.remove(os.path.join(PROBLEMS_FOLDER_PATH, file_name))


    for i,problem in enumerate(problems):
        filename = problem["title_slug"] + ".md"
        filepath = os.path.join(PROBLEMS_FOLDER_PATH, filename)
        try:
            f = open(filepath, "w")
            f.write(to_doc(problem))
            f.close()
        except FileNotFoundError:
            print("Error writing ", problem["title_slug"])
        except Exception as e:
            print("Error writing ", problem["title_slug"], e)
        update_progress(i + 1, len(problems), message="updating docs")


def generateOrPullProblemId(title_slug):
    try:
        prob_id = [int(s) for s in re.findall(r"\d+", title_slug)][0]
    except Exception as e:
        # print("error at " + str(title_slug), e)
        prob_id = random.randint(100000, 10000000)
    return prob_id


def update_progress(current, total, bar_length=20, message="Progress"):
    """Updates a text progress bar based on current step vs total steps."""
    fraction = current / total
    percent = fraction * 100
    filled = "█" * int(fraction * bar_length)
    empty = "-" * (bar_length - len(filled))

    # \r moves the cursor back to the start of the line to overwrite it
    sys.stdout.write(f"\r{message}: |{filled}{empty}| {percent:.1f}% Complete")
    sys.stdout.flush()

    # Print a new line only when completely finished
    if current >= total:
        print()

if __name__ == "__main__":
    main()
