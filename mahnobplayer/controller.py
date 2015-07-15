'''
Created on 14 Jul 2015

@author: sfrullo
'''

from mahnobplayer.mediaplayer import player
from random import randint

class Controller:
    ''' This class implements the main controller for the application '''


    def __init__(self, playername=None):
        '''
        Constructor
        '''
        self.player = player.MultipleMediaPlayer() if not playername else player.MultipleMediaPlayer(name=playername)
        
            
    def on_media_added(self, notifier, addedMedia):
        for path in addedMedia:
            self.player.addMediaToPlaylist(path, hasAudio=False, hasVideo=True)
        
    def on_selection(self, notifier, videoframe, selection):
        print('work on_selection')
        if selection == '---':
            videoframe.winfo_visualsavailable(False)
        else:
            self.player.setMediaXid(selection, videoframe.getXid())
        
    def on_play(self, invoker):
        print(invoker, 'call on_play')
        self.player.play()
    
    def on_stop(self, invoker):
        print(invoker, 'call on_stop')
        self.player.stop()
    
    def on_pause(self, invoker):
        print(invoker, 'call on_pause')
        self.player.stop()
    
    def on_rew(self, invoker):
        print(invoker, 'call on_rew')
        self.player.rew()
    
    def on_ffw(self, invoker):
        print(invoker, 'call on_ffw')
        self.player.ffwd()