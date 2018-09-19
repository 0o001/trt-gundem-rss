import feedparser
import unidecode
from tkinter import *
import webbrowser


openTk = Tk()
openTk.title("TRT Haber - Gündem")
openTk.resizable(False, True)
openTk.geometry("550x500")

def RSS():
    global frame;
    frame = Frame(openTk)
    rss = feedparser.parse('http://www.trt.net.tr/rss/gundem.rss')
    index = 0
    
    for read in rss['entries']:
        title = Label(frame, text = unidecode.unidecode(read['title']), fg = "black", font = ("Arial", 16))
        title.pack()
        
        link = Button(frame, text = "Habere Git", cursor = "hand2", command = lambda clickIndex = index : GoLink(clickIndex))
        link.pack()
        
        frame.pack()
        index += 1

    def GoLink(clickIndex):
        webbrowser.open_new(unidecode.unidecode(rss['entries'][clickIndex]['link']))
         

def Refresh():
    frame.destroy()
    RSS()

refresh = Button(openTk, text = "Yenile", cursor = "hand2", font = ("", 11), fg = "green", command = Refresh)
refresh.pack()

RSS()
    
mainloop()
    
