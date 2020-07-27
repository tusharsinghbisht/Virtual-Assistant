import pygame
import os
import pyttsx3
engine= pyttsx3.init()
from tkinter import *
from tkinter.filedialog import askdirectory

pygame.init()

def speak(audio,rate=130):
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

root = Tk()
root.title("Music Player")
root.minsize(500,500)
root.maxsize(500,500)

listofsongs = []
names = []
v = StringVar()
songlabel = Label(root,textvariable=v,width=35).place(x=125,y=400)



nameofsonglbl = StringVar()
songName = Label(root,textvariable=nameofsonglbl,width=35).place(x=125,y=380)
nameofsonglbl.set('Song Name:')

index = 0
SONG_END = pygame.USEREVENT + 1
def openDir():
    # directory = 'C:\\DownloadsOfFriday'
    directory = askdirectory()

    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith('.wav'):
            listofsongs.append(files)
            names.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(SONG_END)
    v.set(listofsongs[0])


openDir()

def onselectsong(event):
    global index
    cs=  listSongs.curselection()
    # w.config(text=listSongs.get(cs))
    for allsongslist in cs:
        index = allsongslist
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        # print(pygame.mixer.music.get_pos())
        updatelabel()

#listofsongname = StringVar()
#listofsonginfolder = Label(root,textvariable=listofsongname,width=50).place(x=125,y=300)
#for index in listofsongs:
#    index +=1
#    listofsongname.set(f"""
#    All Lists
#    {listofsongs[index]}
#    """)
#x=125
#y=300
#for index in listofsongs:
#    x+=5
#    y+=5
#    listofsongname = StringVar()
#    listofsonginfolder = Label(root,textvariable=listofsongname,width=50).place(x=x,y=y)
#    listofsongname.set(f"""
#    All Lists
#    {index}
#    """)
    
    #print(index)
#ScollBar
# scrollbar = Scrollbar(root)#.place(relx = 0.5, rely = 0.5, anchor="n")
# scrollbar.place(relx = 0.5, rely = 0.5, relheight=0.2#, anchor="nw")


listSongs = Listbox(root, width=30,height=5)
listLabel = Label(root,text="List Of Songs", width=35).place(x=125,y=225)
songno = 0
for songs in listofsongs:
    songno +=1
    listSongs.insert(songno,songs)
listSongs.place(relx = 0.5, rely = 0.5, anchor="n")
listSongs.bind('<<ListboxSelect>>',onselectsong)
# listSongs.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listSongs.yview)

def updatelabel():
    global index
    global songname
    v.set(names[index])
    # print(names[index])


def nextSong(event):
    global index
    try:
        index +=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()
    except:
        # speak("Sir, There's no more song")
        # index -= 1
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()

def prevsong(event):
    global index
    try:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()
    except:
        # speak("Sir, There's no more song")
        # index +=1
        index = -1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(SONG_END)
        updatelabel()
        


def pause_song(event):
    pygame.mixer.music.pause()
    v.set('')

def unpause_song(event):
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_endevent(SONG_END)
    updatelabel()


def restart(event):
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(SONG_END)
    updatelabel()

def set_Vol(vol):
    volume = int(vol)/100
    pygame.mixer.music.set_volume(volume)


def check_end():
    global index
    for event in pygame.event.get():
        if event.type == SONG_END:
            nextSong(index)

    root.after(100,check_end)

def LenCheck():
    global index
    scaleLen.set(pygame.mixer.music.get_pos()/1000)
    # print(pygame.mixer.music.get_pos()/1000)

    root.after(1000,LenCheck)

# while True:
#     check_end()

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

pausebutton = Button(root,text='Pause Music')
pausebutton.pack()

resume = Button(root,text='Resume Music')
resume.pack()


playsong = Button(root,text="Restart Song")#.place(x=100,y=100)
playsong.pack()

scaleVlum = Scale(root, from_= 0, to=100, orient=HORIZONTAL, command=set_Vol)
scaleVlum.set(100)
scaleVlum.pack()

scaleLen = Scale(root, from_= 0, to=pygame.mixer.Sound(listofsongs[index]).get_length(), orient=HORIZONTAL)#, command=set_len)
# scaleLem.set(100)
scaleLen.pack()


nextbutton.bind("<Button-1>",nextSong)
previousbutton.bind("<Button-1>",prevsong)
pausebutton.bind("<Button-1>",pause_song)
resume.bind("<Button-1>",unpause_song)
playsong.bind("<Button-1>",restart)
root.iconbitmap('D:\\FRIDAYv2\\icon\\FRIDAYicon.ico')

    # while True:
    #     print(pygame.mixer.music.get_pos())

# root.after(100,check_end)
# root.after(0,check_end())
check_end()
LenCheck()
# a = pygame.mixer.Sound("test.wav")
# print("length",a.get_length())
root.mainloop()
pygame.quit()

# import mutagen.wavpack import wave