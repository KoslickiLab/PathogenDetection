## Add VFDB and AMR to the graph

More refs:

1. Benchmark of different VF database: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3411817/
2. PATRIC curated VFDB for infectious disease: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4287947/
3. AMR data:
   1. PATRIC has an AMR phenotype table generated by laboratory methods. This table contains records like `32002.4 tiamulin` but NO AMR gene sequences. These records may serve as gold standard training data. 
   2. PATRIC also curated AMR genes mainly from CARD
   3. PATRIC has an AMR genome sets by antibiotic-resistant or suseptible category. But not what we need here.



Data location:

```
### Local at CPU server:
/scratch2/sml6467/temp/VFDB
/scratch2/sml6467/temp/AMR

### in our graph folder
/data/shared_data/metagenomics_graph/pathogen_database/VFDB
/data/shared_data/metagenomics_graph/pathogen_database/AMR
```











### VFDB

---

Download data from [VFDB ](http://www.mgc.ac.cn/VFs/download.htm)or from the curated VFDB in PATRIC FTB site (FTP -> specialty genes -> refDB). Record number:

| PATRIC curated | PATRIC_VFDB | VFDB_core | VFDB_full |
| -------------- | ----------- | --------- | --------- |
| 1570           | 2595        | **4236**  | 27982     |

It seems like the PATRIC VFDB is not up to date and it specifically focuses on some diseases (see ref2 above). So I think we should use the VFDB_core data.



There are 6 files:

1. an excel explaining each VF 
2. a comparative table for VF within a bacteria group (we don't need this)
3. DNA + **Protein** sequence for **core datasets** (representative genes associated with experimentally verified VFs only)
4. DNA + **Protein** sequence for **full datasets** (all genes related to known and predicted VFs)



Use these codes to download files:

```
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setA_nt.fas.gz
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setA_pro.fas.gz
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setB_nt.fas.gz
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setB_pro.fas.gz

# manually transfer the excel to csv file
# wget http://www.mgc.ac.cn/VFs/Down/VFs.xls.gz
```

File information:

| Name              | Contents                                             |
| ----------------- | ---------------------------------------------------- |
| VFs.csv           | Information file with VFID, name, category, function |
| VFDB_setA_nt.fas  | DNA of sub-unit of each VF for core data             |
| VFDB_setA_pro.fas | Protein of sub-unit of each VF for core data         |
| VFDB_setB_nt.fas  | DNA of sub-unit of each VF for full data             |
| VFDB_setB_pro.fas | Protein of sub-unit of each VF for full data         |



#### Final files for graph building:

Structure in graph: VFID <-> several sub-unites <-> genome

1. VFDB_setA_pro.fas: protein sequences for core datasets. 
   1. VF id in the middle paranthesis, e.g. Phospholipase C (**VF0470**) - Exotoxin (VFC0235)
   2. every record is a **SUB-UNIT** of an ID, NOT the whole ID
2. VFs.csv: metadate for the VF file



### AMR

---

#### The PATRIC AMR phenotype table:

```
/data/shared_data/metagenomics_graph/pathogen_database/BV-BRC/raw_data/PATRIC_genomes/PATRIC_genomes_AMR.txt
```

col1: genome id

col4: AMR phenotype



#### AMR gene sequences

Download at [CARD](https://card.mcmaster.ca/download), I'll use the "protein_homolog_model" data

```
wget https://card.mcmaster.ca/download/0/broadstreet-v3.2.7.tar.bz2
tar -xjf broadstreet-v3.2.7.tar.bz2
```



| PATRIC curated | CARD protein_homolog_model | CARD protein_knockout_model | CARD  protein_overexpression_model | CARD  protein_variant_model |
| -------------- | -------------------------- | --------------------------- | ---------------------------------- | --------------------------- |
| 2277           | 4775                       | 18                          | 13                                 | 178                         |

Explanation of models: 

the "protein homolog" model type contains sequences of antimicrobial resistance genes that do not include mutation as a determinant of resistance - these data are appropriate for BLAST analysis of metagenomic data or searches excluding secondary screening for resistance mutations. In contrast, the "protein variant" model includes reference wild type sequences used for mapping SNPs conferring antimicrobial resistance - without secondary mutation screening, analyses using these data will include false positives for antibiotic resistant gene variants or mutants.



#### Final files:

1. protein_fasta_protein_homolog_model.fasta: protein sequences of AMR genes
   1. record structure: `>gb|ACT97415.1|ARO:3002999|CblA-1 [mixed culture bacterium AX_gF3SD01_15]`
      1. ACT97415.1: CARD id
      2. ARO:3002999: Accession in GenBank
      3. CblA-1: CARD short name (no other meaning, just for programming purpose)
   2. inside the file they use full name of the pathogens, so don't need short name file for species
2. CARD-Download-README.txt: full document
3. (not sure if needed) aro_categories.tsv: map records to categories by ARO
4. aro_index.tsv: the metadata where you can map ARO id to more information such as gene family, drug class, resistant mechanism
5. shortname_antibiotics.tsv: maps drug class short names to full name here



#### Notes:

Dr. Ganda suggests use MEGARES:

```
Some genes encode enzymes ex beta-lactamases so it is AMR but not necessarily SNP associated.
The SNP associated genes usually have to do with binding site modifications. So, the long and short of it not all AMR genes are directly related to SNPs some are presence alone.
 
If MEGARES works for your stuff id suggest including it instead of just CARD as it has things related to disinfectant and heavy metal resistance. Not huge deal just wanted to make sure you knew the differences.
```





### FMH-based scan of AMR and VFDB

---

```
###### Sketching
### VFDB: split fa file to one sub-gene per record
cd /data/shared_data/metagenomics_graph/pathogen_database/VFDB
conda activate reproduce_kegg_profile

################################################# just save for now
# subunit files are too small to build sketch (~several hundred AA)
input_fas=$(realpath ./VFDB_setA_pro.fas)
mkdir -p partitiona_by_vfid_and_subunit
cd partitiona_by_vfid_and_subunit
# need to remove line breaks for sequences to make grep easier
awk '/^>/ {print (NR==1 ? "" : "\n") $0; next} {printf $0}' ${input_fas} > temp_vfdb.fa
# transfer record header to VFID-subunit structure
# caveats in grep: there exist multiple (), multipme delim within (), so need to use keyword to grep
# VFG id (or the id follows gb|) is unique identifier, so we use it + VFID
grep '>' ${input_fas} > temp_header_list.txt
cat temp_header_list.txt | while IFS= read -r line
do
 echo "$line"
 new_name=$(echo "$line" | grep -oE '(VFG[0-9]*\(|VF[0-9]*\))' | sed 's/[()]//g' | awk 'ORS=NR%2?"_":"\n"' | awk -F"_" '{print $2"_"$1}') 
 grep -A 1 --no-group-separator -Fw "${line}" temp_vfdb.fa >> ${new_name}.faa
 unset line new_name
done
rm temp*


################################################# get VFID-level sequences and build sketch
input_fas=$(realpath ./VFDB_setA_pro.fas)
mkdir -p partitiona_by_vfid_only
cd partitiona_by_vfid_only
# need to remove line breaks for sequences to make grep easier
awk '/^>/ {print (NR==1 ? "" : "\n") $0; next} {printf $0}' ${input_fas} > temp_vfdb.fa
# vfid list
grep -oE '\(VF[0-9]*\)' temp_vfdb.fa | sed 's/[()]//g' | sort -u > temp_vfid_list.txt
# partition
cat temp_vfid_list.txt | while IFS= read -r line
do
 echo "$line"
 grep -A 1 --no-group-separator -Fw "(${line})" temp_vfdb.fa >> ${line}.faa
 unset line
done
rm temp*

echo "name,genome_filename,protein_filename" > ../VFID_faa_for_sketch.csv
for file in $(ls -1); do
 name=$(echo ${file%.faa})
 path=$(readlink -f ${file})
 echo "${name},,${path}" >> ../VFID_faa_for_sketch.csv
done

inputcsv=$(readlink -f ../VFID_faa_for_sketch.csv)
cd ..
for scaleFactor in 1 2; do
 /usr/bin/time -av -o runlog_scale_${scaleFactor} sourmash sketch fromfile -p protein,k=7,k=11,abund,scaled=${scaleFactor} -o sketch_by_VFID_scaled_${scaleFactor}_k7_11.sig.zip ${inputcsv}
done

### scale 1 ~2590 hashes per file, scale 2 ~1295 hashes per file






################################################# get AMR sequences and build sketch
cd /data/shared_data/metagenomics_graph/pathogen_database/AMR

###### partition by ARO for easier node connection
input_fas=$(realpath ./protein_fasta_protein_homolog_model.fasta)
mkdir -p partitiona_by_aro
cd partitiona_by_aro

# get aro list
grep "^>" ${input_fas} | grep -oE '|ARO:[0-9]*|' > temp_aro_list.txt

# partition
cat temp_aro_list.txt | while IFS= read -r line
do
 echo "$line"
 name=$(echo "$line" | sed 's/:/_/g')
 grep -A 1 --no-group-separator -Fw "${line}" ${input_fas} >> ${name}.faa
 unset line name
done
rm temp*

echo "name,genome_filename,protein_filename" > ../AMR_faa_for_sketch.csv
for file in $(ls -1); do
 name=$(echo ${file%.faa})
 path=$(readlink -f ${file})
 echo "${name},,${path}" >> ../AMR_faa_for_sketch.csv
done

inputcsv=$(readlink -f ../AMR_faa_for_sketch.csv)
cd ..
for scaleFactor in 1; do
 /usr/bin/time -av -o runlog_scale_${scaleFactor} sourmash sketch fromfile -p protein,k=7,k=11,abund,scaled=${scaleFactor} -o sketch_by_AMR_ARO_scaled_${scaleFactor}_k7_11.sig.zip ${inputcsv}
done

### use scale=1, ~314 hashes per gene

```





### AMRFinderPlue note

---

Wiki: https://github.com/ncbi/amr/wiki

Usage: https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus

1. add `--plus` to include more ref DB such as VF
2. method: https://github.com/ncbi/amr/wiki/Methods
3. database: https://github.com/ncbi/amr/wiki/AMRFinderPlus-database
4. output format: https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus#output-format
5. interpret results: https://github.com/ncbi/amr/wiki/Interpreting-results



Example: (from Chunyu)

```
# GPU server

# /scratch/shared_data_new/GTDB/gtdb_genomes_reps_r207/AMRFinderResults
# /scratch/shared_data_new/GTDB/gtdb_genomes_reps_r207/GCA/009/668/225
```



Download metadata from NCBI database:

https://ftp.ncbi.nlm.nih.gov/pathogen/Antimicrobial_resistance/AMRFinderPlus/database/latest/

File: ReferenceGeneCatalog.txt  

1. record number: 9126, including AMR, VIRULENCE, and STRESS
2. key columns: 

| Col name           | Contents                                                     |
| ------------------ | ------------------------------------------------------------ |
| gene_family        | abbv for gene family (may contain more than 1 records corresponding to different sequences but with same function, example: [this](https://www.ncbi.nlm.nih.gov/nuccore/NG_052265.1) and [https://www.ncbi.nlm.nih.gov/nuccore/NG_052157.1](https://www.ncbi.nlm.nih.gov/nuccore/NG_052157.1)) |
| product_name       | full name of gene product. This column specifies detailed gene descript within the family |
| type               | AMR or VIRULENCE or STRESS                                   |
| subtype            | [check here](https://github.com/ncbi/amr/wiki/Interpreting-results#element-type-and-subtype) |
| class and subclass | [check here](https://github.com/ncbi/amr/wiki/Interpreting-results#element-type-and-subtype) |
| 4 accessions       | stored in nodes                                              |



Interpret output:

| Col                                           | Contentes                                                    |
| --------------------------------------------- | ------------------------------------------------------------ |
| ~~1~5, protein, contig, start, stop, strand~~ | information for hits in input genomes (we don't need this in graph) |
| 6~7, Gene symbol, Sequence name               | maps to "gene_family" and "product_name" in metadata         |
| ~~8~12, can be found in metadata~~            | ignore if we can match by col 7                              |
| 13, method                                    | [different level of cutoffs](https://github.com/ncbi/amr/wiki/Interpreting-results#the-method-column) |
| 14~20                                         | details for the match                                        |



Clean metadata and results to proper format:

```
### Clean metadate to serve as nodes
cd /scratch/shared_data_new/GTDB/gtdb_genomes_reps_r207/AMRFinderResults
file=ReferenceGeneCatalog.txt

# hits: to connect KG, use col1 gene_family, or col5 col6 the target of AMR
awk -F"\t" '{print $2,$4,$6,$7,$8,$9,$10,$11,$13,$14}' OFS="\t"  ${file} > cleaned_NCBI_AMRfinderplus_metadata.tsv


# clean output data: use this one as example
cd /scratch/shared_data_new/GTDB/gtdb_genomes_reps_r207/GCA/009/668/225
file=amrfinder_results.txt
awk -F"\t" '{print $6,$7,$13,$14,$15,$16,$17,$18,$19,$20}' OFS="\t"  ${file}  > pre_edge_based_on_amrfinder.tsv


```




