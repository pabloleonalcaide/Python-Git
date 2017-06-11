__author__ = "Pablo Leon Alcaide"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import git and os repository, we need the os repository to check de path
import git
import os


def getOption():
    option = (int(raw_input('\nSelecciona una opcion:\n\t1-Comprobar status\
        \n\t2-Insertarlo todo\n\t3-Insertar fichero especifico\n\t4-Salir')))
    print ' '

    return option
print ' '
print '--------------------------------'
print '|Bienvenido al asistente de git|'
print '--------------------------------'
#insert the path
ruta = raw_input('Indica la ruta absoluta del repositorio: ')

if os.path.isdir(ruta):
    #find the .git
    if os.path.isdir(ruta+'/.git'):
        print 'repositorio encontrado'
        repositorio = git.Repo(ruta)
        try:
            opcion = getOption()
            while True:
                if opcion == 1:
                    #check the status
                    print repositorio.git.status()
                elif opcion == 2:
                    #execute the 'add .' (all) and 'commit -m' commands
                    print repositorio.git.add('.')
                    comentario = raw_input('comentario para el commit: ')
                    print repositorio.git.commit( m=comentario)
                elif opcion == 3:
                    fichero = raw_input('indica el nombre del fichero')
                    #check if 'fichero' is a file
                    if os.path.isfile(fichero):
                        print repositorio.git.add('fichero')
                        comentario = raw_input('comentario para el commit: ')
                        print repositorio.git.commit( m=comentario)
                    else:
                        print 'no existe el fichero solicitado'
                elif opcion == 4:
                    print 'bye!'
                    break
                opcion = getOption()

        except ValueError:
            print 'Introduciste una opcion incorrecta'
    else:
        print 'repositorio no encontrado en el directorio'
else:
    print 'No introduciste ninguna ruta'
