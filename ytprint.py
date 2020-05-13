from pytube import YouTube
import pysubs2
import os

subs = YouTube(input("YouTube video URL: ")).captions.get_by_language_code('en').generate_srt_captions()

f = open("subs.srt", "w+")
f.write(subs)
f.close()
subs = pysubs2.load("subs.srt")
os.remove("subs.srt")

text = ""
for line in subs:
  text+=(line.text+"\n")
print(text)
