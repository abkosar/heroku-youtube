from bs4 import BeautifulSoup
import requests
from bottle import request, Bottle, run
import html_files
import os


app = Bottle()


class items:
    def getValue(self, url):
        self.url = url
        self.items_in = {}
        self.soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for self.title in self.soup.findAll("h1", {"id": "ytitle"}):
            self.items_in["song"] = self.title.text
        self.duration_list_id = []
        for self.duration in self.soup.findAll("small"):
            self.duration_list_id.append(
                self.duration.text.lstrip("Length: ").split("&nbsp;&nbsp;")[0].split(" ")[0].rstrip("\xa0\xa0"))
        self.items_in["duration_time"] = self.duration_list_id[0]
        for self.m4a in self.soup.findAll("a", {"data-itag": "140"}):
            try:
                self.items_in["sound"] = self.m4a.get("href").replace("GenYoutube.net_", "")
            except:
                self.items_in["sound"] = None
        self.items_in["hd_video"] = "#"
        self.items_in["hd_true"] = "hd not available"
        for self.mp4_720p in self.soup.findAll("a", {"data-itag": "22"}):
            self.items_in["hd_video"] = self.mp4_720p.get("href").replace("GenYoutube.net_", "")
            self.items_in["hd_true"] = "Download"
        for mp4_360p in self.soup.findAll("a", {"data-itag": "18"}):
            try:
                self.items_in["video_360p"] = mp4_360p.get("href").replace("GenYoutube.net_", "")
            except:
                self.items_in["video_360p"] = None

        return self.items_in


class items_list:
    def getList(self, url):
        self.list_in = {}
        self.url = "https://www.genyoutube.net/search.php?q={}".format(url)
        self.soup = BeautifulSoup(requests.get(self.url).content, "html.parser")
        self.link_list = []
        self.img_list = []
        self.text_list = []
        self.duration_list = []
        for self.a in self.soup.findAll("div", {"class": "col-xs-6 col-sm-4 col-md-4 vidbox"}):
            for self.video_link in self.a.findAll("a", {"class": "_moviethumb"}):
                self.link_list.append(self.video_link.get("href"))
            for self.img_link in self.a.findAll("img", {"class": "downloadimg"}):
                self.img_list.append(self.img_link.get("src"))
            for self.text in self.a.findAll("a", {"class": "moviea"}):
                self.text_list.append(self.text.text)
            for self.duration in self.a.findAll("span", {"class": "duration"}):
                self.duration_list.append(self.duration.text)

        self.list_in["link_list"] = self.link_list
        self.list_in["img_list"] = self.img_list
        self.list_in["text_list"] = self.duration_list
        self.list_in["duration_list"] = self.text_list

        return self.list_in

@app.get("/")
def youtube():
    return html_files.index()


@app.post("/search-youtube")
def youtube_list():
    global name
    name = request.forms.search_youtube
    if name.startswith("https://www.youtube.com") or name.startswith("https://m.youtube.com"):
        if name.startswith("https://m.youtube.com/"):
            url = name.split("https://m.youtube.com/watch?v=")[1]
            return '<meta http-equiv="refresh" content="0;URL=/video-details-url/{}">'.format(url)
        else:
            url = name.split("https://www.youtube.com/watch?v=")[1]
            return '<meta http-equiv="refresh" content="0;URL=/video-details-url/{}">'.format(url)
    elif name.startswith("https://youtu.be/"):
        url = name.split("https://youtu.be/")[1]
        return '<meta http-equiv="refresh" content="0;URL=/video-details-url/{}">'.format(url)
    else:
        return '<meta http-equiv="refresh" content="0;URL=/list-video/{}">'.format(name)


