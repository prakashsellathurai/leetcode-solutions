SUBMISSION_FOLDER = "../leetcode-submissions"

import os
from bs4 import BeautifulSoup
SUBMISSION_FOLDER_PATH =  os.path.join(os.getcwd(),SUBMISSION_FOLDER)
IGNORED_PATHS = ['.git','.github']

problems = []

def getLang(SUBMISSION_FOLDER_PATH,titleSlug):
    codefilename = os.path.join(SUBMISSION_FOLDER_PATH,titleSlug,titleSlug+'.py')
    if os.path.isfile(codefilename):
        return "Python",codefilename
    else:
        return "",None
cache = {}
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
    Readmefilecontents = Readmefilecontents.split('<hr>', 1)[-1]
    id =  int(str(tag_list[0].string ).split('.')[0])
    Slug = str(str(tag_list[0].string ).split('.')[1]) if str(str(tag_list[0].string ).split('.')[1]) != '' else titleSlug
    Slug = Slug.strip().replace(" ","-")

    if Slug not in cache:
        problems.append({'title':title,'titleSlug':Slug,'leetcodeurl':leetcodeurl,'lang':lang,'code':code,'content':Readmefilecontents,'id':id})
    cache[Slug] = True
problems.sort(key=lambda x:x['id'])

print("total Problems : ",len(cache))
print("ignored : ",len(os.listdir(SUBMISSION_FOLDER_PATH))-len(cache))

file='problems.json' 
import json
with open(file, 'w') as filetowrite:
    filetowrite.write(json.dumps( problems))