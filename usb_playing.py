# /import usb.core
# import usb.util

import dircache, commands, re
from os import listdir

base = '/Volumes/'
volumes = dircache.listdir(base)

for vol in volumes:
	if (vol != 'Simba'):
		path = base + vol
		print path
		result = commands.getstatusoutput('diskutil unmount %s' % (path))
		if result[0] != 0:
			print "Something went wrong unmounting %s" % (path)
			sys.exit(1);
		# result = commands.getstatusoutput('diskutil eject %s' % (path))
		# if result[0] != 0:
		# 	print "Something went wrong ejecting %s" % (path)
		# 	sys.exit(1); 
		print "Successfully umounted  %s" % (path)

	else:
		print "don't touch Simba please!!!"

base = '/dev/'
volumes = dircache.listdir(base)


for vol in volumes:
	if (re.match("rdisk*", vol)):
		path = base + vol
		if (re.match("rdisk1*", vol) is not 0):
			print path
			open(path, 'r')




