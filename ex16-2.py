from sys import argv

script, filename = argv

balloonballs = open(filename)

print balloonballs.read()

balloonballs.close()
