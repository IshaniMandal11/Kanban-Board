# import video_7 #we can write this
import video_7 as mm
# from video_7 import * # this will import everything on from that module
#from video_7 import find_index # this will allow you to use this particular function of that module only
course= ['math','hindi','art']
# index = video_7.find_index(course, 'math')
index = mm.find_index(course, 'math') # we can write this also
print(index)