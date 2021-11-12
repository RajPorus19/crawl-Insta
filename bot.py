import time

class Bot:
	def __init__(self,mail,password,canFollow,numOfLikes,commentText,browser):
                self.mail = mail
                self.password = password
                self.browser = browser
                self.canFollow = canFollow
                self.numOfLikes = numOfLikes
                self.commentText = commentText
	def login(self):
                self.browser.get("https://www.instagram.com/accounts/login")
                while True:
                    try:
                        accept_all = self.browser.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']")
                        accept_all.click()
                        break
                    except:
                        continue
                keepTry = True
                while keepTry:
                    try:
                        mail = self.browser.find_element_by_xpath("//input[@name='username']")
                        password = self.browser.find_element_by_xpath("//input[@name='password']")
                        submit = self.browser.find_element_by_xpath("//button[@type='submit']")
                        mail.click()
                        mail.send_keys(self.mail)
                        password.click()
                        password.send_keys(self.password)
                        submit.click()
                        keepTry=False
                        time.sleep(3)
                        break
                    except:
                            continue

	def isLiked(self):
		button = self.browser.find_element_by_xpath("//span[@class='fr66n']/button")
		if 'fill="#ed4956"' in button.get_attribute('innerHTML'):
			return True
		else:
			return False

	def getOnPage(self,user):
		self.browser.get("https://www.instagram.com/"+user)

	def getPostCount(self):
		return int(self.browser.find_elements_by_xpath("//span[@class='g47SY ']")[0].get_attribute('innerText'))

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

