'''
Created on 9 Jul 2015

@author: sfrullo
'''

# core imports
import tkinter as tk

# local imports
from mahnobplayer.gui.camviewer import CamViewer
from mahnobplayer.controller import Controller

import logging
from mahnobplayer import logger
log = logging.getLogger('main')

if __name__ == '__main__':
    # tk root hook
    root = tk.Tk()
    
    log.info('started')
    ctr = Controller()
    camview = CamViewer(root, controller=ctr)
    
    # set min size of the main window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    # start root mainloop
    root.mainloop()