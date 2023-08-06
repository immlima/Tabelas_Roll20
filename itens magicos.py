import os

meuArquivo = open("tabela suja.xd",encoding='utf8')

nome_tabela=meuArquivo.readline().replace('\n','')
n=1
for nome in meuArquivo:
    linnha=nome.replace('\n','').split(' ',1)
    #linnha[1]=linnha.split('–')
    if len(linnha[0].split('–'))>1:
        print(int(linnha[0].split('–')[1])+1-int(linnha[0].split('–')[0]),int(linnha[0].split('–')[0]),int(linnha[0].split('–')[1])+1)
        for i in range(int(linnha[0].split('–')[0]),int(linnha[0].split('–')[1])+1):
            with open(os.path.join(".",f"{nome_tabela}.txt"),"a",encoding='utf8') as my_file:
                my_file.write(f'{n} - {linnha[1]}\n')
                n=n+1
    else:    
        # print(linnha)
        
        with open(os.path.join(".",f"{nome_tabela}.txt"),"a",encoding='utf8') as my_file:
            my_file.write(f'{n} - {linnha[1]}\n')
            n=n+1
    