import pickle
import numpy as np
from matplotlib import pyplot as plt
import random
import seaborn as sns
import pandas as pd

# THIS IS VERY MESSY, SEE THE JUPYTER NOTEBOOK WITH SAME NAME instead

function_to_ages = pickle.load(open("data/function_to_age_simplified_dict.p","rb"))
function_list= []
mean_list = []
std_list = []
len_list = []

for func in function_to_ages:
    ages = np.array(function_to_ages[func])
    function_list.append(func)
    mean_list.append(np.mean(ages))
    std_list.append(np.std(ages))
    len_list.append(len(ages))

print min(len_list)

"""
plt.title("Standard Deviations of Age of Genes Assoc with Funcs")
plt.hist(std_list,bins=50,alpha=0.7)
plt.text(0,0,'Mean of stds is %.2f' %np.mean(std_list))
plt.savefig("figures/std_by_func_distrib.png")
plt.cla()

plt.title("Means of Age of Genes Assoc with Funcs")
plt.hist(mean_list,bins=50,alpha=0.7)
plt.text(0,0,'Mean of mean ages is %.2f' %np.mean(mean_list))

plt.savefig("figures/mean_by_func_distrib.png")
plt.cla()

plt.title("Number of Genes Assoc with Funcs")
plt.hist(len_list,bins=50,alpha=0.7)
plt.savefig("figures/num_genes_per_func_distrib.png")
plt.cla()
"""

gene_to_age_dict = pickle.load(open("data/gene_to_age_simplified_dict.p","rb"))
ages_list = []
for gene in gene_to_age_dict:
    ages_list.append(gene_to_age_dict[gene])

"""
# more efficient way to not redo same len, but data less good looking
mean_list = []
std_list = []
# make random age lists of len size and see that distrib
len_set = set(len_list)
print len(len_set)
for l in len_set: 
    curr_ages = random.sample(ages_list,l)
    m = np.mean(curr_ages)
    s = np.std(curr_ages)
    mean_list.extend([m for i in xrange(0,len_list.count(l))])
    std_list.extend([s for i in xrange(0,len_list.count(l))])
"""


rand_mean_list = []
rand_std_list = []
# make random age lists of len size and see that distrib

for l in len_list: 
    curr_ages = random.sample(ages_list,l)
    m = np.mean(curr_ages)
    s = np.std(curr_ages)
    rand_mean_list.append(m)
    rand_std_list.append(s)

"""
plt.title("Standard Deviations of Age of Random Chosen Genes")
plt.hist(rand_std_list,bins=50,alpha=0.7)
plt.text(0,0,'Mean of stds is %.2f' %np.mean(rand_std_list))

plt.savefig("figures/std_by_random_len_mult_distrib.png")
plt.cla()

plt.title("Means of Age of Random Chosen Genes")
plt.hist(rand_mean_list,bins=50,alpha=0.7)
plt.text(0,0,'Mean of mean ages is %.2f' %np.mean(rand_mean_list))

plt.savefig("figures/mean_by_random_len_mult_distrib.png")
plt.cla()

"""

"""
plt.title("Standard Deviations of Ages")
plt.hist(std_list,bins=50,alpha=0.5,color="blue",label="by function")
plt.hist(rand_std_list,bins=50,alpha=0.5,color="orange",label="random")
plt.legend(loc='upper left')
plt.text(0,0,'Mean func stds: %.2f, mean rand stds: %.2f' %(np.mean(std_list),np.mean(rand_std_list)), fontsize = 16)
plt.savefig("figures/std_by_func_and_rand_distrib.png")
plt.cla()

"""


len_dict_func_std_list = {}
len_dict_rand_std_list = {}

for i in xrange(0,len(std_list)):
    l = len_list[i]
    if l not in len_dict_func_std_list:
        len_dict_func_std_list[l] = []
        len_dict_rand_std_list[l] = []
    len_dict_func_std_list[l].append(std_list[i])
    len_dict_rand_std_list[l].append(rand_std_list[i])


len_func_stds = []
len_rand_stds = []
len_order_list = []
for l in len_dict_func_std_list:
    len_func_stds.append(np.mean(len_dict_func_std_list[l]))
    len_rand_stds.append(np.mean(len_dict_rand_std_list[l]))
    len_order_list.append(l)

