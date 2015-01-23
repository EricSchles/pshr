import time
def run(first="",second=False):
    from subprocess import call

    call(["git","add","-A"])
    time.sleep(0.001)
    call(["git","commit","-a","-m",first])
    time.sleep(0.001)
    call(["git","push"])
    time.sleep(0.001)
    if on_heroku:
        call(["git","push","heroku","master"])

if __name__ == '__main__':
    from sys import argv
    msg = argv[1]
    on_heroku = False
    try:
        msg = argv[2]
        on_heroku = True
    except:
        run(first=msg,second=on_heroku)
    run(first=msg,second=on_heroku)
