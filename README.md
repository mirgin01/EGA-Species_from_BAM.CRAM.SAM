# EGA-Species_from_BAM.CRAM.SAM

Following the same principale as refgenDetector, this tool identifies the specie the file belongs thanks to the contig's information on the header of the file. 

List of the species that will be identified: 

1. Mouse (Mus musculus)
    
        - GRCm39 / mm39 (2020)
        - GRCm38 / mm10 (2012)
        - GRCm37 / mm9 (2010)
        - mm8 (2006)
        - mm7 (2005)

    Duplicated value: 16299 in mm8['chrM'] and mm7['chrM']
    Duplicated value: 16299 in mm9['chrM'] and mm7['chrM']
    Duplicated value: 206961 in mm10['chr1_GL456221_random'] and mm8['chr8_random']
    Duplicated value: 16299 in mm10['chrM'] and mm7['chrM']
    
    ****
    Possible issues with: 
        Duplicated value: 11753682 in rheMac8['chrY'] and Mmul10['Y']
        Duplicated value: 11753682 in rheMac3['chrY'] and Mmul10['Y']
    ****
       
2. Fruit fly (Drosophila melanogaster)

        - dm6 (2014)
        - dm5 (2000)

3. Zebrafish (Danio rerio)

        - danRer11 (2017)
        - danRer10 (2014)
        
4. Nematode worm (Caenorhabditis elegans)

        - WBcel235 (2013)
        - WBcel215 (2012)

5. Rat (Rattus norvegicus)

        - mRatBN7.2 (2020)
        - Rnor_6.0 (2014)

6. Yeast (Saccharomyces cerevisiae)

        - R64 (2014) 
        
7. Arabidopsis (Arabidopsis thaliana) 

        - Col-XJTU (2022 - couldn't find it)
        - TAIR (2018)
        
8. Escherichia coli (E. coli) 

        - ASM584v2 (2013)
        - ASM886v2 (2018)
        
## The reference for macaque genomes is Indian rhesus (macaca mulatta) : 
## https://genomebiology.biomedcentral.com/articles/10.1186/gb-2012-13-7-r58
## https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8742695/

9. Pan troglodytes

        - Pan_tro 3.0 (2016)
        - Pan_troglodytes-2.1.4 (2011)
        - Pan_troglodytes-2.1.3 (2010)

    Duplicated value: 228333871 in pantro_2_1_4['1'] and pantro2_1_3['1']
    Duplicated value: 113622374 in pantro_2_1_4['2A'] and pantro2_1_3['2A']
    Duplicated value: 247518478 in pantro_2_1_4['2B'] and pantro2_1_3['2B']
    Duplicated value: 202329955 in pantro_2_1_4['3'] and pantro2_1_3['3']
    Duplicated value: 193495092 in pantro_2_1_4['4'] and pantro2_1_3['4']
    Duplicated value: 182651097 in pantro_2_1_4['5'] and pantro2_1_3['5']
    Duplicated value: 172623881 in pantro_2_1_4['6'] and pantro2_1_3['6']
    Duplicated value: 161824586 in pantro_2_1_4['7'] and pantro2_1_3['7']
    Duplicated value: 143986469 in pantro_2_1_4['8'] and pantro2_1_3['8']
    Duplicated value: 137840987 in pantro_2_1_4['9'] and pantro2_1_3['9']
    Duplicated value: 133524379 in pantro_2_1_4['10'] and pantro2_1_3['10']
    Duplicated value: 133121534 in pantro_2_1_4['11'] and pantro2_1_3['11']
    Duplicated value: 134246214 in pantro_2_1_4['12'] and pantro2_1_3['12']
    Duplicated value: 115123233 in pantro_2_1_4['13'] and pantro2_1_3['13']
    Duplicated value: 106544938 in pantro_2_1_4['14'] and pantro2_1_3['14']
    Duplicated value: 99548318 in pantro_2_1_4['15'] and pantro2_1_3['15']
    Duplicated value: 89983829 in pantro_2_1_4['16'] and pantro2_1_3['16']
    Duplicated value: 82630442 in pantro_2_1_4['17'] and pantro2_1_3['17']
    Duplicated value: 76611499 in pantro_2_1_4['18'] and pantro2_1_3['18']
    Duplicated value: 63644993 in pantro_2_1_4['19'] and pantro2_1_3['19']
    Duplicated value: 61729293 in pantro_2_1_4['20'] and pantro2_1_3['20']
    Duplicated value: 32799110 in pantro_2_1_4['21'] and pantro2_1_3['21']
    Duplicated value: 49737984 in pantro_2_1_4['22'] and pantro2_1_3['22']
    Duplicated value: 156848144 in pantro_2_1_4['X'] and pantro2_1_3['X']
    Duplicated value: 23952694 in pantro_2_1_4['Y'] and pantro2_1_3['Y']
   
    --> As we are not interested in finding the exact reference genome used only the 2011 data will be included in the code
        
10. Macaca mulatta

        - Mmul_10 (2019)  
        - rheMac8 (2015)
        - rheMac3 (2010)
        - rheMac2 (2006)
        
    Duplicated value: 225584828 in rheMac3['chr1'] and rheMac8['chr1']
    Duplicated value: 204787373 in rheMac3['chr2'] and rheMac8['chr2']
    Duplicated value: 190429646 in rheMac3['chr5'] and rheMac8['chr5']
    Duplicated value: 185818997 in rheMac3['chr3'] and rheMac8['chr3']
    Duplicated value: 180051392 in rheMac3['chr6'] and rheMac8['chr6']
    Duplicated value: 172585720 in rheMac3['chr4'] and rheMac8['chr4']
    Duplicated value: 169600520 in rheMac3['chr7'] and rheMac8['chr7']
    Duplicated value: 149150640 in rheMac3['chrX'] and rheMac8['chrX']
    Duplicated value: 144306982 in rheMac3['chr8'] and rheMac8['chr8']
    Duplicated value: 133663169 in rheMac3['chr11'] and rheMac8['chr11']
    Duplicated value: 129882849 in rheMac3['chr9'] and rheMac8['chr9']
    Duplicated value: 127894412 in rheMac3['chr14'] and rheMac8['chr14']
    Duplicated value: 125506784 in rheMac3['chr12'] and rheMac8['chr12']
    Duplicated value: 111343173 in rheMac3['chr15'] and rheMac8['chr15']
    Duplicated value: 108979918 in rheMac3['chr13'] and rheMac8['chr13']
    Duplicated value: 95684472 in rheMac3['chr17'] and rheMac8['chr17']
    Duplicated value: 92844088 in rheMac3['chr10'] and rheMac8['chr10']
    Duplicated value: 77216781 in rheMac3['chr16'] and rheMac8['chr16']
    Duplicated value: 74971481 in rheMac3['chr20'] and rheMac8['chr20']
    Duplicated value: 70235451 in rheMac3['chr18'] and rheMac8['chr18']
    Duplicated value: 53671032 in rheMac3['chr19'] and rheMac8['chr19']
    
    --> As we are not interested in finding the exact reference genome used only the 2015 data will be included in the code
              
11. Macaca fascicularis

        - MFA1912RKSv2 (2021)
        - MFA1912RKS (2020)

