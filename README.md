# MahnobPlayer

**MahnobPlayer** is a mediaplayer designed to easily work with [Mahnob Databases](http://mahnob-db.eu/hci-tagging).
It is designed in [Python3](https://www.python.org/downloads/) and it made large use of *gst-python* bindings to exploit [GStreamer](http://gstreamer.freedesktop.org/) powerfull multimedia framework functionalities.

It provides multiple views:

- *CamViewer* allows to view multiple streams in a syncronized way. It was designed to observe an indefinite number of sources arranged in a grid, with the ability to dynamically add video and arrange them in the desired panel. Furthermore, new windows with a desired number of panels that shares loaded sources could be istantiated.

- *GazeViewer* allows to view gaze data parsed from a session's *.tsv* file overlaid to the video stimulus.

- *SessionViewer* works as a combination of *CamViewer* and *GazeViewer* to allow the user to observe, in a synchronized manner, gaze and behavioral reactions of a subject during the entire session.


## Installation

#### Dependencies

MahnobPlayer use as much standard library modules as possible to try to mantain cross-platform compatibily (not tested yet).
At the current stage, the project has the following dependencies:

- System Depencencies:
  - [GStreamer](http://gstreamer.freedesktop.org/)
  - [Python3.x](https://www.python.org/downloads/)
- Python Depencencies:
  - [Pillow 2.8.1](https://pypi.python.org/pypi/Pillow/2.9.0) : `pip install Pillow`
  - [numpy](http://www.numpy.org/) : `pip install numpy`


## How to use

To start the application:

* `cd` to the mahanobplayer project's root.
* `python3 main.py`


## To do

* Testing cross-platform compatibility.
* Find a way to build *EegViewer* to integrate eeg data as for gaze data.