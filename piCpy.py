# /import usb.core
# import usb.util

import dircache, io, os
from os import listdir
from os import path
from os import makedirs
from datetime import datetime

startTime = datetime.now()

base = '/media/'
volumes = dircache.listdir(base)

for vol in volumes:
	if (vol != 'root'):
		curr_path = base + vol + '/'
		dest_dir = "/home/pi/Desktop/" + vol
		if not os.path.isdir(dest_dir):
			os.mkdir(dest_dir)
			print "created directory %s" % dest_dir
		files = listdir(curr_path)
		for file_name in files:
			srcfile = curr_path + file_name
			if (path.isfile(srcfile)):
			  fd_read = io.open(srcfile, 'rb')
			  if (fd_read.name == "/media/TEST/._.Trashes"):
			    print "dont' do this"
			  else:
			    dest = dest_dir + '/' +file_name
			    dest_buf = open(dest, 'w+')
			    rbuf = io.BufferedReader(fd_read, 4096)
			    data = rbuf.read()
			    while (data):
			      dest_buf.write(data)
			      data = rbuf.read()
			  fd_read.close()
	else:
		print "don't touch Simba please!!!"

print(datetime.now() - startTime)
