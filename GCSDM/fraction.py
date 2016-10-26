# Plot of the rates as a funtion of the number of attributes
from pylab import *

a = r_[37,43,21,40,35,50,30,37,37,57,42,46,32,32,22]
z= array([4.22E-10,3.02E-04,1.04E-01,3.91E-05,8.58E-03,2.52E-07,2.22E-02,3.97E-04,1.64E-01,3.08E-08,3.41E-06,4.18E-07,2.97E-01,4.64E-01,3.88E-01])

p = polyfit(a,log10(z),1)
Z = 10**(polyval(p,a))

img = figure(figsize=(6,6))

semilogy(a,Z,a,z,'bo')

grid()
title('GCredut fraction vs. the number of attributes')
xlabel('Attributes')
ylabel('Fraction of evaluated candidates')

img.savefig('candidates.eps')
