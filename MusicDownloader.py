import Tkinter as tk
import QQMusicSearchApi

window = tk.Tk()
window.geometry('500x300+500+200')
window.title('MusicDownload')


def searchAct():
    print("search act")
    enrtyKeyword = keywordEntry.get()
    hintLabel.config(text=enrtyKeyword)
    api = QQMusicSearchApi.keywordSearch(enrtyKeyword)
    # print api
    for item in api['data']:
        name = item['name']
        singer = item['singer']
        url = item['url']
        pic =item['pic']
        lrc=item['lrc']
        resultList.insert(tk.END, name+","+singer)
        # print(item)
    # hintLabel.config(text=api)


def downloadAct(downloadUrl):
    print downloadUrl


keywordLabel = tk.Label(window, text="keyword")
keywordEntry = tk.Entry(window, )
searchBtn = tk.Button(window, text="search", command=searchAct)
hintLabel = tk.Label(window, text='HINT')
resultList = tk.Listbox()
resultList.bind("<<ListboxSelect>>", downloadAct)
keywordLabel.pack()
keywordEntry.pack()
searchBtn.pack()
hintLabel.pack()
resultList.pack()
window.mainloop()
