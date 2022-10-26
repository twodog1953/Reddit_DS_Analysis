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

# get comment result from a specific post
sub_name = 'notjustbikes'   # the name for the subreddit of the post
post_code = 'yckikv'    # the 5-digit code for each reddit post
res = requests.get("https://oauth.reddit.com/r/" + sub_name + "/comments/"+post_code,
                   headers=headers)
content = res.json()

# store all comments in the form of string here
all_comment = ''


def lst_print(l):
    # function to deal with list in the return result
    for i in l:
        if isinstance(i, list):
            lst_print(i)
        elif isinstance(i, dict):
            myprint(i)


def myprint(d):
    # function to deal with dictionary in the return result
    global all_comment
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        elif isinstance(v, list):
            lst_print(v)
        elif k == 'body':
            v = re.sub(r"http\S+", "", v)
            all_comment += v + ', '


lst_print(content)
print(all_comment)

# generate wordcloud here
wordcloud = WordCloud().generate(all_comment)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('comments_cloud.jpg')
plt.show()
