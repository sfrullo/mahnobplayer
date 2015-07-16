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
        self.__medialist = ['---'] + medialist if len(medialist) > 0 else ['---']
        
        self.__videoframe = VideoFrame(self, bg='white', padx=0, pady=0)
        self.__videoframe.grid(column=0,row=0, sticky='nesw')
        
        class FormattedTkStringVar(tk.StringVar):
            def __init__(self, master=None, value=None, name=None):
                tk.StringVar.__init__(self, master, value, name)
        
        self.selectionvar = FormattedTkStringVar()
        self.selectionvar.set(self.__medialist[0])
        self.__selectionlist = tk.OptionMenu(self, self.selectionvar, *self.__medialist, command=self.on_select)
        self.__selectionlist.config(relief=tk.GROOVE, indicatoron=0)
        self.__selectionlist.grid(column=0,row=1, sticky='ew')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def getCurrentSelection(self):
        return self.selectionvar.get()
    
    def SetCurrentSelection(self, value):
        self.selectionvar.set(value)
    
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
        menu.delete(0, 'end')
        menu.add_command(label='---', command=tk._setit(self.selectionvar, '---', self.on_select))
        for v in medialist:
            menu.add_command(label=path.basename(v), 
                             command=tk._setit(self.selectionvar, v, self.on_select))
        
    #---------------------------------------------------------------------------
    # Callbacks
    #---------------------------------------------------------------------------
    def on_select(self, selection):
        # notify the parent that a video was selected
        self.getParent().on_selection(self, selection)
    
if __name__ == '__main__':
    
    root = tk.Tk()
    
    f = selectableVideoFrame(root, ['1','2','3'])
    f.setVideoFrameWidth(200)
    f.setVideoFrameHeight(200)
    
    
    root.mainloop()