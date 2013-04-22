# /import usb.core
# import usb.util

import dircache, commands

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
		result = commands.getstatusoutput('diskutil eject %s' % (path))
		if result[0] != 0:
			print "Something went wrong ejecting %s" % (path)
			sys.exit(1); 
		print "Successfully umounted and ejected %s" % (path)
	else:
		print "don't touch Simba please!!!"
