import re
import json
#text = "Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com"

text = open('websiteData.txt', 'r', encoding="utf8")

emails = re.findall("[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text.read())
result = {}
for email in emails:
    if email in result.keys():
        result[email]['Occurence']+=1
        t = re.search("^[a-zA-Z]+\.[a-zA-Z]+@+",email)
        
        if t is not None:
            result[email]['EmailType']='Human'
        else:
            result[email]['EmailType']='Non-Human'

    value={}
    value['Occurence']=1
    t = re.search("^[a-zA-Z]+\.[a-zA-Z]+@+",email)
    
    if t is not None:
        value['EmailType']='Human'
    else:
        value['EmailType']='Non-Human'


    result[email] = value;
    

print (result)
with open("result.json", "w") as outfile:
    json.dump(result, outfile)

    #print("in json file")test
