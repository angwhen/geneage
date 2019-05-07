import pickle
import csv

# TODO double check how to get age out of period
def get_age(period):
    total = 7.0
    if period == "Cellular_organisms":
        return 7/total
    if period == "Euk_Archaea":
        return 6/total
    if period == "Euk+Bac":
        return 5/total
    if period == "Eukaryota":
        return 4/total
    if period == "Opisthokonta":
        return 3/total
    if period == "Eumetazoa":
        return 2/total
    if period == "Vertebrata":
        return 1/total
    if period == "Mammalia":
        return 0/total
    return None


row_num_to_dataset_dict = {}
dataset_to_gene_to_age_dict = {}

with open('../data/binAges_HUMAN.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            for i in xrange(1,len(row)):
                dataset = row[i].strip()
                row_num_to_dataset_dict[i] = dataset
                dataset_to_gene_to_age_dict[dataset] = {}
        else:
            gene_name = row[0].strip()
            for i in xrange(1,len(row)):
                dataset = row_num_to_dataset_dict[i]
                dataset_to_gene_to_age_dict[dataset][gene_name] = get_age(row[i].strip())


#print dataset_to_gene_to_age_dict
pickle.dump(dataset_to_gene_to_age_dict, open("../data/dataset_to_gene_to_age_dict.p","wb"))  
            