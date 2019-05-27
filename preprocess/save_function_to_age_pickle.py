import pickle



def get_function_to_age_dict(gene_to_age_dict,function_to_genes_dict):
    function_to_age_dict = {}
    for func in function_to_genes_dict:
        if func == "Term": #TODO: understand why some bad data sometimes
            continue 
        # TODO: make robust against functions with genes not given in dataset
        genes = function_to_genes_dict[func.strip()]
        ages = list(map(lambda x: gene_to_age_dict[x.strip()] , genes)) 
        function_to_age_dict[func] = ages
    #print function_to_age_dict
    return function_to_age_dict

function_to_genes_dict = pickle.load(open("../data/function_to_genes_all_in_simplified.p","rb"))

# for data from multiple datasets
"""dataset_to_gene_to_age_dict = pickle.load(open("../data/dataset_to_gene_to_age_dict.p","rb"))  
for dataset in dataset_to_gene_to_age_dict:
    gene_to_age_dict = dataset_to_gene_to_age_dict[dataset]
    function_to_age_dict = get_function_to_age_dict(gene_to_age_dict, function_to_genes_dict)
    pickle.dump(function_to_age_dict,open("../data/function_to_age_%s_dict.p"%dataset,"wb"))
"""

# for simplified data

gene_to_age_simplified_dict = pickle.load(open("../data/gene_to_age_simplified_dict.p","rb"))
function_to_age_dict = get_function_to_age_dict(gene_to_age_simplified_dict, function_to_genes_dict)
#print function_to_age_dict 
pickle.dump(function_to_age_dict,open("../data/function_to_age_simplified_dict.p","wb")
