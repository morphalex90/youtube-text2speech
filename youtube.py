filename = "output/yt_audio.mp3"

# Download YouTube video as Audio ------------------------------------------
import pytube as pt
yt = pt.YouTube("https://www.youtube.com/shorts/J4HXVfi9FKw")
stream = yt.streams.filter(only_audio=True)[0]
stream.download(filename=filename)


# Local Audio transcription ------------------------------------------
import whisper
model = whisper.load_model("base")
result = model.transcribe(filename, fp16=False, language="en")
transcription_text = result['text']
print(transcription_text)


# Generate audio from text ------------------------------------------
from gtts import gTTS

myobj = gTTS(text=transcription_text, lang='en', tld='co.uk', slow=False)
myobj.save("output/converted.mp3")