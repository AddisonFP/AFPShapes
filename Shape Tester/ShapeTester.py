import math
print('Choose a shape and insert dimensions')
print('I will calculate its volume and surface area')
shape = input('choose a box, pyramid, or sphere: ')
if (shape == 'box'):
    from box import *
if (shape == 'pyramid'):
    from pyramid import *
if (shape == 'sphere'):
    from sphere import *
