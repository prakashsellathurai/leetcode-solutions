SUBMISSION_FOLDER = "./leetcode-submissions"

import os
from bs4 import BeautifulSoup
SUBMISSION_FOLDER_PATH =  os.path.join(os.getcwd(),SUBMISSION_FOLDER)
IGNORED_PATHS = ['.git']

problems = []

def getLang(SUBMISSION_FOLDER_PATH,titleSlug):
    codefilename = os.path.join(SUBMISSION_FOLDER_PATH,titleSlug,titleSlug+'.py')
    if os.path.isfile(codefilename):
        return "Python",codefilename
    else:
        return "",None

for titleSlug in os.listdir(SUBMISSION_FOLDER_PATH):
    if titleSlug in IGNORED_PATHS:
        continue
    
    lang,codefilename = getLang(SUBMISSION_FOLDER_PATH,titleSlug)
    with open(codefilename) as f:
        code = f.read()
    Readmefilename =  os.path.join(SUBMISSION_FOLDER_PATH,titleSlug,'README.md')
    with open(Readmefilename) as f:
        Readmefilecontents = f.read()

    soup = BeautifulSoup(Readmefilecontents)
    tag_list = soup.findAll('h2') # Specify the tag
    title = tag_list[0].string
    leetcodeurl = "https://leetcode.com/problems/"+titleSlug
    problems.append({'title':title,'titleSlug':titleSlug,'leetcodeurl':leetcodeurl,'lang':lang,'code':code,'content':Readmefilecontents})


file='./website/problems.json' 
import json
with open(file, 'w') as filetowrite:
    filetowrite.write(json.dumps( problems))