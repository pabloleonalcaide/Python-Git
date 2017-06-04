#Script desde el cual podemos gestionar nuestros repositorios locales de git

__author__ = "Pablo Leon Alcaide"
#importamos la libreria de git
import git
import os

print 'Bienvenido al asistente de git'

#indicamos la ruta
ruta = raw_input('indica la ruta absoluta del repositorio: ')
#comprobamos si se ha introducido un directorio (sería prudente comprobar si el directorio tiene un elemento .git)
if os.path.isdir(ruta):
    repositorio = git.Repo(ruta)
    try:
        opcion = int(raw_input('\nSelecciona una opcion:\n\t1-Comprobar status\n\t2-Realizar commit\n\t3-Salir'))
        while True:
            if opcion == 1:
                #comprobamos el status de nuestro repositorio local
                print repositorio.git.status()
            elif opcion == 2:
                #realizamos el add y su commit correspondiente
                print repositorio.git.add('.')
                comentario = raw_input('comentario para el commit: ')
                print repositorio.git.commit( m=comentario)
            elif opcion == 3:
                break
            opcion = int(raw_input('\nSelecciona una opcion:\n\t1-Comprobar status\n\t2-Realizar commit\n\t3-Salir'))

    except ValueError:
        print 'Introduciste una opcion incorrecta'
else:
    print 'No introduciste ninguna ruta'
