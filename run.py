from flask import Flask,render_template
import faceRead

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result",methods=['POST','GET'])
def result():
    res = faceRead.readImage()
    song = res['song']
    playlist = res['playlist']
    mood = res['mood']
    imgUrl = res['imgUrl']
    AlbumName = res['AlbumName']
    if(mood):
        print(song,mood,playlist)
    return render_template("index.html",mood=mood,playlist=playlist,song=song,imgUrl=imgUrl,AlbumName=AlbumName)

if __name__ == '__main__':
    app.run(debug=True,port=5001)