import os
import re
import sys
from PIL import Image
import numpy as np

inputfolder = 'image/test'
outputfolder = 'image/test_crop'

for root, dirs, files in os.walk(inputfolder):
  cols_min = 500
  cols_max = 1200
  rows_min = 400
  rows_max = 1000

  for file in files:
    if re.findall(r'.png',file):
      im = Image.open(os.path.join(root, file)).convert('RGBA')
      na = np.array(im)
      opaque = na[np.ix_(range(rows_min,rows_max),range(cols_min,cols_max),range(4))]

      outroot = root.replace(inputfolder,outputfolder)
      if os.path.exists(outroot) == False:
        os.makedirs(outroot)
      Image.fromarray(opaque).save(os.path.join(outroot,file))