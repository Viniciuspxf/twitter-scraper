from dotenv import load_dotenv
from twitter_scrapper.twitter_scraper import TwitterScraper
from twitter_scrapper.nitter_scraper import NitterScraper
import pandas

import os

USE_NITTER = True

if USE_NITTER:
    scraper = NitterScraper()
else:
    load_dotenv()
    scraper = TwitterScraper(os.environ["EMAIL"], os.environ["PASSWORD"], os.environ["PHONE"])

username = input("Digite o nome do usuário (ou deixe em branco, se não quiser filtrar por @): ")
hashtag = input("Digite a hashtag (ou deixe em branco, se não quiser filtrar por #): ")
keywords = input("Digite palavras chave separadas por espaço (ou deixe em branco, se não quiser filtrar por): ")
beginDate = input("Digite a data final no formato AAAA-MM-DD: ").strip()
endDate= input("Digite a data inicial no formato AAAA-MM-DD: ").strip()
filename = input("Digite o nome do arquivo: ")

tweets = scraper.searchForTweets(beginDate, endDate, username, hashtag, keywords)

dataframe = pandas.DataFrame.from_dict([tweets])
dataframe = dataframe.T
dataframe.to_excel(filename + ".xlsx")
print("FINALIZADO!")


