'''
Created on 9 Jul 2015

@author: sfrullo
'''

import tkinter as tk


class BasicMenu(tk.Menu):
    
    def __init__(self, parent, *arg, **kwarg):
        tk.Menu.__init__(self, parent, *arg, **kwarg)
        self.parent = parent
    
        menu = tk.Menu(self.parent, tearoff=0)
        self.add_cascade(label="File", menu=menu)
        menu.add_command(label="Quit")
        
        
class BasicFrame(tk.Frame):
    ''' Basic Frame class '''


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.menubar = BasicMenu(self)
        self.parent.config(menu=self.menubar)


if __name__ == '__main__':
    
    root = tk.Tk()
    mainapp = BasicFrame(root).pack()
    root.mainloop()