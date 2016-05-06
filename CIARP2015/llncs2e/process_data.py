from pylab import *
import csv

density = []
reducts = []
ct = []
gap = []
br = []
min1s = []
max1s = []

with open('BM2000x30_1_out2.csv', 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      density.append(float(row['Density']))
      reducts.append(float(row['reducts']))
      ct.append(float(row['CT_time'])/1000)
      gap.append(float(row['GAP_time'])/1000)
      br.append(float(row['BR_time'])/1000)

density = array(density)
reducts = array(reducts)
ct = array(ct)
gap = array(gap)
br = array(br)

# Ratios
BRoverGAP = divide(br,gap)
CToverGAP = divide(ct,gap)

# Create reducts beans
nbeans = 15
maxdens = max(reducts)
mindens = min(reducts)
delta = (maxdens - mindens)/(nbeans+1)
bins = linspace(mindens+delta, maxdens, nbeans)
reducts_discrete = digitize(reducts, bins)

red_mean      = []
ct_mean        = []
ct_std         = []
gap_mean       = []
gap_std        = []
br_mean        = []
br_std         = []
BRoverGAP_mean = []
BRoverGAP_std  = []
CToverGAP_mean = []
CToverGAP_std  = []

for i in range(0,len(bins)):
   red_mean.append(reducts[reducts_discrete==i].mean())
   ct_mean.append(ct[reducts_discrete==i].mean())
   ct_std.append(ct[reducts_discrete==i].std())
   gap_mean.append(gap[reducts_discrete==i].mean())
   gap_std.append(gap[reducts_discrete==i].std())
   br_mean.append(br[reducts_discrete==i].mean())
   br_std.append(br[reducts_discrete==i].std())
   BRoverGAP_mean.append(BRoverGAP[reducts_discrete==i].mean())
   BRoverGAP_std.append(BRoverGAP[reducts_discrete==i].std())
   CToverGAP_mean.append(CToverGAP[reducts_discrete==i].mean())
   CToverGAP_std.append(CToverGAP[reducts_discrete==i].std())

# Plot overall performance
# Use central value in x instead of mean
x = linspace(mindens+delta/2,maxdens-delta/2,nbeans)/1000
img = figure(figsize=(6,4))
errorbar(x,gap_mean,yerr=gap_std,fmt='o-')
#errorbar(x,ct_mean,yerr=ct_std,fmt='^-')
errorbar(x,br_mean,yerr=br_std,fmt='s-')
#plot(x,gap_mean,'o-',x,br_mean,'s-')
xlabels = ['%i'% int(i) for i in x]
xticks(x, xlabels, rotation=30)
ylim(ymin=0)
grid('on')
xlabel('Mean number of reducts (x1000)')
ylabel('Runtime (s)')
title('Runtime vs. number of reducts')
legend(('fast-CT_EXT','fast-BR'), loc=1)
subplots_adjust(bottom=0.15)
#show()
img.savefig('runtime_vs_reducts.eps')

##################################################################################
# Create density beans
nbeans = 16
maxdens = max(density)
mindens = min(density)
delta = (maxdens - mindens)/(nbeans+1)
bins = linspace(mindens+delta, maxdens, nbeans)
digitized = digitize(density, bins)

dens_mean      = []
ct_mean        = []
ct_std         = []
gap_mean       = []
gap_std        = []
br_mean        = []
br_std         = []
BRoverGAP_mean = []
BRoverGAP_std  = []
CToverGAP_mean = []
CToverGAP_std  = []

for i in range(1,len(bins)):
   dens_mean.append(density[digitized==i].mean())
   ct_mean.append(ct[digitized==i].mean())
   ct_std.append(ct[digitized==i].std())
   gap_mean.append(gap[digitized==i].mean())
   gap_std.append(gap[digitized==i].std())
   br_mean.append(br[digitized==i].mean())
   br_std.append(br[digitized==i].std())
   BRoverGAP_mean.append(BRoverGAP[digitized==i].mean())
   BRoverGAP_std.append(BRoverGAP[digitized==i].std())
   CToverGAP_mean.append(CToverGAP[digitized==i].mean())
   CToverGAP_std.append(CToverGAP[digitized==i].std())

## Plot BR over GCreduct runtime ratio
#img = figure(figsize=(6,6))
#ax=axes()
#rc('text', usetex=True)
#ax.set_yscale("log", nonposy='clip')
#ylim(ymin=0.2,ymax=20)
#errorbar(dens_mean,BRoverGAP_mean,yerr=BRoverGAP_std,fmt='o-')
#grid('on')
#xlabel('Mean density of 1\'s')
#ylabel(r"$t_{\mathrm {fast-BR}}/t_{\mathrm GCreduct}$",fontsize=16)
#title('Runtime ratio vs. density of 1\'s')
#img.savefig('BRoverGC')

## Plot CText over GCreduct runtime ratio
#img = figure(figsize=(6,6))
#ax=axes()
#rc('text', usetex=True)
#ax.set_yscale("log", nonposy='clip')
#ylim(ymin=0.9,ymax=10)
#errorbar(dens_mean,CToverGAP_mean,yerr=CToverGAP_std,fmt='o-')
#grid('on')
#xlabel('Mean density of 1\'s')
#ylabel(r"$t_{\mathrm {fast-CT\_EXT}}/t_{\mathrm GCreduct}$",fontsize=16)
#title('Runtime ratio vs. density of 1\'s')
#img.savefig('CToverGC')

# Plot overall performance
# Use central value in x instead of mean
x = linspace(0.22,0.78,15)
img = figure(figsize=(6,4))
errorbar(x,gap_mean,yerr=gap_std,fmt='o-')
#errorbar(x,ct_mean,yerr=ct_std,fmt='^-')
errorbar(x,br_mean,yerr=br_std,fmt='s-')
xlabels = ['%.2f'%i for i in x]
xticks(x, xlabels, rotation=60)
ylim(ymin=0)
grid('on')
xlabel('Mean density of 1\'s')
ylabel('Runtime (s)')
title('Runtime vs. density of 1\'s')
legend(('fast-CT_EXT','fast-BR'), loc=1)
subplots_adjust(bottom=0.15)
#show()
img.savefig('2000x30.eps')
