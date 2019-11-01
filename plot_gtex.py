import sys  # noqa: E402
sys.path.insert(1, "hash-tables-mchifala")  # noqa: E402
import argparse  # noqa: E402
import gzip  # noqa: E402
import time  # noqa: E402
from data_viz import boxplot  # noqa: E402
from hash_tables import ChainedHash  # noqa: E402
from hash_functions import h_rolling  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use('Agg')  # noqa: E402


def linear_search(key, data_list):
    """
    This function linearly searches for a key in a list of data
    and returns the index of the key if it is found or -1 if it is not.

    Parameters:
    - key(int or str): The item we are looking for
    - data_list(list): A list of data

    Returns:
    - The index of the key in the list or -1

    """
    for i in range(len(data_list)):
        if key == data_list[i]:
            return i
    return -1


def binary_search(key, sorted_data_list):
    """
    This function uses binary search for a key in a sorted list of data
    and returns the index of the key if it is found or -1 if it is not.
    Parameters:
    - key(int or str): The item we are looking for
    - data_list(list): A sorted list of data
    Returns:
    - The index of the key in the sorted list or -1
    """
    lo = -1
    hi = len(sorted_data_list)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == sorted_data_list[mid][0]:
            return sorted_data_list[mid][1]

        try:
            if (key < sorted_data_list[mid][0]):
                hi = mid
            else:
                lo = mid

        except TypeError as inst:
            print("Run-Time Error:", type(inst))
            sys.exit(1)

    return -1


def hash_process(gene_reads, sample_attributes, gene,
                 group_types, output_file):
    """
    This function calculates the gene expression distribution across either
    tissue groups (SMTS) or tissue type (SMTSD) for a target gene. It uses
    hash tables for O(1) lookups. A series of box plots is generated.

    Parameters:
    - gene_reads: (see next line)
    GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
    - sample_attributes: GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
    - gene: The target gene
    - group_types: Tissue group or type
    - output_file: File for saving the box plot (.png)

    """
    sample_id_col_name = 'SAMPID'
    sample_info_header = None

    # Initialize tissue-sample hash table
    h_table_samples = ChainedHash(1000, h_rolling)

    # Read and preprocess the data lines
    for line in open(sample_attributes):
        if sample_info_header is None:
            sample_info_header = line.rstrip().split('\t')

    # Find the proper columns containing the group types and sample id's
    # using linear search
            group_col_idx = linear_search(group_types, sample_info_header)
            sample_id_col_idx = linear_search(sample_id_col_name,
                                              sample_info_header)

    # Add samples to hash table
        else:
            line = line.rstrip().split('\t')
            group = line[group_col_idx]
            sample = line[sample_id_col_idx]
            h_table_samples.add(key=group, value=sample)

    version = None
    dim = None
    data_header = None
    gene_name_col = 1

    # Initialize sample-count hash table
    h_table_counts = ChainedHash(100000, h_rolling)

    # Read and preprocess the gene reads data lines
    for line in gzip.open(gene_reads, 'rt'):
        if version is None:
            version = line
            continue

        if dim is None:
            dim = [int(x) for x in line.rstrip().split()]
            continue

        if data_header is None:
            data_header = line.rstrip().split('\t')
            continue

        line = line.rstrip().split('\t')
        if line[gene_name_col] == gene:
            gene_row = line

    for sample, count in zip(data_header, gene_row):
        h_table_counts.add(sample, count)

    # Get the counts for each sample of each tissue type
    group_counts = []
    for tissue in h_table_samples.keys:
        counts = []
        for sample in h_table_samples.search(tissue):
            count = h_table_counts.search(sample)
            if count is not None:
                counts.append(int(count[0]))
        group_counts.append(counts)

    # Generate box plot
    boxplot(group_counts, h_table_samples.keys, gene, group_types,
            "Gene read counts", output_file)


def main(gene_reads, sample_attributes, gene, group_types, output_file):
    """
    This function benchmarks the hash_process and demonstrates
    the speed improvement of using hash tables over linear or binary search.

     Parameters:
    - gene_reads: (see next line)
    GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz
    - sample_attributes: GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
    - gene: The target gene
    - group_types: Tissue group or type
    - output_file: File for saving the box plot (.png)

    Returns:
    - None; the total runtimes for each function is printed.

    """
    t0_hash = time.time()
    hash_process(gene_reads, sample_attributes, gene,
                 group_types, output_file)
    t1_hash = time.time()
    print("Hashing Total Time:", t1_hash-t0_hash)


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
