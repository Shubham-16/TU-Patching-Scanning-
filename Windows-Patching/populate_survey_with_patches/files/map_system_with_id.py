import os
import sys
import json

if __name__ == '__main__':
    all_system={}
    all_system=eval(sys.argv[1])
    list_of_dict=[]
    for key,value in all_system.items():
        ips=key.split(',')
        for ip in ips:
            j={}
            j['ip_address']=ip
            j['resource_id']=value
            list_of_dict.append(j)
    
    print(list_of_dict)
