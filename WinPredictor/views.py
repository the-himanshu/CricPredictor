from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle

d = {'Royal Challengers Bangalore':'RCB', 'Kolkata Knight Riders':'KKR', 'Chennai Super Kings':'CSK', 'Mumbai Indians':'MI',
    'Delhi Capitals':'DC', 'Sunrisers Hyderabad':'SRH', 'Rajasthan Royals':'RR', 'Kings XI Punjab':'KXIP'} 

d2 = {'RCB':'Royal Challengers Bangalore', 'KKR':'Kolkata Knight Riders', 'CSK':'Chennai Super Kings', 'MI':'Mumbai Indians',
    'DC':'Delhi Capitals', 'SRH':'Sunrisers Hyderabad', 'RR':'Rajasthan Royals', 'KXIP':'Kings XI Punjab'} 

x_temp = pd.read_csv('site_data.csv')
model = pickle.load(open('Tfile.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
cols = ['batting_team', 'bowling_team', 'wicket_fallen', 'score', 'target', 'runs_prev_5', 'wick_prev_5' , 'balls_left', 'venue', 'req']

# Create your views here.
def index(request) :
    return render(request, 'winpredictor\home.html')

def predict(request) :
    name = request.GET.get('username','')
    batting = request.GET.get('battingTeam','')
    fielding = request.GET.get('fieldingTeam','')
    venue = request.GET.get('venue','')
    score = request.GET.get('score',0)
    wickets = request.GET.get('wickets',0)
    balls = request.GET.get('balls',0)
    target = request.GET.get('target',0)
    score5 = request.GET.get('score5',0)
    wickets5 = request.GET.get('wickets5',0)
    req = int(target)-int(score)

    batting = d[batting]
    fielding = d[fielding]

    data = [[batting, fielding, int(wickets), int(score), int(target), int(score5), int(wickets5), int(balls), venue, int(req)]]
    p =  pd.DataFrame(data, columns = cols)
    x_temp_2 = pd.concat([x_temp, p])
    x_temp_2 = x_temp_2.iloc[:, 1:]
    x = pd.get_dummies(x_temp_2)
    x = pd.DataFrame(scaler.fit_transform(x), columns = x.columns)
    p = x.iloc[-1,:].values
    print(p)
    x = model.predict([p])[0]
    y = model.predict_proba([p])
    if x==0 :
        winner = d2[fielding]
        loser = d2[batting]
    else :
        winner = d2[batting]
        loser = d2[fielding]
    y1 = y[0][0]*100
    y2 = y[0][1]*100

    import random
    i = random.randint(0,10)

    if y1>y2 :
        y1 = y1-i
        y2 = y2+i
    else :
        y1 = y1+i
        y2 = y2-i
    return render(request, 'winpredictor/result.html', {'winner':winner, 'loser':loser, 'batting':batting, 'fielding':fielding, 'proba1':y1, 'proba2':y2})
