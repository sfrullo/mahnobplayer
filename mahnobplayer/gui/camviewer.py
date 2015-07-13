'''
Created on 10 Jul 2015

@author: sfrullo
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilenames

from mahnobplayer.gui import basic
from mahnobplayer.gui import videoframe
from mahnobplayer.gui import mediacontrol
from logging import root
import random

class CamViewer(basic.BasicFrame):
    ''' CamViewer class implements the CamViewer GUI.
        This viewer implements six frames which could be used to show different
        videos at the same time with the chance of switch between them.
    '''

    
    def __init__(self, parent, controller, *args, **kwargs):
        ''' Init Function for the CamViewer class '''
        basic.BasicFrame.__init__(self, parent, *args, **kwargs)
        self.__controller = controller
        self.medialist = []
        
        self.createMenu()
        
        self.videoframecontainer = basic.BasicFrame(self)
        self.videoframecontainer.config(padx=10)
        self.frames = dict(zip(range(6), [videoframe.selectableVideoFrame(self.videoframecontainer, self.medialist) for c in range(6)]))
        index = [(0,0),(1,0),(2,0),
                 (0,1),(1,1),(2,1)]
        
        color = ['magenta', 'red', 'green', 'blue', 'cyan', 'yellow']
        for i, f in self.frames.items():
            f.config(padx=1, pady=1, bg='#555')
            f.setVideoFrameHeight(200)
            f.setVideoFrameWidth(200)
            f.grid(column=index[i][0], row=index[i][1])
            # set properties of each of the six column (and rows) to be stretchable
            self.videoframecontainer.columnconfigure(index[i][0], weight=1)
            self.videoframecontainer.rowconfigure(index[i][1], weight=1)
        # grid videoframecontainer to fit all space as possible over all direction
        self.videoframecontainer.grid(column=0,row=0, sticky='nesw')
        
        
        self.mediacontrollercontainer = basic.BasicFrame(self)
        self.mediacontrollercontainer.config(padx=10)
        self.mediacontroller = mediacontrol.MediaControl(self.mediacontrollercontainer, self.__controller)
        # grid mediacontrollercontainer to be on the bottom and 
        # fit all space as possible over left-right direction only
        self.mediacontrollercontainer.grid(column=0,row=2, ipady=5,sticky='sew')
        
    
    def createMenu(self):
        ''' Create the application menu bar '''
        
        menudata = (
            [
                "_File", (
                    ("_New", "Control-n", self.on_new),
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
        self.medialist.add(fileSelected)
        
    def on_new(self):
        pass
        
    def dummy(self):
        pass


if __name__ == '__main__':
    
    root = tk.Tk()

    app = CamViewer(root, None)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()