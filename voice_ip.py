import speech_recognition as sr

def listen():
    recogniser=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listining")
        audio=recogniser.listen(source, phrase_time_limit=5)
    
    try:
        command=recogniser.recognize_google(audio)
        print(f"You said :{command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry! I could't understand you")
        return None
    except sr.RequestError:
        print("Recognition service failed, Please try again later")
        return None