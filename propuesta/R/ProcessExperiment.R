
Dataset <- read.table("/home/bill/Documents/Ciencia/mexico/reducts/softwares/BMgenerator/BM2000x30_out1.csv", 
  header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

postscript("/home/bill/Documents/Ciencia/mexico/reducts/softwares/BMgenerator/scatter_density.eps", 
horizontal=FALSE, onefile=FALSE,height=4, width=4, pointsize=10)

scatterplot(BestTime/1000~Density | faster, reg.line=FALSE, smooth=FALSE, spread=FALSE, boxplots=FALSE, 
by.groups=TRUE, data=Dataset, ylab="Best runtime (s)", main="Execution runtime vs. density of 1's",
legend.title="Fastest algorithm",legend.coords="topright")

dev.off()

postscript("/home/bill/Documents/Ciencia/mexico/reducts/softwares/BMgenerator/scatter_CTvsGAP.eps", 
horizontal=FALSE, onefile=FALSE,height=4, width=4, pointsize=10)

a<-Dataset$GAP_time/1000

scatterplot((CT_time/1000)~a | faster, reg.line=FALSE, smooth=FALSE, spread=FALSE,legend.coords="topleft",
  boxplots=FALSE, span=0.5, by.groups=FALSE, data=Dataset, main="CT_EXT vs. GCSDM",xlab="GCSDM runtime (s)",
  ylab="CT_EXT runtime (s)",legend.title="Fastest algorithm")

dev.off()

postscript("/home/bill/Documents/Ciencia/mexico/reducts/softwares/BMgenerator/runtimeReducts.eps", 
horizontal=FALSE, onefile=FALSE,height=4, width=4, pointsize=10)

scatterplot(BestTime/1000~reducts | faster, reg.line=FALSE, smooth=FALSE, spread=FALSE, boxplots=FALSE, 
	    by.groups=TRUE, data=Dataset, main="Execution runtime vs. the number of reducts",
	    xlab="Reducts", ylab="Best runtime (s)",legend.title="Fastest algorithm",
	    legend.coords="topleft")

dev.off()

postscript("/home/bill/Documents/Ciencia/mexico/reducts/softwares/BMgenerator/scatter_std.eps", 
horizontal=FALSE, onefile=FALSE,height=4, width=4, pointsize=10)

scatterplot(BestTime/1000~StdRow | faster, reg.line=FALSE, smooth=FALSE, spread=FALSE, boxplots=FALSE, 
by.groups=TRUE, data=Dataset, ylab="Best runtime (s)", main="Execution runtime vs. std of density in rows",
legend.title="Fastest algorithm",legend.coords="topright",xlab="Standard deviation of density in rows")

dev.off()

t.test(Dataset$CT_time, Dataset$GAP_time, alternative='greater', conf.level=.95, paired=TRUE)

