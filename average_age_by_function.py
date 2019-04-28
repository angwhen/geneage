import pickle

gene_to_age_simplified_dict = {}
f = open("data/HUMAN_LDO_summary.csv","r")
first = True
for line in f:
    if first:
        first = False
        continue
    gene_to_age_simplified_dict[line.split(",")[0]] = float(line.split(",")[1])

pickle.dump(gene_to_age_simplified_dict,open("data/gene_to_age_simplified_dict.p","wb"))

function_to_genes_dict = pickle.load(open("data/function_to_genes_all_in_simplified.p","rb"))

function_to_age_dict = {}

for func in function_to_genes_dict:
    genes = function_to_genes_dict[func]
    ages = list(map(lambda x: gene_to_age_simplified_dict[x] , genes)) 
    function_to_age_dict[func] = ages
    print func
    print ages

print function_to_age_dict 

pickle.dump(function_to_age_dict,open("data/function_to_age_simplified_dict.p","wb"))

