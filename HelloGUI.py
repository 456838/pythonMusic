import Tkinter
# top = Tkinter.Tk()
# top.mainloop()

from Tkinter import *


def okClick(self):
    self.helloLabel.config(text = 'hello')


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.helloLabel = Label(self, text='Hello, world!')
        self.okButton = Button(self, text='ok', commond=okClick(self))
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel.pack()
        self.okButton.pack()
        self.quitButton.pack()


app = Application()
app.master.title('title')
app.mainloop()
