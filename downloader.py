# from pytube import YouTube

# link = "https://www.youtube.com/watch?v=NwdQx2P_ytk"
# youtube1 = YouTube(link)

# # print(youtube1.title)
# # print(youtube1.thumbnail_url)
# video = youtube1.streams.all()
# # video = youtube1.streams.filter(only_audio=True)  only audio will be downloaded using this
# vid = list(enumerate(video))
# for i in vid:
#     print(i)
# print()
# strm = int(input("enter : "))
# video[strm].download()
# print("successfully downloaded the video")


#  ******** playlist downloading ************
from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PL0ZxPmRjddXu7jC2HrltJhbqpFXq2D_Ij")

print(f'downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()
