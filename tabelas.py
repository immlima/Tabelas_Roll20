import random
import os
chars = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-'



excesion=('txt')
for root, dirs, files in os.walk('.'):
    for name_table in files:
        
        txt='''
{
    "name": "'''+os.path.splitext(os.path.basename(open(name_table).name))[0]+'''",
    "showplayers": true,
    "id": "'''+''.join(random.sample(chars,16))+''.join(random.sample(chars,5))+'''",
    "items": {\n'''

        id=''.join(random.sample(chars,16))+''.join(random.sample(chars,5))
        txt=txt+'''        "'''+id+'''": {
                    "id":"'''+id+'''" ,
                    "name": "",
                    "weight": 0
            }'''
        if name_table.split(".")[-1] in excesion:
            for item in open(name_table, encoding='utf8'):
            
                if item.replace('\n','')!='':
                    id=''.join(random.sample(chars,16))+''.join(random.sample(chars,5))
                    txt=txt+',\n       "'
                    txt=txt+''+id
                    txt=txt+'''": {
            "id": "'''+id+'''",
            "name": "'''+item.replace('\n','')+'''"
        }'''
            txt=txt+'''
    }
}'''
            name_table=os.path.splitext(os.path.basename(open(name_table).name))[0]
            # print(name_table)
            with open(os.path.join(".",f"{name_table}.json"),"w",encoding='utf8') as my_file:
                my_file.write(txt)