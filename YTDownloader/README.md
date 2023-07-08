# YTDownloader

YTDownloader : A Youtube/Youtube Playlist downloader using yt-dlp library

## Installer

1.First install [python](https://www.python.org/downloads/)
2.You can download as zip or using `git` to clone the code.

- If you using git please git clone this Project

```
git clone https://github.com/ChongZhiJie0216/python-lib-tools.git
```

3.After Install RUN `python-library-install.cmd`
4.Finish

## Using

1.Open `RUN(CMD).bat` on your download location
2.Using `python` to RUN

- `python YTDownloader.py `

## Command

```
python YTDownloader.py -h
```

```
  -h, --help            show this help message and exit

  -r RESOLUTION, --resolution RESOLUTION
                Customize resolution (default: 1080p)

  -f FORMAT, --format FORMAT
            Specify output format (default: mp4)

  -a, --audio           Download as audio (default: video)
```

# Example

## General

Video : `python YTDownloader.py -r 1080p -f mp4`
Audio : `python YTDownloader.py -a`

If need download to custom path loaction add `-p`,if you don't have set any location it will save in current location folder Names with `YTDownloader_Downloads`

### Example

Video : `python YTDownloader.py -r 1080p -f mp4 -p "E:\00-Windows Data\Videos"`
Audio : `python YTDownloader.py -a -p "E:\00-Windows Data\Music"`

# !!! All Media was save in `YTDownloader_Downloads` Folder
