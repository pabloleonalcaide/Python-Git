__author__ = "Pablo Leon Alcaide"
#import git and os repository, we need the os repository to check de path
import git
import os

print 'Bienvenido al asistente de git'

#insert the path
ruta = raw_input('indica la ruta absoluta del repositorio: ')

if os.path.isdir(ruta):
    #find the .git
    if os.path.isdir(ruta+'/.git'):
        print 'repositorio encontrado'
        repositorio = git.Repo(ruta)
        try:
            opcion = int(raw_input('\nSelecciona una opcion:\n\t1-Comprobar status\n\t2-Realizar commit\n\t3-Salir'))
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
                    break
                opcion = int(raw_input('\nSelecciona una opcion:\n\t1-Comprobar status\n\t2-Realizar commit\n\t3-Salir'))

        except ValueError:
            print 'Introduciste una opcion incorrecta'
    else:
        print 'repositorio no encontrado en el directorio'
else:
    print 'No introduciste ninguna ruta'
