import sys
import json


if __name__ == '__main__':
    scanId1 =  int(sys.argv[1])
    key = "scanId"
    #print(scanId)
    file = open("./site-assets.json","rt")
    #file = open("./site-assets1.json","rt")
    content = file.read()
    content1 =  json.loads(content)["resources"]
    file.close()
    #print(content)
    for obj1 in content1:
        for obj2 in obj1["history"]:
          if key in obj2.keys(): 
            if (((obj2["scanId"] == scanId1 ) and (obj1["vulnerabilities"]["critical"] > 0)) or ((obj2["scanId"] == scanId1 ) and (obj1["vulnerabilities"]["severe"] > 0)) ):
                print(obj1["ip"])