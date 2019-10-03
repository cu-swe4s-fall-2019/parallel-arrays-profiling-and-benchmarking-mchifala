import argparse
import gzip
import sys
import matplotlib
matplotlib.use('Agg')
from data_viz import boxplot

def linear_search(key, data_list):
    hit = -1
    for i  in range(len(data_list)):
        curr =  data_list[i]
        if key == curr:
            return i
    return -1

def binary_search(key, sorted_data_list):
    lo = -1
    hi = len(sorted_data_list)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == sorted_data_list[mid][0]:
            return sorted_data_list[mid][1]
        
        try:
            if ( key < sorted_data_list[mid][0] ):
                hi = mid
            else:
                lo = mid
                
        except TypeError as inst:
            print("Run-Time Error:", type(inst))
            sys.exit(1)

    return -1

def linear_process(gene_reads, sample_attributes, gene, group_types, output_file):
    sample_id_col_name = 'SAMPID'
    samples = []
    sample_info_header = None
    for l in open(sample_attributes):
        if sample_info_header == None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))
            
    group_col_idx = linear_search(group_types, sample_info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)
    
    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)
        
    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [ [] for i in range(len(groups)) ]

    for l in gzip.open(gene_reads, 'rt'):
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header == None:
            data_header = l.rstrip().split('\t')
            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = linear_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break 
             
    boxplot(group_counts, groups, gene, group_types, "Gene read counts", output_file)
    
#def binary_process():
    
def main(gene_reads, sample_attributes, gene, group_types, output_file):
    
    linear_process(gene_reads, sample_attributes, gene, group_types, output_file)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GTEX analysis input")

    parser.add_argument('--gene_reads',
                        type=str,
                        help='Name of .gz file containing genes',
                        required=True)

    parser.add_argument('--sample_attributes',
                        type=str,
                        help='Name of.txt file containing sample attributes',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='Gene of interest',
                        required=True)
    
    parser.add_argument('--group_type',
                        type=str,
                        help='Gene group of interest',
                        required=True)
    
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of output file for boxplot',
                        required=True)

    args = parser.parse_args()
    main(args.gene_reads, args.sample_attributes, args.gene,
         args.group_type, args.output_file)
