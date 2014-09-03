import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage

dna = mahotas.imread('dna.jpeg')

pylab.imshow(dna)
pylab.show()

pylab.imshow(dna)
pylab.gray()
pylab.show()

print dna.shape
print dna.dtype
print dna.max()
print dna.min()

pylab.imshow(dna//2)
pylab.show()

T = mahotas.thresholding.otsu(dna)
pylab.imshow(dna>T)

pylab.show()

dnaf = ndimage.gaussian_filter(dna ,7)
T = mahotas.thresholding.otsu(dnaf)
pylab.imshow(dnaf>T)
pylab.show()
print dnaf

labeled,nr_objects = ndimage.label(dnaf > T)
print 'number:' , nr_objects
pylab.imshow(labeled)
pylab.jet()
pylab.show()

//edited
