from flask import Flask
from flask import render_template, request, flash

from pytubefix import YouTube
from pytubefix.cli import on_progress


app = Flask(__name__)
app.secret_key = "flask_download_video_youtube"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        video.download()
        flash(f"DOWNLOAD COMPLETO!\nVideo: {yt.title}")

        return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run()