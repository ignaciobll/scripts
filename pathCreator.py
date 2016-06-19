import os
import sys


subject = str(sys.argv[1])

if str(sys.argv[1]) == '--help':
    htext = """
python pathCreator.py [Nombre de la asignatura] [Fichero con contenido]

python pathCreator.py --help       ::       Muestra la ayuda

Para usar el script debes indicar un fichero donde se encuentre la estructura de una asignatura (indice de conentido) con el formato:

1. Punto 1
1.1 Subapartado de 1

#sexyACM
"""
    print(htext)
    sys.exit()


path = {}
info = './' + str(sys.argv[2])


def addPath(name, path):
    depth = name.split('. ')[0].split('.')
    current_depth = path
    for i in range(depth.__len__()-1):
        if (not current_depth[str(depth[i])]):
            current_depth[str(depth[i])] = {}
        current_depth = current_depth[str(depth[i])]
    current_depth[str(depth[-1])] = {'dir': str(name)}

with open(info, 'r') as f:
    title = f.readline()
    while(title):
        addPath(str(title).strip('\n'), path)
        title = f.readline()

dirs = []

for i in range(path.keys().__len__()):
    father = './' + subject + '/' + path[str(i+1)]['dir'] + '/'
    for j in range(path[str(i+1)].__len__()-1):
        son = path[str(i+1)][str(j+1)]['dir'].strip('.')
        dirs.append(father+son + '/')

for i in range(dirs.__len__()):
    if not os.path.exists(dirs[i]):
        os.makedirs(dirs[i])
