'''
Created on 9 Jul 2015

@author: sfrullo
'''

# core imports
import tkinter as tk

# local imports
from mahnobplayer.gui.camviewer import CamViewer
from mahnobplayer.controller import Controller

if __name__ == '__main__':
    # tk root hook
    root = tk.Tk()
    
    ctr = Controller()
    camview = CamViewer(root, controller=ctr)
    
    # set min size of the main window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    # start root mainloop
    root.mainloop()