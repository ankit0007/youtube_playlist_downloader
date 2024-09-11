from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

# Directory to save downloaded videos
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        playlist_url = request.form.get("playlist_url")
        if playlist_url:
            try:
                download_videos(playlist_url)
                return f"All videos from the playlist '{playlist_url}' have been downloaded successfully."
            except Exception as e:
                return f"Error occurred: {str(e)}"
    return render_template("index.html")

def download_videos(playlist_url):
    try:
        ydl_opts = {
            'format': 'best',  # Download the best quality available
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',  # Save to the downloads folder
            'noplaylist': False,  # Ensure the entire playlist is downloaded
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])  # Download the playlist
        
        print(f"Downloaded playlist: {playlist_url}")

    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
