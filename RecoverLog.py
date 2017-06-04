#!/usr/bin/python

__author__ = "Pablo Leon Alcaide"

import commands
import subprocess
import os
import sys


pr = subprocess.Popen( "/usr/bin/git log" , cwd = os.path.dirname( '/home/pablo/workspace_proyecto/' ), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr.communicate()


print "Error : " + str(error)

print "out : " + str(out)
