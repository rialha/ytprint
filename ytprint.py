from pytube import YouTube
import pysubs2
import os

# Fetch the YouTube captions in a format the program can read
subs = YouTube(input("YouTube video URL: ")).captions.get_by_language_code('en').generate_srt_captions()

f = open("subs.srt", "w+")
f.write(subs)
f.close()
subs = pysubs2.load("subs.srt")
os.remove("subs.srt")
text = ""

# Add every line to be printed, and print it out at the end
for line in subs:
  text+=(line.text+"\n")
print(text)
