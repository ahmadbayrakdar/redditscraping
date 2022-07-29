from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import praw
import pickle

linktext = ""
comments = []

def runapplication():
    global link
    global linktext
    linktext = link.get()
    print(linktext)

    reddit = praw.Reddit(
        client_id="SodeENmMV1K6OPTwgwyN-Q",
        client_secret="9ycoQMI-eJLObD4PJTAvdeIfzZz2nw",
        password="scraping threads",
        user_agent="scrapingthreads by u/scrapingthreads",
        username="scrapingthreads",
    )

    print(reddit.user.me())

    # subtext = linktext.split("/", 5)
    # sub = subtext[4]
    # subreddit =  reddit.subreddit(sub)
    # subreddit.subscribe()

    submission = reddit.submission(url = linktext)
    for top_level_comment in submission.comments:
        comments.append(top_level_comment.body)

    pickle.dump(comments, open("comments.dat", "wb"))

    


redditpost = ""
gotimage = False
firstmsg = False

root = Tk()
root.title("reddit post")
root.resizable(False, False)
root.geometry('300x300')

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

frm = ttk.Frame(root, padding = 30)
frm.grid()
ttk.Frame(frm, relief='flat', borderwidth=4)

label0 = ttk.Label(frm, text = "Enter Reddit Post Link")
space0 = ttk.Label(frm, text = " ")
space1 = ttk.Label(frm, text = " ")
link = ttk.Entry(frm, width = 25)

space2 = ttk.Label(frm, text = " ")

btn_run = ttk.Button(frm, text='run', command = runapplication)

btn_quit = ttk.Button(frm, text = "quit", command = root.destroy)
label4 = ttk.Label(frm, text = "application made by ahmad bayrakdar")
label5 = ttk.Label(frm, text = "github.com/ahmadbayrakdar")
label6 = ttk.Label(frm, text = "00201552653686")
label7 = ttk.Label(frm, text = "copyright © 2022 all rights reserved", font=("Arial", 7))

label0.grid(column = 0, row = 0)
space0.grid(column = 0, row = 1)
space1.grid(column = 0, row = 3)
link.grid(columnspan = 4, row = 2)
space2.grid(column = 0, row = 5)
btn_run.grid(column = 0, row = 8)
btn_quit.grid(column = 1, row = 8)
label4.grid(columnspan = 3, row = 11)
label5.grid(columnspan = 3, row = 12)
label6.grid(columnspan = 3, row = 13)
label7.grid(columnspan = 3, row = 14)

link.insert(0, "https://www.reddit.com/r/ProgrammerHumor/comments/w1upl0/c_talking_to_python/?utm_source=share&utm_medium=web2x&context=3")


root.mainloop()



