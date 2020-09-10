from gtts import gTTS


def create_tts(text, filename):
    tts = gTTS(text=text)
    tts.save(filename.split(".")[0] + ".mp3")
    print('File saved successfully')


txt = input('Please enter some text: ')
fname = input("Please enter the file name: ")
create_tts(txt, fname)

