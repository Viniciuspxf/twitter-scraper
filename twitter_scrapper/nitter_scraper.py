from driver.driver import Driver

class NitterScraper:
    def __init__(self):
        self.driver = Driver()

    def searchForTweets(self, beginDate, endDate, username = "", hashtag = "", keywords = ""):
        dictOfTweets = dict()
        self.driver.goToUrl(self.buildSearchUrl(beginDate, endDate, username, hashtag, keywords))
        
        while True:
            try:
                tweets = self.driver.findElementsByCSS(".tweet-body")
                for tweet in tweets:
                    datetime = tweet.findByCSS(".tweet-date a").get_attribute("title")
                    textElement = tweet.findByCSS(".tweet-content")
                    dictOfTweets[datetime] = textElement.get_text()
            except:
                break

            self.driver.findByXPathAndClick("//a[contains(text(), 'Load more')]")


        return dictOfTweets     

    def buildSearchUrl(self, beginDate, endDate, username, hashtag, keywords):
        keywordsList = keywords.split()
        url = "https://nitter.net/search?f=tweets&q="

        for keyword in keywordsList:
            url += '"'+ keyword +'"%20'

        if username:
            url += "(from%3A" + username + ")%20"

        if hashtag:
            url +="(%23" + hashtag + ")%20"

        url += "&until=" + beginDate +"&since="+ endDate

        return url
