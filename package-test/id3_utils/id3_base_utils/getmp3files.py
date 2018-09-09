import os

class GetMp3Files(object):

	def __init__(self,topdir):
		self.topdir = topdir

	def mp3FileList(self):
		flist = []
		
		for f in os.listdir(self.topdir):
			if f.endswith('.mp3'):
				flist.append(f)
		
		return flist