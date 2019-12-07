from flask import Flask
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    yt = YouTube("http://www.youtube.com/watch?v=Ik-RsDGPI5Y")
    yt.set_filename('myFirstVideo')
    #video = yt.get('mp4','720p')
    video = yt.filter('.mp4')[-1]
    video.download('/')
    
    app.run(host='0.0.0.0', debug=True)
