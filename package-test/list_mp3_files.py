from id3_utils import basic_mp3_info
from id3_utils.id3_base_utils.getmp3files import GetMp3Files

baseDir = "/adat/Zene/World music/Omar Bashir/The Crazy Oud/"

flist = GetMp3Files(baseDir)

print("List of mp3 files")
print("=================\n")

for fname in flist.mp3FileList():
	print(fname)
	basic_mp3_info.getinfo(baseDir + fname)
	print("_____________________________________________________________")

