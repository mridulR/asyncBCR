import logging
import os

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

