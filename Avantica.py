import speech_recognition as sr

import pyttsx3,webbrowser,os,random,pyautogui,requests
import pywhatkit,sys,time
import datetime
import wikipedia
import bs4
import os
from subprocess import run,PIPE

from datetime import date
import subprocess
from cx_Freeze import Executable
listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


# run(sys.executable,["C:\\Users\\Datta Landge\\Desktop\\nnnn\\hello.py",input])




# music_dir=''
# os.startfile(os.path.join(music_dir))

def ampm():
    hour=int(datetime.datetime.now().hour)
    if hour==0 or hour<12:
        engine.say("good morning sir ")
        talk("Hi I am nakoshi and how can I help you")
        engine.runAndWait()
    elif hour==12 or hour<18:
        engine.say("good afternoon sir ")
        # engine.say('you have a nice day')
        talk("Hi I am syra and how can I help you")
        engine.runAndWait()
    elif hour>18 or hour<22:
        engine.say("good evening sir ")
        # engine.say('you have a nice day')
        talk("Hi I am syra and how can I help you")
        engine.runAndWait()
        
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():    
    try:
        with sr.Microphone() as source:
            print('Listning........')
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()                    
    except:
        talk("sorry sir due weak signal i not properly work ")
        return command
        play_command()

    return command
   
