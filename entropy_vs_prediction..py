import pickle
import numpy as np
from matplotlib import pyplot as plt
import random
import sys
import seaborn as sns
import pandas as pd
from scipy import stats
import os
import prelim_fig_funcs
import csv

# import the main_HUMAN_csv
# for all the genes in HUMAN_LDO_summary.csv 
# match them to their entropy value
# group by entropy
# make correlation charts based on entropy

#duplicate code from save_function_to_age_pickle.py TODO: clean up
def get_function_to_age_dict(gene_to_age_dict,function_to_genes_dict):
    function_to_age_dict = {}
    for func in function_to_genes_dict:
        if func == "Term": #TODO: understand why some bad data sometimes
            continue 
        # TODO: make robust against functions with genes not given in dataset
        genes = function_to_genes_dict[func.strip()]
        ages = list(map(lambda x: gene_to_age_dict[x.strip()] , genes)) 
        function_to_age_dict[func] = ages
    print function_to_age_dict
    return function_to_age_dict


function_to_genes = pickle.load(open("data/function_to_genes_all_in_simplified.p","rb"))
genes_to_age = pickle.load(open("data/gene_to_age_simplified_dict.p","rb"))

exists = os.path.isfile('/data/gene_to_entropy_dict.p')
if not exists:
    gene_to_entropy_dict = {} # has more genes than we generally have other datas for

    with open('data/main_HUMAN.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                gene_name = row[0].strip()
                gene_to_entropy_dict[gene_name] = float(row[12].strip())
    pickle.dump(gene_to_entropy_dict , open("data/genes_to_entropy_dict.p","wb"))
else:
    gene_to_entropy_dict =  pickle.load(open("data/genes_to_entropy_dict.p","rb"))


# sort genes by four groups of entropy
entropy_list = []
gene_list = []
for g in gene_to_entropy_dict:
    if g in genes_to_age.keys():
        entropy_list.append(gene_to_entropy_dict[g])
        gene_list.append(g)

lq = np.percentile(entropy_list,25)
mq = np.percentile(entropy_list,50)
uq = np.percentile(entropy_list,75)


function_to_entropy_dict = get_function_to_age_dict(gene_to_entropy_dict,function_to_genes)



