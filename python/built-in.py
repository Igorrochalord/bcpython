"""
automatizando o processo de gravaçao
"""

filename=input("digite o nome do arquivo: ")
filename=filename+".txt"
arq3=open(filename, "w")
arq3.write("incluindo texto no arquivo criado")
arq3.close()
arq3.open(filename,"r")
print (arq3.read())
arq3.close()