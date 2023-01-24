import speech_recognition as sr
import pyttsx3
import transformers
import os
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    DANGER = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 

class ChatBot():
    def __init__(self):
        print("----- Warming up -----")

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Currently Listening...")
            recognizer.adjust_for_ambient_noise(mic,duration=1)
            audio = recognizer.listen(mic,timeout=15)
            text = "Error"
        try:
            text = recognizer.recognize_google(audio)
            print("Me -> " + text)
            return text
        except sr.RequestError as e:
            print("404 -> Could not request results; {0}".format(e))
            return text

        except sr.UnknownValueError:
            print("404 -> Unknown error occurred")
            return text

    def text_to_speech(self,text):
        print("AI -> ", text)
        speaker = pyttsx3.init()
        voice = speaker.getProperty('voices')
        speaker.setProperty('voice', voice[1].id)
        speaker.say(text)
        speaker.runAndWait()


if __name__ == "__main__":
    ai = ChatBot()
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while True:
        ai.text_to_speech("Do you want to chat or speak with me?")
        action = int(input("(1 to chat 2 to speak) \nMe-> "))
        if action == 1:
            inp = input("AI -> What do you want to call me?\nMe -> ")
            ai.set_name(name=inp)
            print("AI -> Great what's on your mind?")
            while True:
                inp = input("Me -> ")
                if any(i in inp for i in ["quit","exit","close","shut down","bye"]):
                    break
                elif any(i in inp for i in ["your name","who are you"]):
                    print("AI -> I'm " + ai.get_name())
                else:
                    chat = nlp(transformers.Conversation(inp), pad_token_id=50256)
                    res = str(chat)
                    res = res[res.find("bot >> ")+6:].strip()
                    print("AI -> " + res)
        elif action == 2:
            ai.text_to_speech("What do you want to call me?")
            while True:
                res = ai.speech_to_text()
                if res == "Error":
                    ai.text_to_speech("Sorry, come again?")
                else:
                    break
            ai.set_name(name=res)
            ai.text_to_speech("Great what's on your mind?")
            while True:
                res = ai.speech_to_text()
                if any(i in res for i in ["thank","thanks"]):
                    res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
                elif any(i in res for i in ["your name","who are you"]):
                    res = "I'm " + ai.get_name()
                    ai.text_to_speech(res)
                elif any(i in res for i in ["exit","close","quit","bye"]):
                    break
                else:   
                    if res=="Error":
                        res="Sorry, come again?"
                    else:
                        chat = nlp(transformers.Conversation(res), pad_token_id=50256)
                        res = str(chat)
                        res = res[res.find("bot >> ")+6:].strip()
                        ai.text_to_speech(res)
        res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
        ai.text_to_speech(res)
        break
            