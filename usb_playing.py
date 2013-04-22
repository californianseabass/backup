# /import usb.core
# import usb.util

import dircache, io, os
from os import listdir
from os import path
from os import makedirs

base = '/Volumes/'
volumes = dircache.listdir(base)

for vol in volumes:
	if (vol != 'Simba'):
		curr_path = base + vol + '/'
		dest_dir = "/Users/californianseabass/Desktop/" + vol
		print dest_dir
		if not os.path.isdir(dest_dir):
			os.mkdir(dest_dir)
			print "created directory %s" % dest_dir
		# print curr_path
		# result = commands.getstatusoutput('cp -r %s /Users/californianseabass/Desktop/' % (path))
		files = listdir(curr_path)
		for file_name in files:
			srcfile = curr_path + file_name
			if (path.isfile(srcfile)):
				fd_read = io.open(srcfile, 'rb')
				if (fd_read.name == "/Volumes/TEST/._.Trashes"):
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

# base = '/dev/'
# volumes = dircache.listdir(base)


# for vol in volumes:
# 	if (re.match("rdisk*", vol)):
# 		path = base + vol
# 		if (re.match("1234567", vol)):
# 			print path
# 			open(path, 'r')



# for dirname, dirnames, filenames in os.walk('.'):
#     # print path to all subdirectories first.
#     for subdirname in dirnames:
#         print os.path.join(dirname, subdirname)

#     # print path to all filenames.
#     for filename in filenames:
#         print os.path.join(dirname, filename)

#     # Advanced usage:
#     # editing the 'dirnames' list will stop os.walk() from recursing into there.
#     if '.git' in dirnames:
#         # don't go into any .git directories.
#         dirnames.remove('.git')


# import usb
# import sys

# dev = usb.core.find(idVendor=0x0bda)

# # was it found?
# if dev is None:
#     raise ValueError('Device not found')

# if dev.is_kernel_driver_active(0) is True:
# 	dev.detach_kernel_driver(0)

# # set the active configuration. With no arguments, the first
# # configuration will be the active one
# dev.set_configuration()

# # get an endpoint instance
# cfg = dev.get_active_configuration()
# interface_number = cfg[(0,0)].bInterfaceNumber
# alternate_setting = usb.control.get_interface(dev, interface_number)
# intf = usb.util.find_descriptor(cfg, bInterfaceNumber = interface_number,bAlternateSetting = alternate_setting)

# ep = usb.util.find_descriptor(intf,
#     # match the first OUT endpoint
#     custom_match = \
#     lambda e: \
#         usb.util.endpoint_direction(e.bEndpointAddress) == \
#         usb.util.ENDPOINT_OUT
# )

# assert ep is not None

# for cfg in dev:
#     sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
#     for intf in cfg:
#         sys.stdout.write('\t' + \
#                          str(intf.bInterfaceNumber) + \
#                          ',' + \
#                          str(intf.bAlternateSetting) + \
#                          '\n')
#         for ep in intf:
#             sys.stdout.write('\t\t' + \
#                              str(ep.bEndpointAddress) + \
#                              '\n')


# cfg.set()
# dev.set_configuration(cfg)
# write the data
# ep.write('test')
