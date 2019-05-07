import pickle
import numpy as np
from matplotlib import pyplot as plt
import random
import sys
import seaborn as sns
import pandas as pd


def get_function_grouped_age_data(function_to_ages):
    function_list = []
    mean_list = []
    std_list = []
    len_list = []
    
    for func in function_to_ages:
        ages = np.array(function_to_ages[func])
        #remove Nones
        ages = ages[ages != np.array(None)]
        if len(ages) == 0:
            continue
        function_list.append(func)
        mean_list.append(np.mean(ages))
        std_list.append(np.std(ages))
        len_list.append(len(ages))

    return function_list, mean_list, std_list, len_list

def get_random_grouped_age_data(len_list,ages_list):
    rand_mean_list = []
    rand_std_list = []
    for l in len_list: 
        curr_ages = random.sample(ages_list,l)
        m = np.mean(curr_ages)
        s = np.std(curr_ages)
        rand_mean_list.append(m)
        rand_std_list.append(s)
    return rand_mean_list, rand_std_list
        

def figure1(ax,len_list,std_list,rand_std_list):
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
    ax.set_ylim(ymin=0, ymax=0.5)
    ax.set_xlim(xmin=0,xmax=0.5)
    ax.scatter(len_func_stds, len_rand_stds,  s=2, c="blue", alpha=0.5)
   

def figure2(ax,std_list, rand_std_list):

    ax.hist(std_list,bins=50,alpha=0.5,color="blue",label="by function")
    ax.hist(rand_std_list,bins=50,alpha=0.5,color="orange",label="random")

def figure4(ax,len_list,std_list,rand_std_list):
    #PLOT VIOLIN OF STDS GROUPED BY SET SIZE
    lq = np.percentile(len_list,25)
    mq = np.percentile(len_list,50)
    uq = np.percentile(len_list,75)
    

    #duplicate code here TODO clean up
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


    v_data = []
    for l in len_dict_func_std_list:
        if l < lq:
            for s in len_dict_func_std_list[l]:
                v_data.append(["<%d"%lq,s,"Func"])
            for s in len_dict_rand_std_list[l]:
                v_data.append(["<%d"%lq,s,"Rand"])
        elif l < mq:
            for s in len_dict_func_std_list[l]:
                v_data.append(["<%d"%mq,s,"Func"])
            for s in len_dict_rand_std_list[l]:
                v_data.append(["<%d"%mq,s,"Rand"])
        elif l < uq:
            for s in len_dict_func_std_list[l]:
                v_data.append(["<%d"%uq,s,"Func"])
            for s in len_dict_rand_std_list[l]:
                v_data.append(["<%d"%uq,s,"Rand"])
        else:
            for s in len_dict_func_std_list[l]:
                v_data.append(["Largest",s,"Func"])
            for s in len_dict_rand_std_list[l]:
                v_data.append(["Largest",s,"Rand"])

    v_df = pd.DataFrame(v_data,columns = ["GeneSet","Std","Type"])
    sns.violinplot(x="GeneSet",y="Std",data=v_df,ax=ax, order = ["<%d"%lq,"<%d"%mq ,"<%d"%uq,"Largest"],hue="Type",palette="muted",split=True,legend=False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, rotation_mode="anchor")