# Youtube_playlist_downloader
 
```markdown
# YouTube Playlist Downloader

This is a simple Flask-based web application that allows users to download all videos from a YouTube playlist in the highest available quality using `yt-dlp`.

## Features

- Download entire YouTube playlists in HD quality
- User-friendly web interface built with Flask
- Automatically saves videos to a local `downloads/` folder

## Prerequisites

Before you begin, make sure you have the following installed:

1. **Python 3.x**: You can download Python from [here](https://www.python.org/downloads/).
2. **pip**: Python's package manager should come with Python 3.x. If it's missing, install it by following [these instructions](https://pip.pypa.io/en/stable/installation/).

## Installation Guide

Follow these steps to install and run the application locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/youtube_playlist_downloader.git
cd youtube_playlist_downloader
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage your project's dependencies.

- On Windows:

  ```bash
  python -m venv venv
  ```

- On macOS/Linux:

  ```bash
  python3 -m venv venv
  ```

### 3. Activate the Virtual Environment

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` in your terminal indicating that the virtual environment is active.

### 4. Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one by adding the following lines to it:

```txt
Flask
yt-dlp
```

Then, run the `pip install` command again:

```bash
pip install -r requirements.txt
```

### 5. Create Necessary Folders

The application saves downloaded videos in a `downloads/` folder. Make sure this folder exists or create it manually:

```bash
mkdir downloads
```

### 6. Run the Application

With all dependencies installed, you can now run the Flask application:

```bash
python app.py
```

By default, Flask runs the application on `http://127.0.0.1:5000/`. You can open this URL in your web browser.

### 7. Download YouTube Playlists

1. Open `http://127.0.0.1:5000/` in your web browser.
2. Enter a valid YouTube playlist URL.
3. Click "Download Playlist."
4. All videos from the playlist will be downloaded into the `downloads/` folder in the best available quality.

### 8. Deactivating the Virtual Environment

After you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```

## Troubleshooting

### Common Issues:

- **ModuleNotFoundError**: If you encounter a `ModuleNotFoundError` for Flask or `yt-dlp`, ensure that you're installing dependencies in the correct virtual environment.
- **yt-dlp Issues**: If `yt-dlp` is not downloading videos, ensure that you're using the latest version. You can update `yt-dlp` using:

  ```bash
  pip install --upgrade yt-dlp
  ```

### Additional Notes

- If you face any errors, try checking the terminal output for detailed error messages.
- Ensure that you are entering a valid YouTube playlist URL.

## License

This project is licensed under the MIT License.
```

### Summary of Steps

1. **Clone the repository**: Download the project files.
2. **Create a virtual environment**: Manage dependencies locally.
3. **Activate the virtual environment**: Prepare the environment for installation.
4. **Install dependencies**: Install Flask and `yt-dlp`.
5. **Create the `downloads/` folder**: The app needs this folder to save videos.
6. **Run the app**: Use the terminal to start the Flask server.
7. **Access the app in a browser**: Download YouTube playlists via the web interface.

This `README.md` should provide a clear step-by-step guide for setting up and running the project locally. Let me know if you need further assistance or modifications!


<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
<script>
  kofiWidgetOverlay.draw('smt2024', {
    'type': 'floating-chat',
    'floating-chat.donateButton.text': 'Support Me',
    'floating-chat.donateButton.background-color': '#00b9fe',
    'floating-chat.donateButton.text-color': '#fff'
  });
</script>
