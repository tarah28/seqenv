"""
==============================
Test the matrix multiplication
==============================
"""

# Modules #
import os, inspect
from seqenv import Analysis

# Constants #
current_script = inspect.getframeinfo(inspect.currentframe()).filename
current_dir = os.path.dirname(os.path.abspath(current_script)) + '/'
samples_dir =  current_dir + "../examples/samples/"
fasta = samples_dir + "community.fasta"
abund = samples_dir + "abundances.tsv"
out_dir = samples_dir + 'output/'

################################################################################
analysis = Analysis(fasta, out_dir=out_dir, abundances=abund, N=10)

df1 = analysis.outputs.df_seqs_concepts.rename(analysis.concept_to_name)
df2 = analysis.df_abundances
print set(df1.columns) ^ set(df2.index)

df2 = df2.loc[df1.columns]
print set(df1.columns) ^ set(df2.index)

df1.dot(df2)