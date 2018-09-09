#!/usr/bin/python

# Import mp3 ID3 data to SQLite database

# Mutagen docs: https://mutagen.readthedocs.io/en/latest/tutorial.html

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import pprint


def getinfo(fname):

	audio = MP3(fname, ID3=EasyID3)
	#audio.pprint()
	#print(audio)
	
	print( "Artist: {}".format( audio['artist'] ) )
	print("Title: {}".format( audio['title'] ) )
	