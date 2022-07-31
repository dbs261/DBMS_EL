from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
import string

import datetime
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

# def get_sent(body):
#     body = body.lower()
#     body = body.translate(str.maketrans('', '', string.punctuation))

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        return 1
 
    elif sentiment_dict['compound'] <= - 0.05 :
        return -1
 
    else :
        return 0
 

def index(request):
    today = datetime.datetime.now().date()
    l=[]
    # for post in Post.objects.all():
    #     l.append(post.title+"AAAAAAAAAAAA")
    # print("--------------------------")
    
    for post in Post.objects.all():
        d={}
        sentiment = 0
        d['title'] = post.title
        d['body'] = post.body
        sentiment = sentiment_scores(post.body)

        if(sentiment==1):
            d['resp'] = "Glad you liked the content. Stay tuned for more"
        elif(sentiment==-1):
            d['resp'] = "We're very sorry to hear that. The content will gradually improve over time. Please bear with us."
        else:
            d['resp'] = "Hey! We noticed that you were neither satisfied nor dissatisfied with the content. Help us by commenting some more"
        l.append(d)
        # print(posts)
        # print(posts.title)
        # print(posts.body)
        # print("++++++++++++++++")
    # print("--------------------------")
    # return render(request, "index.html",{"today":today,"posts":Post.objects.all()})
    return render(request, "index.html",{"today":today,"posts":l})