import os
import shutil
import tkSimpleDialog
#from Tkinter import *
import Tkinter as tk
from TheGUI import AppGUI
from SplashScreen import Splash
from os.path import expanduser
home = expanduser("~")
archive = home+'/'+'PyCross_Archive'

def MakeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        shutil.rmtree(directory)
        os.makedirs(directory)

def ClearTempData():
    if not os.path.exists('TempData'):
        os.makedirs('TempData')
    else:
        shutil.rmtree('TempData')
        os.makedirs('TempData')

def ClearPlots():
    if not os.path.exists('Plots'):
        os.makedirs('Plots')
    else:
        shutil.rmtree('Plots')
        os.makedirs('Plots')

def MakeArchive():
    if not os.path.exists(archive):
        os.makedirs(archive)
    print 'Making Archive'

def MakePlotArchive():
    if not os.path.exists(archive+'/PlotArchive'):
        os.makedirs(archive+'/PlotArchive')
    print 'Making Plot Archive'

def MakePlots():
    if not os.path.exists(archive+'/Plots'):
        os.makedirs(archive+'/Plots')
    if not os.path.exists(archive+'/Plots/Profiles'):
        os.makedirs(archive+'/Plots/Profiles')
    if not os.path.exists(archive + '/Plots/Emissions'):
        os.makedirs(archive + '/Plots/Emissions')


def main():
    ClearTempData()
    ClearPlots()
    MakeDir("MakeData")
    MakeArchive()
    MakePlots()
    MakePlotArchive()

    root = tk.Tk()
    image_file = "splash.gif"
    s = Splash(root, timeout=3000, image=image_file)
    myGUI = AppGUI(root, "PyCROSS")
    root.mainloop()


if __name__ == '__main__':
    main()



"""
cloudyPath = '/Users/kfitzgerald/c13.05/source/sys_gcc/cloudy.exe'
dir_ = '/Users/kfitzgerald/pyCloudy/PyCROSS/'
#file = 'V5668Sgr_bipolar_varydens.txt'
file = 'quart_polar_v5668Sgr_seg.txt'


print 'Removing temp data and creating new directories'
ClearTempData()
MakeDir("MakeData")

first = Grunt(dir_+"TextFiles/", file, 1)
print 'The minumum and maximum radaii:'
print first.MinMax()

print('Stage 1 Complete, DATA GENERATED')

second = RunCloudy(dir_+"MakeData", "ShapeCloudy", cloudyPath, dir_+"TempData/ShapeCloudy.txt")

print('Stage 2 Complete, Cloudy Executed')

third = GenPlot(dir_+"MakeData", "ShapeCloudy")

print('All Stages Completed')
"""