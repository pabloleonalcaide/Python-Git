#!/usr/bin/python

__author__ = "Pablo Leon Alcaide"

import commands
import subprocess
import os
import sys

#Recuperamos el registro de operaciones en la carpeta donde tenemos nuestro repositorio local
operation = subprocess.Popen( "/usr/bin/git log" , 
	cwd = os.path.dirname( '/home/pablo/workspace_proyecto/' ), 
	shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = operation.communicate()

#Imprimimos los posibles errores
print "Error: " + str(error)
#Imprimimos los registros de log
print "Registro: " + str(out)
