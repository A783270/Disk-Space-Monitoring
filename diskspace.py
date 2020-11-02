# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:25:17 2020

@author: a783270
"""

import shutil 

# Path 
path = "C:/"
  
# Get the disk usage statistics 
# about the given path 
stat = shutil.disk_usage(path) 

# Print disk usage statistics 
print("Disk usage statistics:") 
print(stat[0],stat[1],stat[2])
data = round((stat[2]/stat[0])*100)
print(str(data)+'%')