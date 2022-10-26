import requests
import initialize
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import re

# initialize (personal use script, secret token, username, password)
headers = initialize.start('<your personal use script>>',
                           '<your secret token>',
                           '<your reddit username>',
                           '<your reddit password>')

# get hot result
sub_name = 'notjustbikes'   # the name of the subreddit you wanna explore
res = requests.get("https://oauth.reddit.com/r/" + sub_name + "/hot",
                   headers=headers)

content = res.json()

# get all the self text in the post
self_text = ''
for i in content['data']['children']:
    sentence = i['data']['selftext']
    print(sentence)
    if sentence != '':
        sentence = re.sub(r"http\S+", "", sentence)
        self_text += sentence + ', '
print(self_text)

# generate wordcloud
wordcloud = WordCloud().generate(self_text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('top_cloud.jpg')
plt.show()
