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
    dest_dir = base + 'DEST/'
    print dest_dir
    if not os.path.isdir(dest_dir):
      os.mkdir(dest_dir)
      print "created directory %s" % dest_dir
    files = listdir(curr_path)
    if curr_path == "media/DEST":
      files = []
    for file_name in files:
      srcfile = curr_path + file_name
      if (path.isfile(srcfile)):
        fd_read = io.open(srcfile, 'rb')
        if (fd_read.name == "/media/SRC/._.Trashes"):
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


import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb", shell=True)
devices = []
for line in df.split('\n'):
  if re.match("USB High-Speed Bus", line):
    print line
    info = device_re.match(i)
    if info:
        dinfo = info.groupdict()
        dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
        devices.append(dinfo)
print devices
