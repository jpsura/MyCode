#!usr/bin/env python3
"""
Sura Script
creating directories
"""

##The following will create a DIR and add files that do not already exist
import shutil
import os
os.chdir("/home/student/mycode/")
shutil.copy("5g_research/snd_network.txt", "5g_research/snd_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")
