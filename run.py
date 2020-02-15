from flask import Flask,render_template
#from pytube import YouTube
import youtube_dl

app = Flask(__name__,static_folder='static')

@app.route('/')
def home():
    return 'Hello!'

@app.route('/video')
def video():
    return render_template("video.html")

@app.route('/yt')
'''
def video_yt():
    yt = YouTube("http://www.youtube.com/watch?v=AzguO9C8XG4")
    video = yt.streams.filter(file_extension='mp4').first()
    video.download(output_path='/app/static',filename='myFirstVideo')
    return render_template("yt.html")
'''

def download_video():
    videoURL = 'https://www.youtube.com/watch?v=IPsA3sz934M' 
    videoSavePath = '/app/static'          
    ydl_opts = {                
        'format': 'best[ext=mp4]/best',  
        'outtmpl': videoSavePath + "myFirstVideo.%(ext)s"  
    }          
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:               
    ydl.download([videoURL])
    return render_template("yt.html")

if __name__ == '__main__':   
    app.run(host='0.0.0.0', debug=True)
