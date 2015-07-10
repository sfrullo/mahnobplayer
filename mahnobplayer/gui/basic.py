'''
Created on 9 Jul 2015

@author: sfrullo
'''

import tkinter as tk


class BasicMenu(tk.Menu):
    
    
    def __init__(self, parent, *arg, **kwarg):
        tk.Menu.__init__(self, parent, *arg, **kwarg)
        self.config(relief=tk.FLAT)
        self.parent = parent
        
#         menudata = (
#             [
#                 '_File', (
#                     ('_Quit', 'Alt-F4', self.parent.quit),
#                 ),
#             ],
#         )
#         
#         self.addSubMenu(menudata)
#         
    def addSubMenu(self, menudata):
        ''' Based on Jens Diemer's code.
        loc: https://code.google.com/p/python-code-snippets/source/browse/tkinter_tools/automenu.py '''
        
        def prepstr(label, used):
            """
            Based on prepstr() from python/Lib/idlelib/EditorWindow.py
            Helper to extract the underscore from a string, e.g.
            prepstr("Co_py") returns (2, "Copy").
            Check if the used character is unique in the menu part.
            """
            i = label.find('_')
            if i >= 0:
                label = label[:i] + label[i+1:]
    
                char = label[i]
                assert char not in used, (
                    "underline %r used in %r is not unique in this menu part!"
                ) % (char, label)
                used.append(char)
    
            return i, label
    
        used_topunderline = []
        for toplabel, menuitems in menudata:
            # add new main menu point
            menu = tk.Menu(self, tearoff=False)
            menu.config(relief=tk.GROOVE, bg = 'white')
            underline, toplabel = prepstr(toplabel, used_topunderline)
            self.add_cascade(label=toplabel, menu=menu, underline=underline)
    
            # add all sub menu points
            used_underlines = []
            for index, menudata in enumerate(menuitems):
                if not menudata:
                    menu.add_separator()
                    continue
    
                label, keycode, command = menudata
    
                underline, label = prepstr(label, used_underlines)
    
                menu.add_command(label=label, underline=underline, command=command)
                if keycode:
                    menu.entryconfig(index, accelerator=keycode)
                    self.bind("<"+keycode+">", command)


class BasicWindow(tk.Toplevel):
    ''' Basic TopLevel class '''


    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
    def getGridSize(self):
        return self.size()
    
    def getWidth(self):
        return self.winfo_width()
    
    def setWidth(self, value):
        self.config(width = value)
        
    def getHeight(self):
        return self.winfo_height()
    
    def setHeight(self, value):
        self.config(height = value)
        
    def getXid(self):
        return self.winfo_id()
    
    def setMenu(self, menu):
        self.config(menu=menu)



class BasicFrame(tk.Frame):
    ''' Basic Frame class '''


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
 
    def getGridSize(self):
        return self.size()
    
    def getWidth(self):
        return self.winfo_width()
    
    def setWidth(self, value):
        self.config(width = value)
        
    def getHeight(self):
        return self.winfo_height()
    
    def setHeight(self, value):
        self.config(height = value)
        
    def getXid(self):
        return self.winfo_id()
    
    def setMenu(self, menu):
        self.config(menu=menu)
        


#-------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    
    root = tk.Tk()
     
    window = BasicWindow(root)
    window.title('window')
    window.setHeight(500)
    window.setWidth(500)
    
    
    window1 = BasicWindow(window)
    window1.setMenu(BasicMenu(window1))
    window1.title('window1')

    app = BasicFrame(window1)
    app.config(bg='white')
    app.setHeight(300)
    app.setWidth(300)
    app.grid(column=0,row=0)
    
    app = BasicFrame(window1)
    app.config(bg='black')
    app.setHeight(300)
    app.setWidth(300)
    app.grid(column=1,row=1)
     
    root.mainloop()