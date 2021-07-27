# To parse the site asset ips using python script
# import sys
# import json


# if __name__ == '__main__':
#     iplist =  int(sys.argv[1])
#     #key = "scanId"
#     #print(scanId)
#     file = open("./site-assets-check.json","rt")
#     content = file.read()
#     content =  json.loads(content)["resources"]
#     file.close()
#     #print(content)
#     for item in content:
#         iplist1=[]
#         iplist1.append(item["ip"])
#     #intersection of site asset ip and valid ips
#     final_list = set(iplist1).intersection(iplist)
    