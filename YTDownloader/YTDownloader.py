import argparse
import yt_dlp
import pyperclip
#Import 导入模块：代码开头导入了三个模块：argparse、yt_dlp和pyperclip。argparse 用于解析命令行参数，yt_dlp 是一个 YouTube 视频下载器的库，pyperclip 用于访问系统剪贴板。

def get_clipboard_link():
    return pyperclip.paste()
#定义函数 get_clipboard_link()：这个函数用于获取系统剪贴板中的内容，即复制的 URL。

def download_video(url, resolution, output_format):
    ydl_opts = {
        'format': f'bestvideo[height={resolution}]+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
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
#定义函数 download_video(url, resolution, output_format)：这个函数用于下载单个视频。
#它接受三个参数：视频的 URL、分辨率和输出格式。函数内部使用了 yt_dlp 库来下载视频，通过设置 ydl_opts 字典来指定下载选项。

def download_playlist(url, resolution, output_format):
    ydl_opts = {
        'format': f'bestvideo[height={resolution}]+bestaudio/best',
        'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': output_format,
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    #定义函数 download_playlist(url, resolution, output_format)：这个函数用于下载整个播放列表。
    #它接受三个参数：播放列表的 URL、分辨率和输出格式。函数内部同样使用了 yt_dlp 库来下载播放列表。

def download_audio(url, output_format):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
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
    #定义函数 download_audio(url, output_format)：这个函数用于下载音频文件。它接受两个参数：音频文件的 URL 和输出格式。
    #函数内部同样使用了 yt_dlp 库，但这里只下载音频部分

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download a video or playlist from a given URL.')
    #创建参数解析器 argparse.ArgumentParser()：使用 argparse 模块创建一个参数解析器对象，用于解析命令行参数。
    parser.add_argument('url', nargs='?', help='URL of the video or playlist to download')
    parser.add_argument('-r', '--resolution', default='1080p', help='Customize resolution (default: 1080p)')
    parser.add_argument('-f', '--format', default='mp4', help='Specify output format (default: mp4)')
    parser.add_argument('-a', '--audio', action='store_true', help='Download as audio (default: video)')
    #添加命令行参数：使用 parser.add_argument() 方法添加命令行参数。这里有四个参数：url（视频或播放列表的 URL）、
    # -r 或 --resolution（自定义分辨率，默认为 1080p）、
    # -f 或 --format（指定输出格式，默认为 mp4）、
    # -a 或 --audio（下载为音频，默认为视频）。
    args = parser.parse_args()
    #解析命令行参数：使用 parser.parse_args() 方法解析命令行参数，并将结果保存在 args 变量中

    if args.url:
        print("Downloading from URL:", args.url)  # Print user input URL
        print("Output Format:", args.format)  # Print user input output format
        print("Quality:", args.resolution)  # Print user input quality
        if args.audio:
            download_audio(args.url, args.format)
        else:
            download_video(args.url, args.resolution, args.format)
    else:
        clipboard_link = get_clipboard_link()
        if clipboard_link:
            print("Downloading from clipboard URL:", clipboard_link)  # Print user input URL
            print("Output Format:", args.format)  # Print user input output format
            print("Quality:", args.resolution)  # Print user input quality
            if args.audio:
                download_audio(clipboard_link, args.format)
            else:
                download_video(clipboard_link, args.resolution, args.format)
        else:
            print("Error: Please provide the video or playlist URL as a command-line argument or copy a URL to the clipboard.")
    #根据命令行参数进行下载：根据解析得到的命令行参数，进行相应的下载操作。首先判断是否提供了 URL，如果提供了 URL，则根据参数选择调用 download_audio() 或 download_video() 函数来下载。
    #如果没有提供 URL，则获取剪贴板中的 URL，并进行相应的下载操作。如果剪贴板中也没有 URL，则输出错误提示信息。
