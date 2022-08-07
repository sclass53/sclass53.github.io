from os import path
import glob

temp,filename=path.split(__file__)
files=glob.glob(temp+"\\*")
files.pop(files.index(__file__))

