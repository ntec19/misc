from pytube import YouTube      # pour télécharger l'élément YT
# doc : https://pytube.io

url     = input("\nEntrez l'URL YT de la vidéo à télécharger : ")
yt      = YouTube(url)
a       = yt.author
t       = yt.title
at      = "["+a+"] "+t
y       = yt.streams.filter(progressive=True).filter(type="video").filter(mime_type="video/mp4").get_highest_resolution() # explication du filtre 'progressive=True' : https://pythonsansar.comdownload-youtube-videos-using-python-pytube/
ext     = y.subtype

print("\nAuteur - titre : "+at+"")
print("stream info :", y)
print("Enregistrement sous : "+at+"."+ext+"\n")
y.download(filename=at+"."+ext)
print("-------- terminé --------\n")
