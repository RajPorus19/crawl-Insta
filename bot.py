import time
import requests


class Bot:
    def __init__(self, mail, password, canFollow, numOfLikes, commentText, browser):
        self.mail = mail
        self.password = password
        self.browser = browser
        self.canFollow = canFollow
        self.numOfLikes = numOfLikes
        self.commentText = commentText
    def login(self):
        print("getting on login page")
        self.browser.get("https://www.instagram.com/accounts/login")
        while True:
            try:
                accept_all = self.browser.find_element_by_xpath(
                    "//button[@class='aOOlW  bIiDR  ']")
                accept_all.click()
                break
            except:
                continue
        keepTry = True
        while keepTry:
            try:
                mail = self.browser.find_element_by_xpath(
                    "//input[@name='username']")
                password = self.browser.find_element_by_xpath(
                    "//input[@name='password']")
                submit = self.browser.find_element_by_xpath(
                    "//button[@type='submit']")
                mail.click()
                mail.send_keys(self.mail)
                password.click()
                password.send_keys(self.password)
                submit.click()
                keepTry = False
                time.sleep(3)
                print("login succeeded")
                break
            except:
                print("failed login")
                continue

    def isLiked(self):
        button = self.browser.find_element_by_xpath("//span[@class='fr66n']/button")
        if 'fill="#ed4956"' in button.get_attribute('innerHTML'):
            print(self.browser.current_url, "is liked")
            return True
        else:
            print(self.browser.current_url, "is not liked")
            return False

    def getOnPage(self,user):
        print(self.browser.current_url, "page loaded")
        self.browser.get("https://www.instagram.com/"+user)

    def getPostCount(self):
        num = int(self.browser.find_elements_by_xpath("//span[@class='g47SY ']")[0].get_attribute('innerText'))
        print(self.browser.current_url, f"found {num} posts")
        return num

    def likeAndCommentNum(self,user,num):
        self.getOnPage(user)
        listPost = []
        while len(listPost)<= num:
            try:
                posts = self.browser.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
                for post in posts:
                    link = post.get_attribute('innerHTML').split('"')[1][1:]
                    if link not in listPost:
                        listPost.append(link)
            except:
                continue
        for ext in listPost[:num]:
            self.browser.get("https://www.instagram.com/"+user+'/'+ext)
            time.sleep(1)
            if(not self.isLiked()):
                            button = self.browser.find_element_by_xpath("//span[@class='fr66n']/button")
                            button.click()
                            time.sleep(3)
                            if self.commentText != '':
                                try:
                                    self.comment()
                                except:
                                    time.sleep(5)
                                    self.comment()
            else:
                            continue

    def comment(self):
            print(self.browser.current_url, "post was commented")
            commentBox = self.browser.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            commentBox.send_keys(self.commentText)
            submit = self.browser.find_element_by_xpath("//button[@type='submit']")
            submit.click()
    def crawlFrom(self,user):
        try:
                    self.getOnPage(user)
                    time.sleep(1)
                    if self.canFollow:
                        self.follow()
                    seeMore = self.browser.find_element_by_xpath("//span[@class='mLCHD _1OSdk']/button")
                    seeMore.click()
                    time.sleep(1.5)
                    try:
                        links = self.browser.find_elements_by_xpath("//a[@class='FPmhX notranslate  Qj3-a']")
                        name = links[0].get_attribute('innerHTML')
                    except:
                        self.crawlFrom(user)
                    self.likeAndCommentNum(user,self.numOfLikes)
                    self.crawlFrom(name)
        except:
            self.crawlFrom(user)
            
    def follow(self):
        button = self.browser.find_elements_by_xpath("//button")
        if button[0].get_attribute("innerHTML") == "Follow":
            button[0].click()

    def get_followers(self,username):

        self.getOnPage(username)

        url = "https://i.instagram.com/api/v1/friendships/19318909/followers/?count=10000&search_surface=follow_list_page"

        cookies = {}
        cookies["logs"] = self.browser.get_log("performance")
        cookies["mid"] = self.browser.get_cookie("mid")["value"]
        cookies["ig_did"] = self.browser.get_cookie("ig_did")["value"]
        cookies["csrftoken"] = self.browser.get_cookie("csrftoken")["value"]
        cookies["ds_user_id"] = self.browser.get_cookie("ds_user_id")["value"]
        cookies["sessionid"] = self.browser.get_cookie("sessionid")["value"]
        cookies["shbid"] = self.browser.get_cookie("shbid")["value"]
        cookies["shbts"] = self.browser.get_cookie("shbts")["value"]
        cookies["rur"] = self.browser.get_cookie("rur")["value"]


        headers = {}
        headers['authority'] = 'i.instagram.com' 
        headers['sec-ch-ua'] = "Chromium"
        headers['x-ig-www-claim'] = "hmac.AR0roQYoHzddxr_PSFuZ0cDN_QwNwafDgjIEWOtR-ovf4eGu"
        headers['sec-ch-ua-mobile'] = "?0"
        headers['user-agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        headers['accept'] = "*/*"
        headers['x-asbd-id'] = '198387' 
        headers['sec-ch-ua-platform'] = "Linux"
        headers['x-ig-app-id'] = '936619743392459' 
        headers['origin'] = 'https://www.instagram.com' 
        headers['sec-fetch-site'] = 'same-site' 
        headers['sec-fetch-mode'] = 'cors' 
        headers['sec-fetch-dest'] = 'empty' 
        headers['referer'] = 'https://www.instagram.com/' 
        headers['accept-language'] = 'en-US,en;q=0.9' 
        cookies_string = f"""mid={cookies["mid"]}; 
        ig_did={cookies["ig_did"]}; 
        csrftoken={cookies["csrftoken"]}; 
        ds_user_id={cookies["ds_user_id"]}; 
        sessionid={cookies["sessionid"]}; 
        shbid={cookies["shbid"]};
        shbts={cookies["shbts"]}; 
        rur={cookies["rur"]}"""
        headers['cookie'] = cookies_string.replace('\n','')


        res = requests.get(url, headers=headers)
        users = res.json()["users"]
        for user in users:
            print(user)

        print(res)
