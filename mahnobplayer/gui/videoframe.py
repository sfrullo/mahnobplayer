'''
Created on 11 Jul 2015

@author: sfrullo
'''


import tkinter as tk

from mahnobplayer.gui.basic import BasicFrame
    
class VideoFrame(BasicFrame):
    
    def __init__(self, parent, *args, **kwarg):
        BasicFrame.__init__(self, parent, *args, **kwarg)
        
    def getXid(self):
        return self.winfo_id()


class selectableVideoFrame(BasicFrame):
    
    def __init__(self, parent, playlist, *args, **kwarg):
        BasicFrame.__init__(self, parent, *args, **kwarg)
        self.__playlist = playlist
        
        self.__videoframe = VideoFrame(self, bg='white')
        self.__videoframe.grid(column=0,row=0, sticky='nesw')
        
        self.__selection = tk.StringVar()
        self.__selection.set(self.__playlist[0])
        b = tk.OptionMenu(self, self.__selection, *self.__playlist, command=self.on_select)
        b.config(relief=tk.GROOVE, bg='white', cursor=None)
        b.grid(column=0,row=1, sticky='nesw')
        
        self.grid()
        
        
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
    
    #---------------------------------------------------------------------------
    # Callbacks
    #---------------------------------------------------------------------------
    
    def on_select(self, value):
        print(value)
    
if __name__ == '__main__':
    
    root = tk.Tk()
    
    f = selectableVideoFrame(root, ['1','2','3'])
    f.setVideoFrameWidth(200)
    f.setVideoFrameHeight(200)
    
    
    root.mainloop()