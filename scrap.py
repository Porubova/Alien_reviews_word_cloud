import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud , STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import multidict as multidict
import re
import  random
##link to reviews
url = " https://www.imdb.com/title/tt0078748/reviews?ref_=tt_urv"
# get url data
r = requests.get(url)
#scrap page with reviews
bs = BeautifulSoup(r.text, features="html.parser")
#optionl print to derermin html tags containing reviews
#print(bs)

reviews = []
## loop frough all reviews and store them in list
for review in bs.find_all('div', class_="text show-more__control"):
    #print(review.string)
    if review != None:
        reviews.append(str(review.text))
print("Number of reviews: ", len(reviews))

text = " ".join(reviews)

def green_funct(word, font_size, position, orientation, random_state=None,
                **kwargs):
    a=  "hsl(97, 100%%, %d%%)" % random.randint(60, 100)
    print(a)
    return a
# Display the generated image:
# the matplotlib way:
def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be|has|can|up|her|have", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

def makeImage(text):
    alice_mask = np.array(Image.open("logo.jpg"))# https://www.pinterest.com/pin/228909593535961292

    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="black", max_words=1000,
                   mask=alice_mask, stopwords=stopwords)

    wc.generate_from_frequencies(text)


    # show
    plt.imshow(wc.recolor(color_func=green_funct, random_state=3), interpolation="bilinear")
    plt.axis("off")
    plt.show()
makeImage(getFrequencyDictForText(text))
