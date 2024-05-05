# Download the YouTube video and speech to text
def download_and_stt(youtube_url):
    folder = "output/"
    filename = folder + youtube_url

    # Download YouTube video as Audio ------------------------------------------
    import pytube as pt
    yt = pt.YouTube("https://www.youtube.com/watch?v=" + youtube_url)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename=filename+ '.mp3')


    # Local Audio transcription ------------------------------------------
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe(filename + '.mp3', fp16=False, language="en")
    transcription_text = result['text']
    print(transcription_text)

    f = open(filename  + '.txt', "w")
    f.write(transcription_text)
    f.close()


    # # Generate audio from text ------------------------------------------
    # from gtts import gTTS

    # myobj = gTTS(text=transcription_text, lang='en', tld='co.uk', slow=False)
    # myobj.save("output/converted.mp3")
