import argparse
import yt_dlp
import pyperclip
import os

# ANSI escape code for red color
RED = "\033[31m"
GREEN = "\033[32m"
WHITE = "\033[37m"

def get_clipboard_link():
    return pyperclip.paste()

def download_video(url, resolution, output_format, path):
    output_folder = os.path.join(path, 'YTDownloader_Downloads')
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': f'bestvideo[height={resolution}]+bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': output_format,
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url, output_codec, path):
    output_folder = os.path.join(path, 'Media_Downloads')
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': output_codec,
                'preferredquality': '192',
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Add ffmpeg folder to the system path
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg')
    os.environ['PATH'] = os.pathsep.join([ffmpeg_path, os.environ['PATH']])
    os.environ['FFPROBE'] = os.path.join(ffmpeg_path, 'ffprobe')
    os.environ['FFPLAY'] = os.path.join(ffmpeg_path, 'ffplay')

    parser = argparse.ArgumentParser(description='Download a video or playlist from a given URL.')
    parser.add_argument('url', nargs='?', help='URL of the video or playlist to download')
    parser.add_argument('-r', '--resolution', default='1080p', help='Customize resolution (default: 1080p)')
    parser.add_argument('-f', '--format', default='mp3', help='Specify audio codec (default: mp3)')
    parser.add_argument('-p', '--path', default='.', help='Specify path to save the downloaded file(s)')
    parser.add_argument('-a', '--audio', action='store_true', help='Download as audio (default: video)')
    args = parser.parse_args()

    if args.url:
        print("Downloading from URL:", args.url)
        print("Output Codec:", args.format)
        print("Quality:", args.resolution)
        if args.audio:
            download_audio(args.url, args.format, args.path)
        else:
            download_video(args.url, args.resolution, args.format, args.path)
    else:
        clipboard_link = get_clipboard_link()
        if clipboard_link:
            print("Downloading from clipboard URL:", clipboard_link)
            print("Output Codec:", args.format)
            print("Quality:", args.resolution)
            if args.audio:
                download_audio(clipboard_link, args.format, args.path)
            else:
                download_video(clipboard_link, args.resolution, args.format, args.path)
        else:
            print("Error: Please provide the video or playlist URL as a command-line argument or copy a URL to the clipboard.")
