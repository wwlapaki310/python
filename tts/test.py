import speech_recognition as sr
import subprocess
import tempfile
import pyttsx3

# 音声合成
def TextToSpeech_pyttsx3(ph):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[18].id)
    engine.say(ph)
    engine.runAndWait()


# 音声入力
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("何かお話しして下さい。")
        audio = r.listen(source)

    try:
        # Google Web Speech APIで音声認識
#         text = r.recognize_google(audio, language="ja-JP")
        text = r.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        print("Google Web Speech APIは音声を認識できませんでした。")
    except sr.RequestError as e:
        print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
              " {0}".format(e))
    else:
        print(text)
        TextToSpeech_pyttsx3(text)
        print("--------------------")
        
    if text == "終わりだよ":
        break
print("完了。")


"""
text1="どーもーー！！！ミルクボーイ です。"
text2="こんなんなんぼあってもよいですからね。ははははは笑"
TextToSpeech_pyttsx3(text1)
TextToSpeech_pyttsx3(text2)
"""