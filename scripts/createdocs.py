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
import random
import re

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
STATE_FILE_PATH = os.path.join(os.getcwd(), "./scripts/problem_dates.json")


def load_dates():
    try:
        with open(STATE_FILE_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_dates(dates):
    with open(STATE_FILE_PATH, "w") as f:
        json.dump(dates, f, indent=2)


def to_doc(problem):
    """converts problem to doc

    Args:
        problem (dict): problem data

    Returns:
        str: doc string
    """
    site_base = "https://prakashsellathurai.com/leetcode-solutions/"
    json_ld = {
        "@context": "https://schema.org",
        "@type": "QAPage",
        "mainEntity": {
            "@type": "Question",
            "name": problem["title"],
            "text": problem["description_text"],
            "url": problem["leetcodeurl"],
            "answerCount": 1,
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

def main():
    """reads submissions and creates docs"""

    problems = []
    cache = {}
    for title_slug in os.listdir(SUBMISSION_FOLDER_PATH):
        if title_slug in IGNORED_PATHS:
            continue

        lang, codefilename = get_lang(SUBMISSION_FOLDER_PATH, title_slug)

        if codefilename is None:
            print(f"No code file found for {title_slug}")
            continue

        try:
            with open(codefilename, 'r') as file_buff:
                code = file_buff.read()
        except FileNotFoundError:
            print("Code file Not found error " + str(title_slug))
            continue

        readme_filename = getReadme(SUBMISSION_FOLDER_PATH, title_slug)
        try:
            with open(readme_filename, 'r', encoding="utf-8") as file_buff:
                readme_file_contents = file_buff.read()
        except FileNotFoundError:
            print(f"Readme file Not found error {title_slug}")
            readme_file_contents = ""

        soup = BeautifulSoup(readme_file_contents, "html.parser")
        tag_list = soup.findAll("h2")  # Specify the tag
        try:
            title = tag_list[0].string
        except IndexError:
            print("error at " + str(title_slug))
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
                }
            )
        cache[title_slug] = True
    problems.sort(key=lambda x: x["id"])

    dates = load_dates()
    today = datetime.date.today().isoformat()
    for problem in problems:
        slug = problem["title_slug"]
        if slug not in dates:
            dates[slug] = today
        problem["datePublished"] = dates[slug]
    save_dates(dates)

    print("############ problems collected ##################")

    print("total Problems : ", len(cache))
    print("ignored : ", len(os.listdir(SUBMISSION_FOLDER_PATH)) - len(cache))
    if not os.path.isdir(PROBLEMS_FOLDER_PATH):
        os.makedirs(PROBLEMS_FOLDER_PATH)

    for file_name in os.listdir(PROBLEMS_FOLDER_PATH):
        os.remove(os.path.join(PROBLEMS_FOLDER_PATH, file_name))

    print("############ old docs cleared ##################")
    for problem in problems:
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
    print("############ docs created ##################")

def generateOrPullProblemId(title_slug):
    try:
        prob_id = [int(s) for s in re.findall(r"\d+", title_slug)][0]
    except Exception as e:
        print("error at " + str(title_slug), e)
        prob_id = random.randint(100000, 10000000)
    return prob_id


if __name__ == "__main__":
    main()
