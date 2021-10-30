# Find Wikipedia source

from mediawiki import MediaWiki
from imdbpie import Imdb

def choc():
    """"pulls data from chocolate cake wikipedia page"""
    wikipedia = MediaWiki()
    choc_cake = wikipedia.page("Chocolate_cake") # cake must be lowercase
    print(choc_cake.title)
    print(choc_cake.content)


def mov():
    """"pulls data from IMDB page"""
    imdb = Imdb()
    print(imdb.search_for_title("Venom")[0])
    reviews = imdb.get_title_user_reviews("tt1270797") # string from http

    # import pprint
    # pprint.pprint(reviews)

    print(reviews['reviews'][0]['author']['displayName'])
    print(reviews['reviews'][0]['reviewText'])


def  main():
    choc()
    # mov()


if __name__ == "__main__":
    main()
