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
        self.player.setMediaXid(selection, videoframe.getXid())
        
    def on_play(self, mediacontrol):
        self.player.play()
    
    def on_stop(self, mediacontrol):
        self.player.stop()
    
    def on_pause(self, mediacontrol):
        pass
    
    def on_rew(self, mediacontrol):
        pass
    
    def on_ffw(self, mediacontrol):
        pass