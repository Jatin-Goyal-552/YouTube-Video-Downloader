from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
import os
def index(request):
    return render(request,"index.html")

def result(request):
    link=request.GET.get('text','default')
    url = link
    global url2
    url2 = link

    resolutions=[]
    # params={"vlink":link}
    yt = YouTube(link)
    al=yt.streams.filter(progressive=True,file_extension='mp4').all()
    for i in al:
        resolutions.append(i.resolution)
    # yt = yt.streams.filter(progressive=True, file_extension='mp4',res="360p").desc().first()
    # yt.download('a.mp4')
    resolutions=list(dict.fromkeys(resolutions))
    link = url.replace("watch?v=", "embed/")
    params={"reso":resolutions,"vlink":link}
    print(resolutions)
    return render(request,"result.html",params)

def download(request,res):
    global url2
    print(url2)
    homedir=os.path.expanduser("~")
    dirs=homedir + '/Downloads'
    print(dirs)

    YouTube(url2).streams.get_by_resolution(res).download(homedir + '/Downloads')
    return render(request,"download.html")