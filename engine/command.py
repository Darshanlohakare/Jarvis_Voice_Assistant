import pyttsx3
import speech_recognition as sr
import eel
import time
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit 



def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    #print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(4)
        #speak(query)
        #eel.showHood()
        
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
       query = takecommand()
       print(query)
       eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        

        if "open" in query:
                from engine.features import openCommand
                openCommand(query)

        elif "hello jarvis" in query:
                speak("hello sir , i am Jarvis , How can i help you.")
        elif "hi jarvis" in query:
                speak("hello Mam ,i am jarvis , how can i help you.")
        elif "who are you" in query:
                speak("I am Jarvis , A Personal Voice Assistant")
        elif "how are you" in query:
                speak("i am fine , what about you ?")
        elif "i am also fine" in query:
                speak("ok , i am Happy to here...")

        # Date
        elif "current date" in query:
                now_time=datetime.datetime.now().strftime("%d:%m:%y")
                speak("Current date is" + str(now_time))
        #Time
        elif "current time" in query:
                now_time=datetime.datetime.now().strftime("%H:%M")
                speak("Current time is" + str(now_time))
        
        # Open Desktop Application
        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)


        #wikipedia
        elif "wikipedia" in query:
            import wikipedia
            query = query.replace("jarvis", "")
            query = query.replace("search wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)

        # Search in Google
        elif "search" in query:
                query =query.replace("jarvis", "")
                query =query.replace("search ", "")
                webbrowser.open("https://www.google.com/search?q="+query)

        # Task To Do List
        elif "new task" in query:
                    task = query.replace("new task", "")
                    task = task.strip()
                    if task !="":
                        speak("Adding Task :" + task)
                        with open("todo.txt", "a") as file:
                            file.write(task + "\n")
                
        # Speak Task
        elif "speak task" in query:
                    with open("todo.txt", "r") as file:
                         speak("Remainig task we have to do today is: "+ file.read())
                
        # To Do List Show
        elif "show work" in query:
                    with open("todo.txt", "r") as file:
                      tasks = file.read()
                    notification.notify(
                        title = "Today's Work",
                        message = tasks
                    )

        elif "on youtube":
                from engine.features import PlayYoutube
                PlayYoutube(query)

        # Send Message in Whatsapp
        elif "send whatsapp" in query:
            pywhatkit.sendwhatmsg("+919881226527", "Hi , How are You ?",7,7,30)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)



        else:
            # print("Not run")
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
                

    
    
    

    eel.showHood()
