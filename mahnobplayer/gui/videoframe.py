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
    
    def __init__(self, parent, medialist, *args, **kwarg):
        BasicFrame.__init__(self, parent, *args, **kwarg)
        self.__medialist = medialist if len(medialist) > 0 else ['empty']
        
        self.__videoframe = VideoFrame(self, bg='white', padx=0, pady=0)
        self.__videoframe.grid(column=0,row=0, sticky='nesw')
        
        self.__selectionvar = tk.StringVar()
        self.__selectionvar.set(self.__medialist[0])
        self.__selectionlist = tk.OptionMenu(self, self.__selectionvar, *self.__medialist, command=self.on_select)
        self.__selectionlist.config(height=0, relief=tk.GROOVE)
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
    
    #---------------------------------------------------------------------------
    # Callbacks
    #---------------------------------------------------------------------------
    
    def on_select(self, value):
        print(value, 'video selected')
        self.parent.on_video_selection(self, value)
    
if __name__ == '__main__':
    
    root = tk.Tk()
    
    f = selectableVideoFrame(root, ['1','2','3'])
    f.setVideoFrameWidth(200)
    f.setVideoFrameHeight(200)
    
    
    root.mainloop()