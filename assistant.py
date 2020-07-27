'''
Virtual Assistant Module
========================
  >>> __version__  = 2.0.0

This is a virtual assistant module containing a `Assistant` class for making 
Virtual assistant such as Tony Stark's Jarvis or Friday

Usage
------
  >>> from assistant import *

  >>> if __name__ == '__main__':
  >>>    jarvis = Assistant('your_assistant_name', voice_speed, voice(either 0 or 1), '_version_', 'your_name', 'your_gender', 'absolute_path_to_your_any_image')
  >>>    jarvis.main_loop()

@author - `Tushar Bisht`
------------------------
@contact - aabisht2006@gmail.com
--------------------------------
'''

__version__ = "2.0.0"

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import datetime
import platform
import speech_recognition as sr
import sys
import os
import string
import math
import random
import webbrowser
import smtplib
import time
import cv2
import numpy as np
import face_recognition
import wikipedia
import wolframalpha
import win10toast
import pymongo
import requests
import json

engine = pyttsx3.init('sapi5')

weather_key = "b1abc297c8af9f3533cdaf1114ac30bf"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

toaster = win10toast.ToastNotifier()

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['python']
collection = db['workList']

wolframalpha_client = wolframalpha.Client('V7EJTH-34K2J7EGRU')

class Assistant:
    '''
    Assistant
    =========
    
    This class `Assistant` create a object of this.

    Arguments
    ---------

    It takes 7 basic Arguments:
      1. Assistant Name: str
      2. Voice speed: int
      3. Voice Type: int (0 for male or 1 for female)
      4. Version: str, Example: "2.0.0"
      5. Username: str
      6. User Gender: str (either `male` or `female`)
      7. Your face Image path: str

    Features
    --------
    The Features are listed below:
      1. It makes a virtual assistant like Iron man's Jarvis
      2. You cam make GUI'S also
      3. Works Best with tkinter
      4. Cool functions and features of a real looking assistant

    See More on www.github.com/1234ayushBisht/Assistant  

                                            - Thanks
    '''
    def __init__(self, name, speed, voice, version, user, gender, img):
        self.assistant_name = name
        self.assistant_speed = speed
        self.assistant_voice = voice
        self.assistant_version = version
        self.user = user
        self.user_gender = gender
        self.user_face = img
        self.operating_system = platform.system()
        self.node = platform.node()
        self.release = platform.release()
        self.version = platform.version()
        self.machine = platform.machine()
        self.processer = platform.processor()
        self.architecture = platform.architecture()

    def speak(self, audio):
        try: 
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[self.assistant_voice].id)
            engine.setProperty('rate', self.assistant_speed)
            engine.say(audio)
            engine.runAndWait()

        except Exception as e:
            print(e)

    def tell_user_gender(self):
        word = ''

        if(self.user_gender == "male"):
            word = 'Sir'
        elif(self.user_gender == "female"):
            word = 'Mam'
        else:
            word = f'{self.user}'
        return word

    def intro(self):
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            self.speak(f'Good Morning {self.tell_user_gender()}')
        elif hour >= 12 and hour < 18:
            self.speak(f'Good Afternoon {self.tell_user_gender()}')
        else:
            self.speak(f'Good Evening {self.tell_user_gender()}')

        word = self.tell_user_gender()
        intro_lines = [f'I am Your Virtual assistant {self.assistant_name}, What can I do for you', f'Welcome Back, I am Now Online', f'How are You {self.tell_user_gender()}? What can i do for you', f'Nice To see you again {self.tell_user_gender()}, What Do you want']
        self.speak(random.choice(intro_lines))

    def about(self):
        self.speak(f'I am A virtual assistant Jarvis Made By Sir Tushar')
        messagebox.showinfo(f'About {self.assistant_name}', f"{self.assistant_name}\nI am A virtual assistant Jarvis Made By Sir Tushar Singh Bisht for serving as a nice friend\n\nCurrent User: {self.user}")

    def computer(self):
        self.speak(f'Here Is Your Computer Info')
        messagebox.showinfo(f'Your Computer', f"Operating System: {self.operating_system}\nNode: {self.node}\nProcessor: {self.processer}\nArchitecture: {self.architecture}\nMachine: {self.machine}\nVersion: {self.version}\nRelease: {self.release}")

    def owner(self):
        self.speak(f'My Owner\'s Name is {self.user}')
        messagebox.showinfo('Owner Info', f"About Owner\nMy Owner's Name is {self.user}, you are my owner")

    def takeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # self.speak('Listening ...')
            print('Listening ...')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            # self.speak('Recognizing ...')
            print('Recognizing ...')
            query = r.recognize_google(audio, language='en-in')
        except sr.RequestError:
            return 'None'
        except sr.UnknownValueError:
            return 'None'
        
        return query   

    def recognize_me(self):
        cap = cv2.VideoCapture(0)

        user_image = face_recognition.load_image_file(self.user_face)
        user_face_encoding = face_recognition.face_encodings(user_image)[0]

        known_face_encodings = [user_face_encoding]
        known_face_names = [self.user]

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            ret, frame = cap.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]
            cv2.imshow(f'{self.assistant_name}', frame)
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unkown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        return True
                        break

                    face_names.append(name)

            process_this_frame = not process_this_frame

            if cv2.waitKey(25) & 0xFF == ord('q'):
                self.speak('Tking Exit')
                exit()
        
        cap.release()
        cv2.destroyAllWindows()

    def create_password(self, number):
        if number != 0:
            s1 = string.ascii_letters
            s2 = string.ascii_lowercase
            s3 = string.ascii_uppercase
            s4 = string.digits
            s4 = string.punctuation
            
            string_list = [s1,s2,s3,s4]

            word_list = []
            random_list = []
            password = ''
            
            for item in string_list:
                for char in item:
                    word_list.append(char)

            for char in word_list:
                randomValue = math.floor(random.random() * 100)
                random_list.append([randomValue, char])

            sorted_list = sorted(random_list)

            for item in sorted_list:
                password += item[1]

            return password[0:number]
            
        else:
            self.speak(f'Password can not take zero characters {self.tell_user_gender()}')

    def sure(self, app):
        self.speak(f'Did You want to open {app}')
        permission = self.takeCommand().lower()

        answer = None

        if 'yes' in permission:
            self.speak(f'Ok {self.tell_user_gender()}')
            answer = True
        elif 'no' in permission:
            self.speak(f'Ok {self.tell_user_gender()}')
            answer = False
        else:
            self.speak('I did\'nt get that {self.tell_user_gender()}') 

        return answer

    def vscode(self):
        if self.sure('vscode'):
            self.speak('Opening VS Code')
            path = r"C:\Users\Ayush\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)

    def powershell(self):
        if self.sure('powershell'):
            self.speak('Opening Powershell')
            path = r"C:\Users\Ayush\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Windows PowerShell.lnk"
            os.startfile(path)

    def chrome(self):
        if self.sure('chrome'):
            self.speak('Opening Chrome')
            path = r"C:\Users\Ayush\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(path)

    def camera(self):
        if self.sure('camera'):
            self.speak('Opening Camera')
            path = r"C:\Users\Ayush\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Camera.lnk"
            os.startfile(path)

    def google(self):
        if self.sure('google'):
            self.speak('Opening Google')
            webbrowser.open('www.google.com')

    def gmail(self):
        if self.sure('gmail'):
            self.speak('Opening Gmail')
            webbrowser.open('www.gmail.com')

    def youtube(self):
        if self.sure('youtube'):
            self.speak('Opening Youtube')
            webbrowser.open('www.youtube.com')

    def github(self):
        if self.sure('github'):
            self.speak('Opening Github')
            webbrowser.open('www.github.com')

    def whatsup(self):
        if self.sure('whatsup'):
            self.speak('Opening Whatapp')
            webbrowser.open('web.whatsapp.com')

    def send_mail(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('aabisht2006@gmail.com', '1234ayush')
            self.speak(f'{self.tell_user_gender()} Please Speak Subject')
            sub = self.takeCommand()
            self.speak(f'{self.tell_user_gender()} Please Speak Message')
            msg = self.takeCommand()
            self.speak(f'Whom to send {self.tell_user_gender()}')
            recivers_list = [['self', 'aabisht2006@gmail.com'], ['mom', 'rosy.bisht80@gmail.com'], ['brother', 'tushar.bisht2006@gmail.com'], ['dad', 'tushar.4972@kvsrodelhi.in']]         
            reciver_email = None
            reciver_command= self.takeCommand().lower()
            
            for reciver in recivers_list:
                if reciver[0] in reciver_command:
                    reciver_email = reciver[1]
                    server.sendmail('aabisht2006@gmail.com', reciver_email, f'Subject: {sub}\n\n{msg}')
                    self.speak(f'Your Message sent successfully {self.tell_user_gender()}')
                    server.close()
                    break
                else:
                    self.speak(f'Sorry {self.tell_user_gender()}, I couldn\'t find the email address. ')
                    break
        except Exception as e:
            #print(e)
            self.speak(f'Sorry , {self.tell_user_gender()} I am unable to send email')

    def tell_time(self):
        curr_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.speak(f'{self.tell_user_gender()} the time now is {curr_time}')
        messagebox.showinfo('Time Now', f'Time:\n{time.asctime(time.localtime())}')

    def take_exit(self):
        random_lines = [f'Bye {self.tell_user_gender()} I am taking exit', f'Good Bye {self.tell_user_gender()}', f'Bye {self.tell_user_gender()} See you next time', f'Taking Exit {self.tell_user_gender()}', f'{self.tell_user_gender()} I am taking exit']
        one_line = random.choice(random_lines)
        self.speak(one_line)
        sys.exit()

    def search(self, query):
        self.speak(f'Seraching for results {self.tell_user_gender()}...')
        try:
            try:
                res = wolframalpha_client.query(query)
                results = next(res.results).text
                self.speak(results)
            except:
                results = wikipedia.summary(query, sentences=3)
                self.speak(results)
                webbrowser.open(f'www.google.com/search?q={query}')
        except:
            webbrowser.open(f'www.google.com/search?q={query}')

    def music(self):
        self.speak('What Should I play sir')
        music_name = self.takeCommand()
        self.speak(f'Seraching on youtube {self.tell_user_gender()}...')
        if 'favourite' in music_name:
            musicList = ['www.youtube.com/watch?v=kJQP7kiw5Fk', 'www.youtube.com/watch?v=RKioDWlajvo', 'www.youtube.com/watch?v=JkYJmXYreeA', 'www.youtube.com/watch?v=F_mhWxOjxp4', 'www.youtube.com/watch?v=eQxmhqaR2OA']
            webbrowser.open(random.choice(musicList))
        else:
            webbrowser.open(f'www.youtube.com/results?search_query={music_name}')

    def weather(self):
        city = "Delhi, India"
        complete_url = f'{base_url}appid={weather_key}&q={city}'

        res = requests.get(complete_url)
        x = res.json()

        if x["cod"] != "404":
            y = x['main']

            temperature = y["temp"] 
  
            pressure = y["pressure"] 
        
            humidity = y["humidity"] 

            z = x["weather"] 
            desc = z[0]['description']
            temp = math.floor(temperature-273)
            weather_list = [f'{self.tell_user_gender()} todays temprature is {temp} degree celcius, Its a {desc} day and humidity is {humidity}% and pressure is {pressure}', f'{self.tell_user_gender()} the humidity now is {humidity}% temperature is {temp} degree celcius', ]
            self.speak(random.choice(weather_list))
        else:
            self.speak('City Not found.')

    def show_work_list(self):
        try:
            self.speak(f'Showing work list {self.tell_user_gender()}')
            x = collection.find()
            items = []
            for i in x:
                items.append(i)
            mylist = Tk()
            mylist.title('Work List')
            mylist.geometry('400x400')
            mylist.minsize(400, 400)
            mylist.maxsize(400, 400)

            Label(mylist, text="Your Work List", fg="black", bg="white", relief=SUNKEN, font="verdana 18 bold").pack(fill=X)
            
            if len(items) != 0:
                self.speak(f'{self.tell_user_gender()} You have {len(items)} items in your list')
                i = 0

                for item in items:
                    i+=1
                    Label(text=f"\n{i}. {item['work'].upper()}  -> {item['time']}", fg="white", bg="black", font="verdana 10").pack()
                
                # scroll = Scrollbar(mylist)
                # scroll.pack(fill=Y, side=RIGHT)
                mylist.config(bg="Black")
            else:
                self.speak(f'{self.tell_user_gender()} You have {len(items)} items in your list, so i can not show anything')
                mylist.destroy()

            mylist.mainloop()
        except:
            self.speak(f'{self.tell_user_gender()} Please Start Mongo DB.. I am Unable to connect')
    
    def update_work_list(self):
        try:
            self.speak(f'Should I add or remove something {self.tell_user_gender()}')
            command = self.takeCommand()

            if 'add' in command or 'insert' in command:
                self.speak(f'What Should I add {self.tell_user_gender()}')
                item = self.takeCommand()
                collection.insert_one({'time': time.asctime(time.localtime()), 'work': item})
                self.speak(f'{item} added to list successfully {self.tell_user_gender()}')
            
            elif 'remove' in command or 'delete' in command:
                self.speak(f'What Should I remove {self.tell_user_gender()}')
                item = self.takeCommand()
                work = collection.find_one({'work': item})
                if work:
                    collection.delete_one({'work': item})
                    self.speak(f'{item} removed from list successfully {self.tell_user_gender()}')
                else:
                    self.speak(f'{item} is not in list {self.tell_user_gender()}')

            else:
                self.speak(f'I could not understand {self.tell_user_gender()}')

        except:
            self.speak(f'{self.tell_user_gender()} Please Start Mongo DB.. I am Unable to connect')
    
    def main_win(self):
        def start():
            btn.destroy()
            self.intro()
            curr_time = datetime.datetime.now().strftime('%H:%M:%S')

            while True:
                if curr_time == '21:00:00':
                    self.speak(random.choice([f'It\'s your sleeping time {self.tell_user_gender()}, go to bed', f'Its night {self.tell_user_gender()} sleeping time', f'I think you should go for sleep {self.tell_user_gender()}']))
                elif curr_time == '06:00:00':
                    self.speak(random.choice([f'Wake up {self.tell_user_gender} sun is rising', f'Its morning {self.tell_user_gender} wakeup', f'Time now is 8 A.M {self.tell_user_gender} wakeup']))
                
                query = self.takeCommand()
                query = query.lower()

                if 'hello' in query or 'hi' in query:
                    self.speak(f'Hi, {self.tell_user_gender()} how are you')

                elif 'who is ironman' in query:
                    self.speak(f'You are Iron man {self.tell_user_gender()}')
                elif 'how are you' in query:
                    self.speak(f'I am {self.tell_user_gender()}')
                elif 'i am fine' in query:
                    self.speak(f'I am also fine {self.tell_user_gender()}')
                elif 'what should I do' in query:
                    self.speak(f'Tell me {self.tell_user_gender()}, I can do everything for you')
                elif 'are you online' in query or 'wakeup' in query or 'help me' in query:
                    self.speak(f'Always {self.tell_user_gender()} everytime for you')
                elif 'who are you' in query:
                    self.about()
                
                elif 'who is me' in query or 'who I' in query or 'about me' in query:
                    self.owner()

                elif 'my computer' in query or 'about computer' in query or 'about my computer' in query:
                    self.computer()

                elif 'exit' in query or 'abort' in query or 'sleep' in query or 'get out' in query:
                    self.take_exit()

                elif 'music' in query or 'play something' in query:
                    self.music()

                elif 'send mail' in query or 'send email' in query or 'send a email' in query:
                    self.send_mail()

                elif 'time' in query:
                    self.tell_time()
                
                elif 'weather' in query:
                    self.weather()

                elif 'vscode' in query or 'code' in query or 'visual studio code' in query:
                    self.vscode()

                elif 'camera' in query:
                    self.camera()

                elif 'chrome' in query:
                    self.chrome()

                elif 'google' in query:
                    self.google()

                elif 'whatsup' in query:
                    self.whatsup()

                elif 'gmail' in query:
                    self.gmail()

                elif 'powershell' in query:
                    self.powershell()

                elif 'youtube' in query:
                    self.youtube()

                elif 'github' in query:
                    self.github()

                elif 'work list' in query or 'my list' in query:
                    self.show_work_list() 

                elif 'update list' in query or 'remove item' in query or 'add item' in query or 'update worklist' in query:
                    self.update_work_list()

                elif 'password' in query:
                    self.speak(f'Should I make a password {self.tell_user_gender()}')
                    permission = self.takeCommand().lower()

                    if 'yes' in permission:
                        new_password = self.create_password()
                        messagebox.showinfo(f'{self.assistant_name}-{self.assistant_version}', f'Your Password: \n{new_password}')
                    elif 'no' in permission:
                        self.speak(f'All Ok {self.tell_user_gender()}')
                    else:
                        self.speak(f'I couldn\'t understand {self.tell_user_gender()}')
                
                elif query == 'none':
                    self.speak(f'{self.tell_user_gender()} I am Unable to get commnad, please say that again')

                else:
                    self.search(query)

        root = Tk()
        root.title(f'{self.assistant_name}(Virtal Assistant) - {self.user}')
        root.geometry('600x600')
        root.minsize(600, 600)
        root.maxsize(600, 600)

        btn =  Button(text='START', command=start, bg="black", fg="white", font="comicsans 12", padx=17, pady=5)
        btn.pack()
        bg = PhotoImage(file='img/JarvisBot.gif')
        Label(image=bg).pack(fill=X) 
        root.config(bg='white')
        root.mainloop()

    def main_loop(self):
        toaster.show_toast(f'{self.assistant_name}-{self.assistant_version}', f'{self.user} your {self.assistant_name} is working properly.\n\nPlease Recognize your face', duration=10)
        self.speak(f'Starting Recognizing face {self.tell_user_gender()}. Please show your face')
        self.recognize_me()
        toaster.show_toast(f'{self.assistant_name}-{self.assistant_version}', f'Your Recognization is complete now.\nPress Start for Launch')     
        self.speak(f'You are recognized {self.tell_user_gender()}. Do whatever you want')

        def main():
            root.destroy()
            self.main_win()

        root = Tk()

        root.geometry('1300x680')
        root.minsize(510,480)
        root.title(f'{self.assistant_name}(Virtal Assistant) - {self.user}')

        main_menu = Menu(root)

        m1 = Menu(main_menu)
        m1.add_command(label='VSCode', command=self.vscode)
        m1.add_command(label='Google', command=self.google)
        m1.add_command(label='Youtube', command=self.youtube)
        m1.add_command(label='Gmail', command=self.gmail)
        m1.add_command(label='WhatsApp', command=self.whatsup)
        m1.add_command(label='Github', command=self.github)
        m1.add_command(label='Camera', command=self.camera)
        m1.add_command(label='Powershell', command=self.powershell)
        main_menu.add_cascade(label='Open', menu=m1)

        main_menu.add_command(label='Time', command=self.tell_time)
        main_menu.add_command(label='Mail', command=self.create_password)

        m2 = Menu(main_menu)
        m2.add_command(label='About', command=self.about)
        m2.add_command(label='Computer', command=self.computer)
        m2.add_command(label='Owner', command=self.owner)
        main_menu.add_cascade(label='More', menu=m2)

        main_menu.add_command(label='Quit', command=self.take_exit)

        root.config(menu=main_menu, bg='gray')   

        status_bar = Label(root, text="Virtual Assistant System - By Tushar Singh Bisht", anchor='w', relief=SUNKEN, fg='white', bg='black', pady=3, padx=3)
        status_bar.pack(fill=X, side=BOTTOM)
        
        menu_bar = Label(root, text=f"{self.assistant_name}", bg="black", fg="white", relief=SUNKEN, padx=13, pady=12, width=15, font="Verdana 17 underline")
        menu_bar.pack(side=LEFT, fill=Y)

        msg_bar = Button(root, command=main, text=f"START YOUR {self.assistant_name}", font="comicsans 13")
        msg_bar.pack(side=TOP, fill=X)

        bg_img = Image.open('./img/bg.jpg')
        bg_new_img = ImageTk.PhotoImage(bg_img)
        label1 = Label(image=bg_new_img)
        label1.pack(fill=BOTH)

        root.mainloop()

'''
******************************************************************* - Code Ends Here - ********************************************************
'''