def play_command():
        query=take_command()
        if 'play song' in query:
            song=query.replace('play song',"")
            talk("playing"+song)
            pywhatkit.playonyt(song)
        elif "good afternoon" in query:
            talk("good afternoon sir")
            talk("sir you have nice day")
        elif "tell me date" in query:
            talk("ok sir wait")
            talk("sir")
            today=date.today()
            talk("sir today date is ")
            talk(today)
        elif 'tell me about day' in query:
            talk('just a wait ')
            talk('sir')
            talk('no sir no special this day')

        elif 'tell me time table' in query:
            talk("ok sir wait a second ")
            talk("sir")
            talk("from 9 am to 10 am ")
            talk("there is ")
            talk("web technology")
            talk("and")
            talk("design and anylys of algorithem")
            talk("lecture")
            talk("and from 11 am to 1 pm ")
            talk("there is")
            talk("system programing and operating system practical")
            talk("ok sir")
            talk("sir")
            talk("can i play music for you")
        elif 'play music' in query:
            talk("please wait a second sir i will play a song for you")
            music_dir='C:\\song'
            songs=os.listdir(music_dir)
            ran=random.choice(songs)
            os.startfile(os.path.join(music_dir,ran))
            talk("playing song sir")
            talk("you liked this song sir")
        elif 'python file' in query:
            talk("please wait a second sir")
           
            talk("playing song sir")
            talk("you liked this song sir")
        elif "switch on light" in query:
            talk(" please wait a second sir")
            pp=run([sys.executable,"C:\\Users\\Datta Landge\Desktop\Avantica\\alexa.py"],shell=False,stdout=PIPE)
            talk("done sir")
            print(pp)
            
            
        elif 'nice song'in query:
            talk("ok sir enjoy it ")
            talk("sir you have a new messages on whatsapp can you check it now")
        elif 'close music' in query:
            talk("ok i will close music sir")
            os.system("TASKKILL /F /IM wmplayer.exe")
            talk("ok done sir")
            talk("sir you have a new messages on whatsapp can you check it now")
               
        elif 'thank you for that' in query:
            talk("no mind sir ")
            talk("you welcome sir")
        elif 'close window' in query:
            talk('ok sir')
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            talk("you want more information sir")
        elif 'location' in query:
            talk("wait sir let me check where you are")
            try:
                ipadd=requests.get('https://api.ipify.org').text
                url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_request=requests.get(url)
                geo_data=geo_request.json()
                city=geo_data.get('city')
                state=geo_data.get('state')
                country=geo_data.get('country')
                talk(f'sir i am not sure but you are living in maharashtra  of {country}')
                talk("it's right sir")
            except:
                pass
        elif 'take screenshot'  in query:
            talk("sir please tell me filename this photo ")
            name=take_command().lower()
            talk("please wait sir i taking scrrenshot")
            img=pyautogui.screenshot()
            img.save(f'{name}.jpg')
            talk("well done i take screenshot successfully")

        elif 'can you change song' in query:
            talk("ok sir I will change song ok please wait a second sir")
            music_dir='C:\\song'
            songs=os.listdir(music_dir)
            rand_idx = random.randrange(len(songs)) 
            random_num = songs[rand_idx]
                # ch=random.choice(songs)
            os.startfile(os.path.join(music_dir,random_num))
            talk("i hope this song you liked it sir")
        elif 'open notepad' in query:
            talk("wait a second sir i will open your notepad")
            os.startfile('C:\\WINDOWS\\system32\\notepad.exe')
            talk("ok done sir")
            talk("sir you want write some note on notepad")
        elif 'close notepad' in query:
            talk("ok sir")
            talk("i close notepad")
            # os.startfile('C:\\WINDOWS\\system32\\notepad.exe')
            os.system("TASKKILL /F /IM notepad.exe")
            talk("ok sir")
            talk("i done")
        elif 'open whatsapp' in query:
            talk("wait a second sir i will open whatsapp")
            os.startfile('"C:\\Users\\Datta Landge\\AppData\\Local\\WhatsApp\\WhatsApp.exe"')
            talk("wait sir")
            talk("due to low network speed  your browser take some time  ")
         
            talk("done sir ")
            talk("sir you have new messages on email ")
            talk("you have to read it now ")
            talk("you want to close whatsapp sir")
        elif 'ok i will check' in query:
            talk("ok sir as you like")
            talk("sir today you have write note on python ")
            talk("can i help you to find you query sir")
        elif "no" in query:
            talk("no problem sir ")
        elif 'close whatsapp' in query:
            talk("of course  wait sir I close whatsapp")
            os.system("TASKKILL /F /IM whatsapp.exe")
            talk("done sir")
            talk("sir you want to check email")
            talk("can I open gmail sir ")
        elif 'show me mail' in query:
            talk("wait sir let me check your email ")
            talk("wait sir")
            talk("due to low network speed  your browser take some time  ")
            talk("so please wait a second till email open")
            
            webbrowser.open("www.gmail.com")
            talk("done sir ")
            talk("sir you have new email on email you need to check it ")
            
        
        elif 'close email' in query:
            talk("ok wait a second close email")
            os.system("TASKKILL /F /IM WinMail.exe")
            talk("done sir")
   
       
        elif 'find' in query:
            query=query.replace("find","")

            webbrowser.open(query)
            
        elif 'open google' in query:
            talk("please wait a second sir")
            talk("what you should search on google sir")
            cm=take_command().lower()
            webbrowser.open(cm)
            talk("according to google")
            about=wikipedia.summary(cm,2)
            talk(about)
            talk('sir you want screenshot it')

        elif 'tell me current time' in query:
            time=datetime.datetime.now().strftime('%I:%M:%p')
            talk(' Sir Current time is' + time)
            talk("and today temprature is 32 celcius")
            
        elif 'who is' in query:
            person=query.replace('who is',"")
            info=wikipedia.summary(person,2)
            talk('according to wikipedia')
            talk(info)
        elif 'say something about' in query:
            bio=query.replace('say something about',"")
            info=wikipedia.summary(bio,2)
            talk("according to google")
            talk(info)
        elif 'send message' in query:
            talk("which message you have to send it sir")
            message=take_command()
            pywhatkit.sendwhatmsg('+919359708049',f'{message}',21,00 )
            talk("ok done sir please wait a second ")
        elif 'you can sleep'in query:
            talk("I am going to sleep now you can call me anytime ok ")
            second=50
            time.sleep(second)
       
        elif 'are you single' in query:
            talk("ohh no I have already two boyfriends so I think  you must try another girl ")
            talk("but you and me always friends  ")

        elif 'you know my favourite dancer' in query:
            talk("of course sir I know your favourite is Sunny Leony")
            talk("you have must listen song laila mai laila can i play ")
        
        elif "good bye" in query:
            talk("good by sir see you again")
            talk('you can call me anytime sir ')
            talk("thank you for spend time with me bye")
            sys.exit()

        
        else:
            talk("please try again")
            
ampm()   
while True:
  
    play_command()
    
