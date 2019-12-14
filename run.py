from flask import Flask,render_template
from pytube import YouTube
import os

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return 'Hello!'

@app.route('/video')
def video():
    return render_template("video.html")

@app.route('/yt')
def video_yt():
    yt = YouTube("http://www.youtube.com/watch?v=Ik-RsDGPI5Y")
    #yt.set_filename('myFirstVideo')
    #video = yt.get('mp4','720p')
    video = yt.filter('.mp4')[-1]
    video.download('/templates')
    os.rename('/templates/'+yt.title+'.mp4','/templates/myFirstVideo.mp4'
    return render_template("yt.html")

if __name__ == '__main__':   
    app.run(host='0.0.0.0', debug=True)
