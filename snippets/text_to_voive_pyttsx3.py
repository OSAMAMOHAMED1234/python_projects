import pyttsx3
osama = pyttsx3.init()
osama.setProperty('rate', 150)
osama.setProperty('volume', 1.5)
osama.setProperty('voice', osama.getProperty('voices')[0].id) # 0 male, 1 female
osama.say('OSAMA')
osama.save_to_file('OSAMA', 'osama.mp3')
osama.runAndWait()