@app.get("/list-video/<search:path>")
def list_video(search):
    name = search
    item_list = items_list()
    value_list = item_list.getList(name)
    img_list = value_list["img_list"]
    link_list = value_list["link_list"]
    text_list = value_list["text_list"]
    duration_list = value_list["duration_list"]

    return html_files.yt_list().format(
        name, img_list[0], img_list[1], img_list[2], img_list[3], img_list[4], img_list[5], img_list[6], img_list[7],
        img_list[8], img_list[9], img_list[10], img_list[11], img_list[12], img_list[13], img_list[14], img_list[15],
        img_list[16], img_list[17], img_list[18], img_list[19], img_list[20], name,
        link_list[0].split("https://video.genyoutube.net/")[1], text_list[0], duration_list[0],
        link_list[1].split("https://video.genyoutube.net/")[1], text_list[1], duration_list[1],
        link_list[2].split("https://video.genyoutube.net/")[1], text_list[2], duration_list[2],
        link_list[3].split("https://video.genyoutube.net/")[1], text_list[3], duration_list[3],
        link_list[4].split("https://video.genyoutube.net/")[1], text_list[4], duration_list[4],
        link_list[5].split("https://video.genyoutube.net/")[1], text_list[5], duration_list[5],
        link_list[6].split("https://video.genyoutube.net/")[1], text_list[6], duration_list[6],
        link_list[7].split("https://video.genyoutube.net/")[1], text_list[7], duration_list[7],
        link_list[8].split("https://video.genyoutube.net/")[1], text_list[8], duration_list[8],
        link_list[9].split("https://video.genyoutube.net/")[1], text_list[9], duration_list[9],
        link_list[10].split("https://video.genyoutube.net/")[1], text_list[10], duration_list[10],
        link_list[11].split("https://video.genyoutube.net/")[1], text_list[11], duration_list[11],
        link_list[12].split("https://video.genyoutube.net/")[1], text_list[12], duration_list[12],
        link_list[13].split("https://video.genyoutube.net/")[1], text_list[13], duration_list[13],
        link_list[14].split("https://video.genyoutube.net/")[1], text_list[14], duration_list[14],
        link_list[15].split("https://video.genyoutube.net/")[1], text_list[15], duration_list[15],
        link_list[16].split("https://video.genyoutube.net/")[1], text_list[16], duration_list[16],
        link_list[17].split("https://video.genyoutube.net/")[1], text_list[17], duration_list[17],
        link_list[18].split("https://video.genyoutube.net/")[1], text_list[18], duration_list[18],
        link_list[19].split("https://video.genyoutube.net/")[1], text_list[19], duration_list[19],
        link_list[20].split("https://video.genyoutube.net/")[1], text_list[20], duration_list[20])


@app.get("/video-details-url/<vid:path>")
def send_yt_url(vid):
    url = "http://video.genyoutube.net/{}".format(vid)
    item = items()
    values = item.getValue(url=url)
    song = values["song"].replace(" ", "_")
    duration_time = values["duration_time"]
    hd_video = values["hd_video"]
    hd_true = values["hd_true"]
    video_360p = values["video_360p"]
    sound = values["sound"]
    import urllib.request 
    urllib.request.urlretrieve(sound, song + ".m4a")

    if hd_video == "#":
        return html_files.video_details().format(song, video_360p, song, duration_time, hd_video, hd_true, video_360p,
                                                 song + ".m4a")
    else:
        return html_files.video_details().format(song, hd_video, song, duration_time, hd_video, hd_true, video_360p,
                                                 song + ".m4a")
@app.get("<filepath:re:.*\.m4a>")
def m4a(filepath):
    return static_file(filepath, root="")
    
    
@app.post("/video-details")
def send_yt():
    video_id = request.forms.youtube_id
    url = "http://video.genyoutube.net/{}".format(video_id)
    item = items()
    values = item.getValue(url=url)
    song = values["song"]
    duration_time = values["duration_time"]
    hd_video = values["hd_video"]
    hd_true = values["hd_true"]
    video_360p = values["video_360p"]
    sound = values["sound"]

    if hd_video == "#":
        return html_files.video_details().format(song, video_360p, song, duration_time, hd_video, hd_true, video_360p, sound)
    else:
        return html_files.video_details().format(song, hd_video, song, duration_time, hd_video, hd_true, video_360p, sound)


run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
