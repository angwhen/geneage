library(GOSemSim)
library(dplyr)

# X, FractionLDOs
ages <- read.csv("data/HUMAN_LDO_summary.csv",stringsAsFactors = FALSE) 
#genelist <-ages$X;


#https://www.bioconductor.org/packages/devel/bioc/vignettes/GOSemSim/inst/doc/GOSemSim.html
hsGO2 <- godata('org.Hs.eg.db', keytype = "UNIPROT", ont="MF");

simlist <- vector(mode="list", length=1000)
agedistlist <- vector(mode="list", length=1000)

i <- 1
while (i<=1000){
    #s<-sample(genelist,2);
    s <- sample_n(ages,2)
    sim <- geneSim(s$X[1],s$X[2], semData=hsGO2, measure="Wang");

    if(is.na(sim)){ #idk why this happens semi-often ...?
        next 
    }

    geneSim = sim$geneSim;
   
    simlist[[i]] <- geneSim
    agedistlist[[i]] <- abs(s$FractionLDO[1]-s$FractionLDO[2])
    #print(sprintf("similarity: %#.5f",sim$geneSim))
    i <- i+1
}

print (simlist)
print (agedistlist)
png("figures/temporal_vs_func_dist.png", width = 1500, height = 1500)
plot(simlist,agedistlist, main = "Temporal Distance vs Func Similarity (From GOSemSim)",
     xlab = "Function Similarity", ylab = "Temporal Distance",pch=19,
     col = "#2E9FDF", frame = FALSE)
dev.off()


# might be more efficient to use this to find gene sims, but need to figure out how to use the format
#print (mgeneSim(genelist,semData=hsGO2,measure="Wang",combine="BMA",verbose=FALSE))
