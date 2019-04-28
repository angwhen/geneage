import csv
import pickle

d = pickle.load(open("../data/function_to_genes_all_in_simplified.p","rb"))

f = open("../data/function_to_genes_all_in_simplified.txt","w")
for key,val in d.iteritems():
    f.write("%s\t"%key)
    for v in val:
        f.write("%s\t"%v)
    f.write("\n")

f.close()
