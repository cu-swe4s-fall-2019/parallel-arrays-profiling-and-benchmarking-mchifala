# Parallel Arrays Profiling and Benchmarking 
V1.0: The goal of this assignment is to use parallel arrays to analyze data as well as profile and benchmark different search algorithms (linear vs. binary). 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following packages were used during the development of this code. Other versions may be supported, but cannot be guaranteed.

- python (version 3.7.0)
- pycodestyle (version 2.5.0)
- matplotlib (version 3.1.1)

### Installation

The following steps will help you set up the proper environment on your machine. All example commands are entered directly into terminal.

**Installing conda:**

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

**Creating conda environment:**

```
conda create --yes -n <your_environment>
conda install --yes python=3.7
```

**Activating conda environment:**

```
conda activate <your_environment>
```

**Installing pycodestyle:**

pycodestyle is used to ensure that all .py files adhere to the PEP8 style guidelines.

```
conda install -y pycodestyle
```

**Installing matplotlib:**

matplotlib is used to generate the box plots of the data.

```
conda install -y pycodestyle
```

### Examples
plot_gtex.py processes the data in two user defined files and plots the gene expression distribution across tissue groups or tissue types for a target gene. The resulting boxplot is output to a file. The following example will create a multi-part boxplot for gene "ACTA2" and save it to the file "test.png"

```
python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene "ACTA2" --group_type SMTS --output_file test.png
```

test_search.py runs several unit tests on the linear and binary search methods in plot_gtex.py to test both accuracy and proper error handling.

```
python test_search.py
```

test_data_viz.py runs several unit tests on the box plotting functions in data_viz.py to test for the proper creation of the figure files.

```
python test_data_viz.py
```
### Profiling Results
The Cprofile results for the script when using linear_search method are included in plot_gtex_linear_search.txt. For the particular run which generated these results, there were 45,904 calls to the linear_search function taking a total of 16.143 seconds out of the 18.328 seconds required to fully execute the script.  

### Benchmarking Results
Including all data processing and creation of the resulting box plots, the time to run this script using linear_search method takes ~15 seconds on my machine/environment. The same process using binary_search method takes ~1.5 seconds. 

## Authors

**Michael W. Chifala** - University of Colorado, Boulder, CSCI 7000: Software Engineering for Scientists


## Acknowledgments

* Ryan Layer's CSCI 7000 "Development Environment" document
* Ryan Layer's CSCI 7000 "Continuous Integration with Travis CI" document
* Ryan Layer's CSCI 7000 "Test-Driven Development" document
* Ryan Layer's CSCI 7000 "Using libraries: Matplotlib" document
* PEP8 Style Guidelines: https://www.python.org/dev/peps/pep-0008/
* Github: PurpleBooth/README-Template.md
* Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

