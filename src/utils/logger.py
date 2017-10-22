import logging
import os
import glob, os, os.path


FORMAT = '%(asctime)s.%(msecs)03d %(NodeName)s: %(NodeId)s:%(levelname)s: %(message)s'

NODE_INFO = {'NodeId': 'Default', 'NodeName': 'Default'}

def getLogDir():                                                          
    cwd = os.getcwd()
    logDir = cwd + "/logs/"
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    return logDir 

def setLogNodeInfo(nodeId, nodeName):
    NODE_INFO['NodeId'] = nodeId
    NODE_INFO['NodeName'] = nodeName
    return

def setLogFormatting(fname, logDir, logLevel):
    logging.basicConfig(format=FORMAT,filename=logDir+fname,
                   filemode='a',
                   level= logLevel,
                   datefmt='%Y-%m-%d %H:%M:%S')
    return

def cleanLogFile(fname, logDir):
    name = logDir + fname
    print("CleanLogFile ------ ", name)
    if os.path.isfile(name):
        with open(name, 'w'): pass    
    return

def cleanLogDirectory(cleanDir):
    filelist = glob.glob(os.path.join(cleanDir, "*.log"))
    for f in filelist:
        os.remove(f)
    return
