import os
from bs4 import BeautifulSoup
from string import Template

SUBMISSION_FOLDER = "./leetcode-submissions"
DOCS_FOLDER = "./docs"

SUBMISSION_FOLDER_PATH = os.path.join(os.getcwd(), SUBMISSION_FOLDER)
DOCS_PATH = os.path.join(os.getcwd(), DOCS_FOLDER)
PROBLEMS_FOLDER_PATH = os.path.join(os.getcwd(), "./source/problems/")
INDEX_FILE_PATH = os.path.join(os.getcwd(), "./source/_static/index.html")
IGNORED_PATHS = [".git", ".github"]


def toDoc(problem):
    f = open('./scripts/ProblemTemplate.txt')
    templateString = f.read()
    f.close()
    t = Template(templateString)
    return t.substitute(
        {
            "titleSlug": problem["titleSlug"],
            "leetcodeurl": problem["leetcodeurl"],
            "content": problem["content"],
            "lang": problem["lang"],
            "code": problem["code"],
        }
    )


def getLang(SUBMISSION_FOLDER_PATH, titleSlug):
    codefilename = os.path.join(SUBMISSION_FOLDER_PATH, titleSlug, titleSlug + ".py")
    if os.path.isfile(codefilename):
        return "Python", codefilename
    else:
        return "", None


def main():

    problems = []
    cache = {}
    for titleSlug in os.listdir(SUBMISSION_FOLDER_PATH):
        if titleSlug in IGNORED_PATHS:
            continue

        lang, codefilename = getLang(SUBMISSION_FOLDER_PATH, titleSlug)

        with open(codefilename) as f:
            code = f.read()
        Readmefilename = os.path.join(SUBMISSION_FOLDER_PATH, titleSlug, "README.md")
        with open(Readmefilename) as f:
            Readmefilecontents = f.read()

        soup = BeautifulSoup(Readmefilecontents)
        tag_list = soup.findAll("h2")  # Specify the tag
        title = tag_list[0].string
        leetcodeurl = "https://leetcode.com/problems/" + titleSlug
        Readmefilecontents = Readmefilecontents.split("<hr>", 1)[-1]
        id = int(str(tag_list[0].string).split(".")[0])
        Slug = (
            str(str(tag_list[0].string).split(".")[1])
            if str(str(tag_list[0].string).split(".")[1]) != ""
            else titleSlug
        )
        Slug = Slug.strip().replace(" ", "-")

        if Slug not in cache:
            problems.append(
                {
                    "title": title,
                    "titleSlug": Slug,
                    "leetcodeurl": leetcodeurl,
                    "lang": lang,
                    "code": code,
                    "content": Readmefilecontents,
                    "id": id,
                }
            )
        cache[Slug] = True
    problems.sort(key=lambda x: x["id"])

    print("############ problems collected ##################")

    print("total Problems : ", len(cache))
    print("ignored : ", len(os.listdir(SUBMISSION_FOLDER_PATH)) - len(cache))
    if not os.path.isdir(PROBLEMS_FOLDER_PATH):
        os.makedirs(PROBLEMS_FOLDER_PATH)

    for f in os.listdir(PROBLEMS_FOLDER_PATH):
        os.remove(os.path.join(PROBLEMS_FOLDER_PATH, f))

    print("############ old docs cleared ##################")
    for problem in problems:
        filename = problem["titleSlug"] + ".md"
        filepath = os.path.join(PROBLEMS_FOLDER_PATH, filename)
        try:
            f = open(filepath, "w")
            f.write(toDoc(problem))
            f.close()
        except:
            print("Error writing ", problem["titleSlug"])
    print("############ docs created ##################")
    # indexDoc = problems[0]['titleSlug']
    # IndexTemp = Template(open('./scripts/IndexTemplate.txt','r').read())
    # f = open(INDEX_FILE_PATH,'w')
    # f.write(IndexTemp.substitute({'indexDoc':indexDoc}))
    # f.close()
    print("############ Index redirect added ##################")


if __name__ == "__main__":
    main()
