import argparse
import yt_dlp
import pyperclip

# ANSI escape code for red color
RED = "\033[31m"
GREEN = "\033[32m"
WHITE = "\033[37m"

def get_clipboard_link():
    return pyperclip.paste()

def download_video(url, resolution, output_format, path):
    ydl_opts = {
        'format': f'bestvideo[height={resolution}]+bestaudio/best',
        'outtmpl': path + '/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': output_format,
            }
        ],
        'external_downloader_args': ['-hwaccel', 'cuda'],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist(url, resolution, output_format, path):
    ydl_opts = {
        'format': f'bestvideo[height={resolution}]+bestaudio/best',
        'outtmpl': path + '/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': output_format,
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url, output_format, path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path + '/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': output_format,
                'preferredquality': '192',
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download a video or playlist from a given URL.')
    parser.add_argument('url', nargs='?', help='URL of the video or playlist to download')
    parser.add_argument('-r', '--resolution', default='1080p', help='Customize resolution (default: 1080p)')
    parser.add_argument('-f', '--format', default='mp4', help='Specify output format (default: mp4)')
    parser.add_argument('-p', '--path', default='.', help='Specify path to save the downloaded file(s)')
    parser.add_argument('-a', '--audio', action='store_true', help='Download as audio (default: video)')
    args = parser.parse_args()

    if args.url:
        print("Downloading from URL:", args.url)
        print("Output Format:", args.format)
        print("Quality:", args.resolution)
        if args.audio:
            download_audio(args.url, args.format, args.path)
        else:
            download_video(args.url, args.resolution, args.format, args.path)
    else:
        clipboard_link = get_clipboard_link()
        if clipboard_link:
            print("Downloading from clipboard URL:", clipboard_link)
            print("Output Format:", args.format)
            print("Quality:", args.resolution)
            if args.audio:
                download_audio(clipboard_link, args.format, args.path)
            else:
                download_video(clipboard_link, args.resolution, args.format, args.path)
        else:
            print("Error: Please provide the video or playlist URL as a command-line argument or copy a URL to the clipboard.")
