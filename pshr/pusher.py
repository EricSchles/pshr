import time
import argparse
from subprocess import call

def main(msg,on_heroku=False,sleep_for=300,continuous=False):
    while True:
        call(["git","add","--all",":/"])
        call(["git","commit","-m",msg])
        call(["git","push"])
        if on_heroku:
            call(["git","push","heroku","master"])

        if continuous:
            time.sleep(sleep_for) #sleep for n seconds
        else:
            break
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="automatically push to github, every n minutes")
    parser.add_argument("--message",type=str, help="the message to be committed every n minutes to github")
    parser.add_argument("--on-heroku",type=bool, help="if you are pushing to heroku")
    parser.add_argument("--push-n-seconds",type=int, help="how long to wait between pushes in seconds")
    parser.add_argument("--continuous",type=bool,help="run this script continously")
    args = parser.parse_args()
    main(msg=args.message,on_heroku=args.on_heroku,sleep_for=args.push_n_seconds)


