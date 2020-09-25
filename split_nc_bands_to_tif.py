#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""
提取nc数据集中每个波段为一个tiff数据
"""
import os

lenBands = 264 #波段个数，可以从gdalinfo中获取
for nband in range(1,lenBands):
#     cmd = "gdal_translate.exe -of GTiff -b {0} F:\田德宇5st\\2020——三室自研\估产\data\\temp\min\\f9c0e7cc-ea38-4290-85ab-b4fd93de3bb0.nc F:\田德宇5st\\2020——三室自研\估产\data\\temp\min\\f9c0e7cc-ea38-4290-85ab-b4fd93de3bb0.tiff".format(nband)
    cmd = "gdal_translate.exe -of GTiff -b {0} b718bc1b-12c4-4262-81ab-bb280ab4f70e.nc min_{0}.tiff".format(nband)
    print(cmd)
    os.system(cmd)


# In[ ]:




