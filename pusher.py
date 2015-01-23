from subprocess import call
from sys import argv

call(["git","add","-A"])
if argv[1] != "-h":
    call(["git","commit","-a","-m",argv[1]])
else:
    call(["git","commit","-a","-m",argv[2]])
call(["git","push"])
if argv[1] == "-h":
    call(["git","push","heroku","master"])
