import speech_recognition

rec = speech_recognition.Recognizer()
while True:
  with speech_recognition.Microphone() as mic:
    print('say somthing ...')
    audio = rec.listen(mic)
  mic_audio = rec.recognize_google(audio) # write text from mic
  print(mic_audio)
  text = rec.recognize_google(audio)
  if 'hello' in text:
    print('Hello OSAMA')