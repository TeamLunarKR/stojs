from bs4 import BeautifulSoup
import requests
import time

def get_soup(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


def 경기결과_가져오기():
    game_list = {
        "request_date":time.strftime("%Y-%m-%d %H:%M:%S"),
        "games":[
            {
                "place":"",
                "time":'-1',
                "team1":{
                    "name":"",
                    "score":'-1'
                },
                "team2":{
                    "name":"",
                    "score":'-1'
                },
                "status":""
            },
            {
                "place":"",
                "time":'-1',
                "team1":{
                    "name":"",
                    "score":'-1'
                },
                "team2":{
                    "name":"",
                    "score":'-1'
                },
                "status":""
            },
            {
                "place":"",
                "time":'-1',
                "team1":{
                    "name":"",
                    "score":'-1'
                },
                "team2":{
                    "name":"",
                    "score":'-1'
                },
                "status":""
            },
            {
                "place":"",
                "time":'-1',
                "team1":{
                    "name":"",
                    "score":'-1'
                },
                "team2":{
                    "name":"",
                    "score":'-1'
                },
                "status":""
            },
            {
                "place":"",
                "time":'-1',
                "team1":{
                    "name":"",
                    "score":'-1'
                },
                "team2":{
                    "name":"",
                    "score":'-1'
                },
                "status":""
            }
        ]
    }

    soup = get_soup("https://www.koreabaseball.com/Schedule/ScoreBoard.aspx")
    teams = soup.find_all("strong", {"class":"teamT"})
    for i in range(len(teams)):
        if not i%2:
            game_list['games'][int(i/2)]['team1']['name'] = teams[i].text
        if i%2:
            game_list['games'][int(i/2)]['team2']['name'] = teams[i].text
        
    place = soup.find_all("p", {"class":"place"})
    for i in range(len(place)):
        place[i] = str(place[i]).split(" <span>")
        game_list['games'][i]['place'] = place[i][0][-2:]
        game_list['games'][i]['time'] = place[i][1][:5]
    
    status = soup.find_all("strong",{"class":"flag"})
    for i in range(len(status)):
        game_list['games'][i]['status'] = status[i].text

        score = soup.find_all("em", {"class":"score"})
        for i in range(len(score)):
            try:
                if not i%2:
                    game_list['games'][int(i/2)]['team1']['score'] = score[i].text
                if i%2:
                    game_list['games'][int(i/2)]['team2']['score'] = score[i].text
            except:
                pass
    
    
    return str(game_list)
    
from flask import Flask, render_template, request, jsonify
import flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)

print(경기결과_가져오기())
@app.route("/")
def asdf():
    res = flask.Response(경기결과_가져오기())
    res.access_control_allow_origin = "0.0.0.0"
    return res

if __name__ == '__main__':
   app.run('0.0.0.0',port=8000,debug=True,use_reloader=False)