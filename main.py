from flask import Flask,render_template,request
from os import link
from urllib.request import urlopen
import time
from pytube import YouTube
from pytube import Playlist
import datetime 

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clac", methods=['GET', 'POST'])
def clac():
    if request.method == 'POST':
        url = request.form["address"]
        p = Playlist(url)
        t = 0 
        for video in p.videos:
            t += video.length
        convert = datetime.timedelta(seconds=t)
        
        return render_template("result.html",convert=convert)
    else:
        return render_template("index.html")


@app.route('/back',methods=['GET', 'POST'] )
def back():
    if request.method == 'POST':
        return render_template("index.html")
    render_template("index.html")

if __name__ == "__main__":
    app.run()