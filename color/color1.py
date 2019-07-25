#!/usr/bin/env python3
import crayons

#print 'red string' in red
print(crayons.red('Red String'))

# red white an blue
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.disable() #disables color pack
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.
