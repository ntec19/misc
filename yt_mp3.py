from pytube import YouTube      # pour télécharger l'élément YT
# doc : https://pytube.io
from pydub import AudioSegment  # pour convertir en MP3 et ajouter des méta-données
# https://github.com/jiaaro/pydub/blob/master/API.markdown

url     = input("\nEntrez l'URL YT à convertir en MP3 : ")
yt      = YouTube(url)
a       = yt.author
t       = yt.title
at      = "["+a+"] "+t
y       = yt.streams.filter(only_audio=True).desc().first()
ext     = y.subtype

if a[-4:] == "VEVO":
    a = a[:-4]

print("\nAuteur - titre : "+at+"")
print("stream info :", y)
print("Enregistrement 1 sous : "+at+"."+ext)
print("Enregistrement 2 sous : "+at+".mp3\n")

y.download(filename=at+"."+ext)

sound   = AudioSegment.from_file(at+"."+ext)
sound.export(at+".mp3", format="mp3", tags={"title": t, "artist": a})

print("-------- terminé --------\n")
