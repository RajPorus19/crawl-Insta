![demo gif](bot.gif)

# Unofficial Instagram Web Crawler

This is an unofficial Instagram crawler bot written in Python, using Selenium WebDriver.
I am not responsable for any issues you might get from Instagram, from my experience this bot was rather slow, and slow enough to not get spotted by Instagram's algorithm.
But I would still suggest you to not run it for too long if you consider using this for growth-hacking.
Feel free to fork it change it however you want and share any issues you encounter !

## What does it do ?

Given a start user "-u", it crawls to other users using Instagram's recommendation.

We Specify with how many posts per user we want to interact with, for example 3 posts : "-n 3" 

And then the flags "-f", "-l", "-c" will be in charge to (f)ollow, (l)ike and ( c)omment on these posts.

## Installation

```
pip install -r requirements.txt
```
Then install the geckodriver from selenium if you need to.
https://github.com/mozilla/geckodriver/releases/tag/v0.28.0
You won't need any drivers with chromium.

## Usage

```
$ python crawlInsta.py -h
usage: crawlInsta.py [-h] [-e E] [-p P] [-f] [-l] [-c C] [-n N] [-u U] [-b B] [-gp GP]

Unofficial Instagram crawler bot written in Python, using Selenium WebDriver

optional arguments:
  -h, --help  show this help message and exit
  -e E        The email you used for you Instagram account.
  -p P        The password you used for you Instagram account.
  -f          This flag enables follow, by default off.
  -l          This flag enables likes, by default on.
  -c C        This enables comments, by default off, you need to give it a String.
  -n N        Number of post to interact with in an account, by default set to 1
  -u U        User from what the crawling should start.
  -b B        There are two supported drivers : 'chrome','geckodriver', Chrome is set by default.
  -gp GP      Geckodriver's path

```
### Example 

```
$ python crawlInsta.py -e "your@email.com" -p "yourPassword" -f -l -n 3 -c "Hi there I am a bot !" -u "github"
```
