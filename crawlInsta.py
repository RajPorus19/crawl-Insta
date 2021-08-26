import argparse
import sys
from bot import Bot
from selenium import webdriver

parser = argparse.ArgumentParser(description='Unofficial Instagram crawler bot written in Python, using Selenium WebDriver')
parser.add_argument('-e', help="The email you used for you Instagram account.")
parser.add_argument('-p', help="The password you used for you Instagram account.")
parser.add_argument('-f', action='store_true',help="This flag enables follow, by default off.")
parser.add_argument('-l', action='store_true',help="This flag enables likes, by default on.")
parser.add_argument('-c', help="This enables comments, by default off, you need to give it a String.")
parser.add_argument('-n', type=int, help="Number of post to interact with in an account, by default set to 1")
parser.add_argument('-u', help="User from what the crawling should start.")
parser.add_argument('-b', help="There are two supported drivers : 'chrome','geckodriver', Chrome is set by default.")
parser.add_argument('-gp', help="Geckodriver's path")

args = parser.parse_args() 

if __name__=='__main__':
    numOfPost = 1
    comment = ""

    if args.e == None or args.p == None:
        print("You cannot use this bot without an account.")
        sys.exit()
    if args.n != None:
        numOfPost = args.n
    if args.c != None:
        comment = args.c
    if args.u == None:
        print("Please provide a user to crawl from in the beginning")
        sys.exit()
    if args.b:
        if args.b not in ['chrome','geckodriver']:
            print("Please provide one of the supporter WebDriver.")
            sys.exit()
        elif args.b == 'geckodriver':
            if args.gp == None:
                print("Specify the path for the Geckodriver")
                sys.exit()
            else:
                browser = webdriver.Firefox(executable_path=args.gp)
    if not args.b:
        browser = webdriver.Chrome()
    myBot = Bot(args.e,args.p,args.f,numOfPost,comment,browser)
    myBot.login()
    myBot.crawlFrom(args.u)
