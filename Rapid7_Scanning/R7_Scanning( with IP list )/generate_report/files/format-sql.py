import sys
import json


if __name__ == '__main__':

    file = open("generate_report/files/sql-query.txt","rt")
    content = file.read()
    c4 = content.replace("\n"," ")
    #c5 = c4.replace(" \" ",' \\" ')
    c5 = c4.replace("\t", " ")
    c6 = c5.replace('\"','\\"')
    file.close()    
    print(c6)