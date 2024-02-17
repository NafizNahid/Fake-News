from django.shortcuts import render
import numpy as np
import pandas as pd
import pickle
import re
import string

with open('savedModels\model (1)' , 'rb') as f:
    model = pickle.load(f)

# Create your views here.
def mlapp(request):
    def wordopt(t):
        t = t.lower()
        t = re.sub('\[.*?\]', '', t)
        t = re.sub("\\W"," ",t)
        t = re.sub('https?://\S+|www\.\S+', '', t)
        t = re.sub('<.*?>+', '', t)
        t = re.sub('[%s]' % re.escape(string.punctuation), '', t)
        t = re.sub('\n', '', t)
        t = re.sub('\w*\d\w*', '', t)
        return t
    if request.method == 'POST':
        News = request.POST['News']
        News = str(News)
        testing_news = {"text":[News]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(wordopt)
        new_x_test = new_def_test["text"]
        y_pred = model.predict(new_x_test)
        
        y =y_pred[0]
        y = int (y)
        # if y_pred == 0:
        #     y = "Fake News"
        # elif y_pred == 1:
        #     y = "Not A Fake News"  
        News1 = News[:900]    
        return render(request, 'mlapp/result.html', {'result' : y , 'news':News1})

    return render(request,'mlapp/ml.html')


def ml(request):
    return render(request, 'mlapp/ml.html')
