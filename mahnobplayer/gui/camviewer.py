'''
Created on 10 Jul 2015

@author: sfrullo
'''

import tkinter as tk
from tkinter.filedialog import askopenfilenames

from mahnobplayer.gui import basic
from mahnobplayer.gui import videoframe

class CamViewer(basic.BasicWindow):
    ''' CamViewer class implements the CamViewer GUI.
        This viewer implements six frames which could be used to show different
        videos at the same time with the chance of switch between them.
    '''


    def __init__(self, parent, *args, **kwargs):
        ''' Init Function for the CamViewer class '''
        basic.BasicWindow.__init__(self, parent, *args, **kwargs)
        self.grid()

        menudata = (
            [
                "_File", (
                    ("_New", "Control-n", self.dummy),
                    ("_Add Video", "Control-o", self.on_add_video),
                    (), # Add a separator here
                    ("_Exit","Alt-F4", self.on_quit),
                ),
            ],
            [
                "_Edit", (
                    ("_Undo", "Control-z", self.dummy),
                    ("_Find", "F3", self.dummy),
                    ("F_ooBar", "Control-Shift-A", self.dummy),
                    ("Foo_Bar2","Alt-s", self.dummy),
                ),
            ],
            [
                "_Help", (
                    ("_Help", "F1", self.dummy),
                    (), # Add a separator here
                    ("_About", "", self.dummy),
                )
            ],
        )
        
        menu = basic.BasicMenu(self)
        menu.addSubMenu(menudata)
        self.setMenu(menu)
        
        
        self.medialist = [(),(),()]
        
        
        self.frames = dict(zip(range(6), [videoframe.selectableVideoFrame(self, self.medialist) for c in range(6)]))
        index = [(0,0),(1,0),(2,0),
                 (0,1),(1,1),(2,1)]
        #configure column/row to get resizeble frames
        for c,r in index:
            self.rowconfigure(r, minsize=0, weight=1)
            self.columnconfigure(c, minsize=0, weight=1)

        color = ['white', 'red', 'green', 'blue', 'cyan', 'yellow']
        for i, f in self.frames.items():
            f.config(bg=color[i], padx=30, pady=30)
            f.rowconfigure(0, weight=1)
            f.columnconfigure(0, weight=1)
            f.setVideoFrameHeight(200)
            f.setVideoFrameWidth(200)
            f.grid(column=index[i][0], row=index[i][1])
        print(self.frames)
        
    #-----------------------------------------------------------------------
    # Callbacks
    #-----------------------------------------------------------------------
    def on_quit(self):
        self.quit()


    def on_add_video(self):
        fileSelected = askopenfilenames()

    def dummy(self):
        pass


if __name__ == '__main__':
    
    app = CamViewer(tk.Tk())

    app.mainloop()