'''
Created on 10 Jul 2015

@author: sfrullo
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilenames
from os import path

from mahnobplayer.gui import basic
from mahnobplayer.gui import videoframe
from mahnobplayer.gui import mediacontrol

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
        self.createVideoFrames(parent=self, medialist=self.medialist, nframes=6)
        self.createMediaController()
        
    def createVideoFrames(self, parent=None, medialist=(), nframes=0):
        videoframecontainer = basic.BasicFrame(parent)
        videoframecontainer.config(padx=10)
        self.frames = dict(zip(range(nframes), [videoframe.selectableVideoFrame(parent, medialist) for c in range(nframes)]))
        #index = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
        index = list(zip([x%3 for x in range(nframes)], [int(x/3) for x in range(nframes)]))
        for i, f in self.frames.items():
            f.config(padx=1, pady=1, bg='#555')
            f.setVideoFrameHeight(200)
            f.setVideoFrameWidth(200)
            # grid each videoframes and set "in_" property to put frames in videoframecontainer
            f.grid(column=index[i][0], row=index[i][1], in_=videoframecontainer)
            # set properties of each of the six column (and rows) to be stretchable
            videoframecontainer.columnconfigure(index[i][0], weight=1)
            videoframecontainer.rowconfigure(index[i][1], weight=1)
        # grid videoframecontainer to fit all space as possible over all direction
        videoframecontainer.grid(column=0, row=0, sticky='nesw')
        
    def createMediaController(self):
        mediacontrollercontainer = basic.BasicFrame(self)
        mediacontrollercontainer.config(padx=10)
        self.mediacontroller = mediacontrol.MediaControl(mediacontrollercontainer, self.__controller)
        # grid mediacontrollercontainer to be on the bottom and 
        # fit as much space as possible over left-right direction only
        mediacontrollercontainer.grid(column=0, row=2, ipady=5, sticky='sew')
        
    
    def createMenu(self):
        ''' Create the application menu bar '''
        
        menudata = (
            [
                "_File", (
                    ("_New", "Control-n", self.on_new),
                    ("_Add Video", "Control-o", self.on_add_video),
                    (),  # Add a separator here
                    ("_Exit", "Alt-F4", self.on_quit),
                ),
            ],
            [
                "_Help", (
                    ("_Help", "F1", self.dummy),
                    (),  # Add a separator here
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
        options = {}
        options['parent'] = self
        options['title'] = 'Add Video(s)'
        options['initialdir'] = path.split(__file__)[0]
        # options['initialdir'] = path.join(path.sep, __file__.split(path.sep)[0])
        options['filetypes'] = [('video files', '*.avi'), 
                                ('video files', '*.mpeg'),
                                ('all files', '.*')]
        options['multiple'] = True
        
        fileSelected = askopenfilenames(**options)
        
        print('fileselected:', fileSelected)
        self.medialist += fileSelected
        print(self.medialist)
        
        # if a file was selected than update gui media list
        if fileSelected != ():
            for f in self.frames.values():
                print('change media list for: ', f)
                f.updateMediaList(self.medialist)
                
            # and notify the changes to controller
            self.__controller.on_media_added(self, fileSelected)

    def on_selection(self, videoframe, selection):
        print(selection, ' selected for ', videoframe)
        # notify the controller about the selection
        self.__controller.on_selection(self, videoframe, selection)
        
    def on_new(self):
        newwind = basic.BasicWindow(self)
        # add hook for on_selection callbacks
        newwind.__dict__['on_selection'] = self.on_selection
        newframes = self.createVideoFrames(parent=newwind, medialist=self.medialist, nframes=6)
        
    def dummy(self):
        pass


if __name__ == '__main__':
    
    root = tk.Tk()

    app = CamViewer(root, None)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()
