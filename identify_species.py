#################################
#####   SPECIE DETECTION   ######
#################################


# This script only accepts decompressed txt and runs when called with commands_starlife.bash 


from dictionaries import *
import sys


# Load species dictionaries

reference_genomes = [
    (GRCh37, 'Homo Sapiens'),
    (GRCh38, 'Homo Sapiens'),
    (rCRS, 'Homo Sapiens'),
    (chrM_old, 'Homo Sapiens'),
    (hg18, 'Homo Sapiens'),
    (t2t, 'Homo Sapiens'),
    (mm7, 'Mus Musculus'),
    (mm8, 'Mus musculus'),
    (mm9, 'Mus musculus'),
    (mm10, 'Mus musculus'),
    (mm39, 'Mus musculus'),
    (dm5, 'Drosophila Melanogaster'),
    (dm6, 'Drosophila Melanogaster'),
    (danRer10, 'Danio Rerio'),
    (danRer11, 'Danio Rerio'),
    (WBcel215, 'Caenorhabditis elegans'),
    (WBcel235, 'Caenorhabditis elegans'),
    (mRatBN7_2, 'Rattus norvegicus'),
    (Rnor_6_0, 'Rattus norvegicues'),
    (R64, 'Saccharomyces cerevisiae'),
    (ASM886v2, 'Escherichia coli'),
    (ASM886v2, 'Escherichia Coli'),
    (pantro3_0, 'Pan troglodytes'),
    (pantro_2_1_4, 'Pan troglodytes'),
    (Mmul10, 'Macaca mulatta'),
    (rheMac8, 'Macaca mulatta'),
    (rheMac2, 'Macaca mulatta'),
    (TAIR, 'Arabidopsis thaliana')
]


def comparison(dict_SN_LN):
    if len(dict_SN_LN) == 0:
        print(sys.argv[2], "Incomplete header")
    else:
        max_match = (0, '')
        for ref_genome, species in reference_genomes:
            intersection_size = len(set(dict_SN_LN.values()).intersection(ref_genome.values()))
            if intersection_size > max_match[0]:
                max_match = (intersection_size, species)
        
        if max_match[0] == 0:
            print(sys.argv[2], "Unknown contigs")
        else:
            print(sys.argv[2], max_match[1])

        
def main():
    """ 
    process_data takes the headers in the txt one by one and creates a dictionary with the SN and LN fields.
    If the AS and md5 field is present and asked by the user, it prints them.
    """
    try:
        with open(sys.argv[1]) as header_reader:
            SQ = [line for line in header_reader if '@SQ' in line]  # creates a list with the SQ header lines
            SQ2= [i.split("\t") for i in SQ]
            dict_SN_LN = {line[1].replace('SN:', ''): int(line[2].replace('LN:', '')) for line in SQ2}  # we convert the
            # dictonary values to int, beacuse that's how we've constructed our collection of dictionaries
            comparison(dict_SN_LN)  # run the next f
    except OSError:
        print(sys.argv[2], "File can't be opened")

if __name__ == '__main__':  # the first executed function will be main()
    main()
