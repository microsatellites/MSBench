#!/bin/sh


dir_ccs_contig_bam="/home/DATA/ProjectSTR/codes/test/MSBench/"
dir_output="/home/DATA/ProjectSTR/codes/test/MSBench/"
path_microsatellite_regions="/home/DATA/ProjectSTR/data/microsatellite_regions/GRCh38_l5_m100_20200528.no.list"
path_ref="/home/pengjia/REF/GRCh38_full_analysis_set_plus_decoy_hla/genome/GRCh38_full_analysis_set_plus_decoy_hla.fa"
/home/pengjia/miniconda3/envs/default/bin/python /home/DATA/ProjectSTR/codes/MSBench/src/main.py benchmark \
  -i ${dir_ccs_contig_bam}HG00732.Contig.GRCh38.hap1.bam \
  -o ${dir_output}HG00732.Contig.GRCh38.hap1 \
  -m ${path_microsatellite_regions} \
  -r ${path_ref} \
  -t 28 -b 3000  --tech contig

/home/pengjia/miniconda3/envs/default/bin/python /home/DATA/ProjectSTR/codes/MSBench/src/main.py benchmark \
  -i ${dir_ccs_contig_bam}HG00732.Contig.GRCh38.hap2.bam \
  -o ${dir_output}HG00732.Contig.GRCh38.hap2 \
  -m ${path_microsatellite_regions} \
  -r ${path_ref} \
  -t 28 -b 3000  --tech contig

/home/pengjia/miniconda3/envs/default/bin/python /home/DATA/ProjectSTR/codes/MSBench/src/main.py benchmark \
  -i ${dir_ccs_contig_bam}HG00732.Contig.GRCh38.hap2.bam \
  -o ${dir_output}HG00732.Contig.GRCh38.hap2 \
  -m ${path_microsatellite_regions} \
  -r ${path_ref} \
  -t 28 -b 3000  --tech contig









#/home/pengjia/miniconda3/envs/default/bin/python /mnt/project/ProjectMSI/MSCalling/note/py/MSHunter/src/main.py benchmark_merge \
#  -1 ${output_dir}ilm_test_hap1.vcf.gz -2 ${output_dir}ilm_test_hap1.vcf.gz \
#  -o ilm_test.vcf.gz -d True
