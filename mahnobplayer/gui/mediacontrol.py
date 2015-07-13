'''
Created on 13 Jul 2015

@author: sfrullo
'''

import tkinter as tk
import tkinter.ttk as ttk
from os import listdir, path
from PIL import Image, ImageTk

from mahnobplayer.gui.basic import BasicFrame
    
class MediaControl(BasicFrame):
    ''' This class implements the standard media controller. It is a basic
    frame with a series of button which associated callback invoke 
    the main controller (sort of MVC) methods for media control '''
    
    
    def __init__(self, parent, controller,*args, **kwarg):
        '''
        Constructor
        '''
        BasicFrame.__init__(self, parent, *args, **kwarg)
        self.__controller = controller
        
        FILEDIR = path.split(__file__)[0]
        icons = {}
        for icon in listdir(path=path.join(FILEDIR,'etc')):
            name = icon.split('.')[0]
            image = Image.open(path.join(FILEDIR,'etc',icon))
            icons[name] = ImageTk.PhotoImage(image.resize((15, 15), Image.ANTIALIAS))
            
        
        self.buttoncontainer = BasicFrame(self, padx=5, pady=5)
        btopt = { 'width' : 20,
                  'height' : 20,
                  'relief' : 'groove'}
        for index, name in enumerate(['rew', 'stop', 'play', 'pause', 'ffw']):
            bt = tk.Button(self.buttoncontainer, btopt, image=icons[name], command=getattr(self, 'on_' + name))
            bt.image = icons[name]
            setattr(self, name + 'bt', bt)
            bt.grid(column = index, row=0)
        self.buttoncontainer.grid(column = 0, row=1, sticky='w')
            
        
        self.progresbarconainer = BasicFrame(self, padx=5)
        self.progresbarconainer.grid(column=0,row=0, sticky='ew')
        self.progressvar = tk.DoubleVar()
        self.progressvar.set(.0)
        self.progressbar = ttk.Scale(self.progresbarconainer, 
                                          length = 300,
                                          #mode='determinate', 
                                          orient = tk.HORIZONTAL, 
                                          variable = self.progressvar, 
                                          to = 1.0)
        self.progressbar.grid(column = 0, columnspan=6, row=1, sticky = 'ew')
    
    #---------------------------------------------------------------------------
    # Callbacks
    # It calls the controller method which is responsible to update media status
    #---------------------------------------------------------------------------
    def on_rew(self):
        self.__controller.on_rew(self)
    
    def on_stop(self):
        self.__controller.on_stop(self)
    
    def on_play(self):
        self.__controller.on_play(self)
    
    def on_pause(self):
        self.__controller.on_pause(self)
    
    def on_ffw(self):
        self.__controller.on_ffw(self)
    
    def update_progressbar(self, value):
        # value must be in percent: 0 = start position, 1 = full
        self.progressvar.set(value)

    def dummy(self):
        pass


if __name__ == '__main__':
    
    root = tk.Tk()
    
    m = MediaControl(root, None)
    m.update_progressbar(.65)
    root.mainloop()