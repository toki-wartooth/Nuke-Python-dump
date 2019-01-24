## [value NODE_NAME.projDir]/folder1/floder2/[value NODE_NAME.section]_[value NODE_NAME.floor]/1.filename_P[value NODE_NAME.plan]_S[value NODE_NAME.section]_L[value NODE_NAME.floor].####.jpg


##
	# 
	# import nuke


	nProject = nuke.root()

	nodesList=list()
	writeNodesList=list()

	lastframeList=list()
	firstframeList=list()



	## create write nodes and fill lists
	for iiter, enumSel in enumerate(nuke.selectedNodes()):
	    fileName = enumSel.knob('file').value()

	    inFirstFrame = enumSel.knob('first').value()
	    inLastFrame = enumSel.knob('last').value()

	    newFileName = fileName[:-4]+".mov"
	    print newFileName 

	    a=nuke.nodes.Write(file=newFileName, file_type="mov", first=inFirstFrame, last=inLastFrame, use_limit=True, create_directories=True)
	    a.setInput(0, enumSel)
	    nodesList.append(enumSel)

	    writeNodesList.append(a)
	    lastframeList.append(inLastFrame)
	    firstframeList.append(inFirstFrame)
	    

	print writeNodesList

	## set codec
	##for y in writeNodesList:
	    # y.knob("meta_codec").setValue("mp4v")
	    #y.knob("_jpeg_quality").setValue(1)
	    # print "codecType ", y.knob("meta_codec").value()
	    #print "max quality", y.knob("mov64_quality_max").value()

	## set project maxFrame
	nProject.knob("last_frame").setValue(max(lastframeList))
	nProject.knob("first_frame").setValue(min(firstframeList))
##



import csv
import sys

WriteBase = 'Write_MAIN'
ReadBase = 'ReadMAIN'

file=open(r"z:/production/Z_Exterior/01_Rumyzncevo/Renders/PANO_PLAN_EXT/00_system/data/data_01.txt", "r")
csvReader = csv.reader(file, delimiter="\t")

EpicWrite = nuke.toNode(WriteBase)
seqTime = str(int(nuke.toNode(ReadBase).knob('first').getValue()))+'-'+str(int(nuke.toNode(ReadBase).knob('last').getValue()))


for row in csvReader:
    print (row)
    print (len(row))
    nuke.toNode('NODE_NAME').knob('framehold').setValue(int(row[0]))
    nuke.toNode('NODE_NAME').knob('section').setValue(row[1])
    nuke.toNode('NODE_NAME').knob('floor').setValue(row[2])
    print nuke.toNode('NODE_NAME').knob('framehold').getValue()
    print nuke.toNode('NODE_NAME').knob('section').getValue()
    print nuke.toNode('NODE_NAME').knob('floor').getValue()
    nuke.executeBackgroundNuke(nuke.EXE_PATH,[EpicWrite],nuke.FrameRanges(seqTime),['main'],{'maxThreads':4, 'maxCache':"5G"})


##


import csv
import sys
import time

WriteBase = 'Write_MAIN'  # node name in variable
ReadBase = 'ReadMAIN' # same

file=open(r"z:/production/Z_Exterior/01_Rumyzncevo/Renders/PANO_PLAN_EXT/00_system/data/data_01.txt", "r") # open file for read
csvReader = csv.reader(file, delimiter="\t") # read csv contrnt with space delimiter

EpicWrite = nuke.toNode(WriteBase)  # locate node in graph with setted name
seqTime = str(int(nuke.toNode(ReadBase).knob('first').getValue()))+'-'+str(int(nuke.toNode(ReadBase).knob('last').getValue()))  # compose string of frames for write node

# cycle in file
for row in csvReader: # in csv file for each row  -- ERROR -- ROW is actually column in csv
    print (row) # 
    print (len(row)) #
    nuke.toNode('NODE_NAME').knob('framehold').setValue(int(row[0])) # set framehold value from file
    nuke.toNode('NODE_NAME').knob('section').setValue(row[1]) # set cetion value from file
    nuke.toNode('NODE_NAME').knob('floor').setValue(row[2]) # set floor value from file 
    print nuke.toNode('NODE_NAME').knob('framehold').getValue() # print results
    print nuke.toNode('NODE_NAME').knob('section').getValue()
    print nuke.toNode('NODE_NAME').knob('floor').getValue()
    nuke.executeBackgroundNuke(nuke.EXE_PATH,[EpicWrite],nuke.FrameRanges(seqTime),['main'],{'maxThreads':4, 'maxCache':"5G"}) # setup bg render with one write node. exe_path is ok, need to spec writenode, framerange string
    time.sleep(1) # wait for next iteration




import csv
import sys

txtFile = nuke.toNode('NODE_NAME').knob('datafile').getValue()

file=open(txtFile, "r")
csvReader = csv.reader(file, delimiter="\t")


for row in csvReader:
    print (row)
    print (len(row))



#


[value NODE_NAME.projDir]/[value NODE_NAME.plan]/post_[value NODE_NAME.type]/S[value NODE_NAME.section]_L[value NODE_NAME.floor]/1.P[value NODE_NAME.plan]_S[value NODE_NAME.section]_L[value NODE_NAME.floor].####.jpg


[value PATHS_NODE.path]/C[value PATHS_NODE.CEKK]/bg/BASE_CAMERA_C0[value PATHS_NODE.CEKK]_####.exr

Z:/production/Rumyancevo-88/floor/RENDERS/C04/180330/Final/1.VRayDenoiser.####.tif
[value PATHS_NODE.path]/C[value PATHS_NODE.CEKK]/base/1.VRayDenoiser.####.tif

[value PATHS_NODE.path]/C[value PATHS_NODE.CEKK]/base/1_.Alpha.####.tif
[value PATHS_NODE.path]/C[value PATHS_NODE.CEKK]/base/1_.VRayReflection.####.tif

[value PATHS_NODE.path]/out/C[value PATHS_NODE.CEKK]/[value PATHS_NODE.framehold]/1.Denoiser.####.jpg



#### WOKRKING METHOD ###

from os import listdir
# writer = 'WRITER'
endWrite = nuke.toNode('WRITER')
ctrl = nuke.toNode('PATHS_NODE')
timestring = ctrl.knob('allframes').getValue()

fstart = int(ctrl.knob('fstart').getValue())
path = ctrl.knob('path').getValue() + "/" + "C" + ctrl.knob('CEKK').getValue() + "/bg/"
fend = len(listdir(path))
# print (fend)
# fend = int(nuke.toNode(ctrl).knob('fend').getValue())+1
# iterate over levels with framehold and fstart fend


for i in range(0, fend, 1):
    # set value to framehold and start bg render
    ctrl.knob('framehold').setValue(int(i))
    nuke.executeBackgroundNuke(nuke.EXE_PATH,[endWrite],nuke.FrameRanges(timestring),['main'],{'maxThreads':4, 'maxCache':"5G"})

    ## time.sleep(2)

print "submitted"



pt = ctrl.knob('path').getValue()
dirlist = listdir(pt)
print (dirlist)
dl = list()
for i in dirlist:
    if i[0]=="C":
        dl.append(i[1:])

print dl
type(dl[0])
dir(dirlist[0])
type(dirlist[0])

