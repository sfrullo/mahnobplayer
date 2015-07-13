'''
Created on 11 Jul 2015

@author: sfrullo
'''


import tkinter as tk
from os import path

from mahnobplayer.gui.basic import BasicFrame
    
class VideoFrame(BasicFrame):
    
    def __init__(self, parent, *args, **kwarg):
        BasicFrame.__init__(self, parent, *args, **kwarg)
        
    def getXid(self):
        return self.winfo_id()


class selectableVideoFrame(BasicFrame):
    
    def __init__(self, parent, medialist, *args, **kwarg):
        BasicFrame.__init__(self, parent, *args, **kwarg)
        self.__medialist = medialist if len(medialist) > 0 else ['---']
        
        self.__videoframe = VideoFrame(self, bg='white', padx=0, pady=0)
        self.__videoframe.grid(column=0,row=0, sticky='nesw')
        
        self.selectionvar = tk.StringVar()
        self.selectionvar.set(self.__medialist[0])
        self.__selectionlist = tk.OptionMenu(self, self.selectionvar, *self.__medialist, command=lambda x:self.on_select(x))
        self.__selectionlist.config(relief=tk.GROOVE)
        self.__selectionlist.grid(column=0,row=1, sticky='ew')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def getCurrentSelection(self):
        return self.__selection.get()
    
    def setVideoFrameWidth(self, width):
        self.__videoframe.setWidth(width)

    def getVideoFrameWidth(self):
        return self.__videoframe.getWidth()
    
    def setVideoFrameHeight(self, heigth):
        self.__videoframe.setHeight(heigth)

    def getVideoFrameHeight(self):
        return self.__videoframe.getHeight()
    
    def getXid(self):
        return self.__videoframe.getXid()
    
    def updateMediaList(self, medialist):
        self.__medialist = medialist
        menu = self.__selectionlist.children['menu']
        menu.delete(1, 'end')
        for value in medialist:
            menu.add_command(label=path.basename(value), command=lambda v=value: self.selectionvar.set(v) )
            
    #---------------------------------------------------------------------------
    # Callbacks
    #---------------------------------------------------------------------------
    
    def on_select(self):
        print(self.selectionvar.get(), 'video selected')
    
if __name__ == '__main__':
    
    root = tk.Tk()
    
    f = selectableVideoFrame(root, ['1','2','3'])
    f.setVideoFrameWidth(200)
    f.setVideoFrameHeight(200)
    
    
    root.mainloop()