#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

units_folder = "BM1000x30_out"
table_fname  = "BM1000x30.csv"

ofiles = commands.getoutput('ls '+units_folder).split('\n')

odir = {}

def processFile(fname):
   f = file(units_folder+"/"+fname,'r')
   lineas = f.readlines()
   f.close()
   sptname        = fname.split('_')
   bm             = sptname[0]+'_'+sptname[1]+'_'+sptname[2]+'.txt'
   alg            = sptname[3]
   time_ms        = int(lineas[1].split(':')[1].split('ms')[0])
   reducts        = int(lineas[2].split(':')[1])
   super_reducts  = int(lineas[3].split(':')[1])
   candidates     = int(lineas[4].split(':')[1])
   
   #print bm
   #print alg
   #print time_ms
   #print reducts
   #print super_reducts
   #print candidates
   
   # Store data
   if odir.has_key(bm):
      if reducts != odir[bm]['reducts']:
         print 'Error in number of reducts: '+bm+', '+alg
      else:
         if odir[bm].has_key(alg):
            odir[bm][alg]['runtimes'].append(time_ms)
         else:
            odir[bm].setdefault(alg,{'candidates':candidates,'testors':super_reducts,'runtimes':[time_ms]})
   else:
      odir.setdefault(bm,{'reducts':reducts})
      odir[bm].setdefault(alg,{'candidates':candidates,'testors':super_reducts,'runtimes':[time_ms]})

# Process the list
for of in ofiles:
   processFile(of)

# Load Table
f = file(table_fname,'r')
lineas = f.readlines()
f.close()

algs = ["fastBR","gapCText"]
# Save data
f = file(table_fname.split('.')[0]+'_out.cvs','w')
f.write('Name,Density,MinCol,MaxCol,StdCol,MinRow,MaxRow,StdRow,reducts,BR_time,BR_cand,GAP_time,GAP_cand,faster\n')
for linea in lineas[1:]:
   bm = linea.split(',')[0]
   record = odir[bm]
   str_add = str(odir[bm]['reducts'])+','
   f.write(linea[:-1]+',')
   # Add new data
   min_time = 2**30
   for alg in algs:
      data = record[alg]
      data['runtimes'].sort()
      ltime = data['runtimes'][0]
      if ltime < min_time:
         faster = alg
         min_time = ltime
      str_add += str(ltime)+',' # Select the lowest runtime
      str_add += str(data['candidates'])+','
   # End line
   str_add += faster
   f.write(str_add+'\n')
f.close()
