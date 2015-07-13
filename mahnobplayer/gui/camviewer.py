'''
Created on 10 Jul 2015

@author: sfrullo
'''

import tkinter as tk
from tkinter.filedialog import askopenfilenames

from mahnobplayer.gui import basic
from mahnobplayer.gui import videoframe
from mahnobplayer.gui import mediacontrol

class CamViewer(basic.BasicWindow):
    ''' CamViewer class implements the CamViewer GUI.
        This viewer implements six frames which could be used to show different
        videos at the same time with the chance of switch between them.
    '''

    
    def __init__(self, parent, controller, *args, **kwargs):
        ''' Init Function for the CamViewer class '''
        basic.BasicWindow.__init__(self, parent, *args, **kwargs)
        self.grid()
        
        self.__controller = controller
        
        self.createMenu()
        
        self.medialist = [(),(),()]
        
        self.videoframecontainer = basic.BasicFrame(self)
        self.frames = dict(zip(range(6), [videoframe.selectableVideoFrame(self.videoframecontainer, self.medialist) for c in range(6)]))
        index = [(0,0),(1,0),(2,0),
                 (0,1),(1,1),(2,1)]
        #configure column/row to get resizeble frames
        for c,r in index:
            self.rowconfigure(r, minsize=0, weight=1)
            self.columnconfigure(c, minsize=0, weight=1)

        color = ['white', 'red', 'green', 'blue', 'cyan', 'yellow']
        for i, f in self.frames.items():
            f.config(bg=color[i], padx=3, pady=3)
            f.rowconfigure(0, weight=1)
            f.columnconfigure(0, weight=1)
            f.setVideoFrameHeight(200)
            f.setVideoFrameWidth(200)
            f.grid(column=index[i][0], row=index[i][1])
        print(self.frames)
        
        self.videoframecontainer.grid(column=0,row=0, sticky='nesw')
        
        
        self.mediacontrollecontainer = basic.BasicFrame(self)
        self.mediacontroller = mediacontrol.MediaControl(self.mediacontrollecontainer, self.__controller)
        self.mediacontrollecontainer.grid(column=0,row=1, sticky='nesw')
        
    
    def createMenu(self):
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
    
    app = CamViewer(tk.Tk(), None)

    app.mainloop()