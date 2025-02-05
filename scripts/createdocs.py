#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    createDocs() utility to create docs from submissions
"""
__author__ = "prakashsellathurai"
__copyright__ = "Copyright 2022"
__version__ = "1.0.1"
__email__ = "prakashsellathurai@gmail.com"

import os
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
IGNORED_PATHS = [".git", ".github"]


def to_doc(problem):
    """converts problem to doc

    Args:
        problem (dict): problem data

    Returns:
        str: doc string
    """
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
        }
    )


def get_lang(folder_path, title_slug):
    """get lang from title_slug"""

    codefilename = os.path.join(folder_path, title_slug, title_slug + ".py")

    if os.path.isfile(codefilename):
        return "Python", codefilename
    else:
        return "", None


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

        readme_filename = os.path.join(
            SUBMISSION_FOLDER_PATH,
            title_slug,
            "README.md")
        try:
            with open(readme_filename, 'r') as file_buff:
                readme_file_contents = file_buff.read()
        except FileNotFoundError:
            print(f"Readme file Not found error {title_slug}")
            readme_file_contents = ""

        soup = BeautifulSoup(readme_file_contents, features="html.parser")
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

        if title_slug not in cache:
            problems.append(
                {
                    "title": title,
                    "title_slug": title_slug,
                    "leetcodeurl": leetcodeurl,
                    "lang": lang,
                    "code": code,
                    "content": readme_file_contents,
                    "id": prob_id,
                }
            )
        cache[title_slug] = True
    problems.sort(key=lambda x: x["id"])

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
    print("############ docs created ##################")


if __name__ == "__main__":
    main()
