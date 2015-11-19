#Pshr

A simple command line tool that pushes either to git or git and heroku

##Usage:

**To github: (from the command line)**

python pusher.py --message [commit message] --on-heroku [True/False] --push-n-seconds [some number of seconds] --continuous [True/False]

**To github: (from a program)**

```
>>> from pshr import pusher
>>> pusher.main(msg="Hello there")
```
