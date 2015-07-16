'''
Created on 14 Jul 2015

@author: sfrullo
'''

from mahnobplayer.mediaplayer import player
from random import randint

import logging
log = logging.getLogger('controller')

def callbackLogDecorator(f):
    def wrapper(*arg, **kwarg):
        log.info('{} calls {}'.format(arg[1].__name__, f.__name__))
        return f(*arg, **kwarg)
    wrapper.__name__ = f.__name__
    return wrapper

class Controller:
    ''' This class implements the main controller for the application '''


    def __init__(self, playername=None):
        '''
        Constructor
        '''
        self.player = player.MultipleMediaPlayer() if not playername else player.MultipleMediaPlayer(name=playername)
        
            
    def on_media_added(self, notifier, addedMedia, xids):
        for path, xid in zip(addedMedia,xids):
            self.player.addMediaToPlaylist(path, hasAudio=False, hasVideo=True)
            self.player.setMediaXid(path, xid)
        
    def on_selection(self, notifier, videoframe, selection):
        log.info('{} selected on {}'.format(selection, videoframe))
        if selection == '---':
            media = self.player.getMediaFromXid(videoframe.getXid())
            if media: media.setXid(0)
        else:
            self.player.setMediaXid(selection, videoframe.getXid())
    
    @callbackLogDecorator
    def on_play(self, invoker):
        self.player.play()
    
    @callbackLogDecorator
    def on_stop(self, invoker):
        self.player.stop()
    
    @callbackLogDecorator
    def on_pause(self, invoker):
        self.player.stop()
    
    @callbackLogDecorator
    def on_rew(self, invoker):
        self.player.rew()
    
    @callbackLogDecorator
    def on_ffw(self, invoker):
        self.player.ffwd()