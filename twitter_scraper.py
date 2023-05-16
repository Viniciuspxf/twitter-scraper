from driver.driver import Driver

class TwitterScraper:
    def __init__(self, email, password, phone):
        self.driver = Driver()
        self.driver.goToUrl("https://twitter.com/")


        self.driver.findByCSSAndClick("#layers > div > div:nth-child(1) > div > div > div > div > div > div > div > div:nth-child(1) > a > div")

        self.driver.findByCSSAndWrite("input[autocomplete='username']", email)

        self.driver.findByXPathAndClick("//span[contains(text(), 'Next')]")

        try:
            self.driver.findByCSSAndWrite("input[autocomplete='current-password']", password)
            self.driver.findByXPathAndClick("//span[contains(text(), 'Log in')]", 1)
        except:
            self.driver.findByCSSAndWrite("input[autocomplete='on']", phone)
            self.driver.findByXPathAndClick("//span[contains(text(), 'Next')]")

            self.driver.findByCSSAndWrite("input[autocomplete='current-password']", password)
            self.driver.findByXPathAndClick("//span[contains(text(), 'Log in')]", 1)
            
        self.driver.findElementsByCSS("a[href='/home']")

    def searchForTweets(self, beginDate, endDate, username = "", hashtag = "", keywords = ""):
        dictOfTweets = dict()
        self.driver.goToUrl("https://twitter.com/")
        self.driver.goToUrl(self.buildSearchUrl(beginDate, endDate, username, hashtag, keywords))

        previousHeight = -1
        currentHeight = 0
        
        while previousHeight != currentHeight:
            tweets = self.driver.findElementsByCSS("article[data-testid='tweet']")

            for tweet in tweets:
                datetime = tweet.findByCSS("time").get_attribute("datetime")
                textElement = tweet.findByCSS("div[data-testid='tweetText']")
                dictOfTweets[datetime] = textElement.get_text()

            self.driver.scrollDown()
            currentHeight, previousHeight = self.driver.getPageHeight(), currentHeight

        return dictOfTweets     

    def buildSearchUrl(self, beginDate, endDate, username, hashtag, keywords):
        keywordsList = keywords.split()
        url = "https://twitter.com/search?q="

        for keyword in keywordsList:
            url += '"'+ keyword +'"%20'

        if username:
            url += "(from%3A" + username + ")%20"

        if hashtag:
            url +="(%23" + hashtag + ")%20"

        url += "until%3A" + beginDate +"%20since%3A"+ endDate +"&src=typed_query&f=live"

        return url




        


        