"""
# PLOT SCATTER OF STDS FUNC GPED VS RAND GPED
fig, ax = plt.subplots()
ax.scatter(len_func_stds, len_rand_stds,  c="blue", alpha=0.5)
plt.title('Random vs Func Grouped Stds')
plt.xlabel('Function grouped stds')
plt.ylabel('Random grouped stds')

for i, txt in enumerate(len_order_list):
    ax.annotate(txt, (len_func_stds[i], len_rand_stds[i]),fontsize = 3)
plt.ylim(0.1,0.4)
plt.xlim(0.1,0.4)

plt.savefig("figures/scatter_std_by_rand_against_std_by_func_size_annot.png",dpi=800)

slope, intercept = np.polyfit(len_func_stds,len_rand_stds, 1)
print np.corrcoef(len_func_stds,len_rand_stds)
print slope, intercept

"""

"""
#PLOT OVERALL DISTRIBUTION OF GENE AGES
plt.hist(ages_list,bins=30,alpha=0.7)
plt.title("Overall distribution of Gene Ages")
plt.xlabel("Gene Age")
plt.savefig("figures/overall_distrib_gene_ages.png")
"""

#PLOT VIOLIN OF STDS GROUPED BY SET SIZE


"""
func_quartile_data = [[],[],[],[]] #list of arrays of func stds, grouped by set size
rand_quartile_data = [[],[],[],[]]


lq = np.percentile(len_list,25)
mq = np.percentile(len_list,50)
uq = np.percentile(len_list,75)

for l in len_dict_func_std_list:
    if l < lq:
        func_quartile_data[0].extend(len_dict_func_std_list[l])
        rand_quartile_data[0].extend(len_dict_rand_std_list[l])
    elif l < mq:
         func_quartile_data[1].extend(len_dict_func_std_list[l])
         rand_quartile_data[1].extend(len_dict_rand_std_list[l])
    elif l < uq:
        func_quartile_data[2].extend(len_dict_func_std_list[l])
        rand_quartile_data[2].extend(len_dict_rand_std_list[l])
    else:
        func_quartile_data[3].extend(len_dict_func_std_list[l])
        rand_quartile_data[3].extend(len_dict_rand_std_list[l])



all_data_to_plot = []
for i in xrange(0,4):
    all_data_to_plot.append(func_quartile_data[i])
    all_data_to_plot.append(rand_quartile_data[i])

ax = sns.violinplot(data=all_data_to_plot,palette = ["blue","orange","blue","orange","blue","orange","blue","orange"])
plt.show()
"""
lq = np.percentile(len_list,25)
mq = np.percentile(len_list,50)
uq = np.percentile(len_list,75)
print len_list

print lq,mq,uq
v_data = []
for l in len_dict_func_std_list:
    if l < lq:
        for s in len_dict_func_std_list[l]:
            v_data.append(["Less Than %d Genes"%lq,s,"Func"])
        for s in len_dict_rand_std_list[l]:
            v_data.append(["Less Than %d Genes"%lq,s,"Rand"])
    elif l < mq:
        for s in len_dict_func_std_list[l]:
            v_data.append(["Less Than %d Genes"%mq,s,"Func"])
        for s in len_dict_rand_std_list[l]:
            v_data.append(["Less Than %d Genes"%mq,s,"Rand"])
    elif l < uq:
        for s in len_dict_func_std_list[l]:
            v_data.append(["Less Than %d Genes"%uq,s,"Func"])
        for s in len_dict_rand_std_list[l]:
            v_data.append(["Less Than %d Genes"%uq,s,"Rand"])
    else:
        for s in len_dict_func_std_list[l]:
            v_data.append(["Largest Gene Sets",s,"Func"])
        for s in len_dict_rand_std_list[l]:
            v_data.append(["Largest Gene Sets",s,"Rand"])


v_df = pd.DataFrame(v_data,columns = ["GeneSet","Std","Type"])
sns.set_context("paper",font_scale = 0.8)
ax = sns.violinplot(x="GeneSet",y="Std",data=v_df,order = ["Less Than %d Genes"%lq,"Less Than %d Genes"%mq ,"Less Than %d Genes"%uq,"Largest Gene Sets"],hue="Type",palette="muted",split=True)
plt.savefig("figures/violinplot_of_stds_func_vs_rand.png",dpi=600)
