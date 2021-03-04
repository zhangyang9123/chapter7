import os

def run(**argv):
    print ("[*] In dirlister module")
    files = os.listdir(".")

    return str(files)
