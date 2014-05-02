from pylab import *

n = [40,42,44,46,48,50,55]
ct = r_[300,971,2484,4378,7375.5,11166,57803]/3600.
bt = r_[1728,4391,13924]/3600.
sf = r_[3238,7320,12420,57480]/3600.

img = figure(figsize=(4,4)) # figsize=(4,8)
plot(n,ct,'k-*',n[0:-3],sf,'k-s',n[0:-4],bt,'k-^')
xlim((39,56))
grid('on')
xlabel('Attributes')
ylabel('Time (Hrs)')
title('Density 8% and 400 rows')
legend(('CTH','CTS','BTH'), loc=2)
img.savefig('low_density.eps')

n = [50,55,60,65,70,75,80,85,90]
ct = r_[434.2,712.8,1475.2,2448.4,5359.4,12933.8,19325.4,44786.1,115455]/3600.
bt = r_[78077.6]/3600.
sf = r_[14820,51060]/3600.

img = figure(figsize=(4,4)) # figsize=(4,8)
plot(n,ct,'k-*',n[0:2],sf,'k-s',n[0],bt,'k-^')
xlim((49,91))
grid('on')
xlabel('Attributes')
ylabel('Time (Hrs)')
title('Density 30% and 225 rows')
legend(('CTH','CTS','BTH'), loc=2)
img.savefig('med_density.eps')


n = [48,50,52,54,56,58,60,62,64,66,68,70]
ct = r_[639, 763, 727, 822, 958, 978, 1170, 1253, 1407, 2560, 3511, 2701]/3600.
bt = r_[78077.6]/3600.
sf = r_[1857, 2656, 3324, 4800, 6660, 0, 0, 17040, 26460, 43920, 59580, 76800]/3600.

img = figure(figsize=(4,4)) # figsize=(4,8)
plot(n,ct,'k-*',n,sf,'k-s')#,n[0],bt,'k-^')
xlim((47,71))
grid('on')
xlabel('Attributes')
ylabel('Time (Hrs)')
title('Density 48% and 255 rows')
legend(('CTH','CTS'), loc=2)
img.savefig('med48_density.eps')
