import sys
from moviepy.editor import *

name = sys.argv[1]
output = sys.argv[2]

codecs = {
	'ogg': 'libvorba',
	'mp4': 'mpeg4'
}

# codec = codecs[output.split('.')[-1]]

video = VideoFileClip(name)
video = video.volumex(0)

# uncomment when doing OGG
# video.write_videofile(output, codec='libtheora', audio_codec='libvorbis')

# comment out when doing OGG
video.write_videofile(output)