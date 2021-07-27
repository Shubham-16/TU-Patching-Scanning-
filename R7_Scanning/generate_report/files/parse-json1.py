import sys
import json


if __name__ == '__main__':
    scanId1 =  int(sys.argv[1])
    key = "scanId"
    #print(scanId)
    #file = open("./site-assets.json","rt")
    file = open("./site-assets1.json","rt")
    content = file.read()
    content =  json.loads(content)["resources"]
    file.close()
    #print(content)
    for obj1 in content:
        for obj2 in obj1["history"]:
          if key in obj2.keys(): 
            if ( (obj1["vulnerabilities"]["critical"] > 0) or (obj1["vulnerabilities"]["severe"] > 0) ):
                print(obj1["ip"])