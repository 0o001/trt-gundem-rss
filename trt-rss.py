import feedparser
import unidecode
from tkinter import *
import webbrowser


openTk = Tk()
openTk.title("TRT Haber - Gündem")
openTk.resizable(False, True)
openTk.geometry("550x500")

frame = None;

def RSS():
    frame = Frame(openTk)
    rss = feedparser.parse('http://www.trt.net.tr/rss/gundem.rss')
    
    for read in rss['entries']:
        title = Label(frame, text = unidecode.unidecode(read['title']), fg = "black", font = ("Arial", 16))
        title.pack()
        
        link = Button(frame, text = "Habere Git", cursor = "hand2", command = lambda link = read['link'] : GoLink(link))
        link.pack()
        
        frame.pack()

    def GoLink(link):
        webbrowser.open_new(unidecode.unidecode(link))
         

def Refresh():
    frame.destroy()
    RSS()

refresh = Button(openTk, text = "Yenile", cursor = "hand2", font = ("", 11), fg = "green", command = Refresh)
refresh.pack()

RSS()
    
mainloop()
    
