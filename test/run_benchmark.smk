dir_ccs_contig_bam = "/home/DATA/ProjectSTR/codes/test/MSBench/"
dir_output = "/home/DATA/ProjectSTR/codes/test/MSBench/"
path_microsatellite_regions = "/home/DATA/ProjectSTR/data/microsatellite_regions/GRCh38_l5_m100_20200528.no.list"
path_ref = "/home/pengjia/REF/GRCh38_full_analysis_set_plus_decoy_hla/genome/GRCh38_full_analysis_set_plus_decoy_hla.fa"
python = "/home/pengjia/miniconda3/envs/default/bin/python"
my_script = "/home/DATA/ProjectSTR/codes/MSBench/src/main.py"

samples = ["HG00733"]
rule all:
    input:
         expand(dir_output + "{sample}/{sample}.Contig.GRCh38.vcf.gz", sample=samples)

rule benchmark_one_hap:
    input:
         bam=dir_ccs_contig_bam + "{sample}.Contig.GRCh38.{hap}.bam",
         ms_list=path_microsatellite_regions,
         ref=path_ref
    output:
          dir_output + "{sample}/{sample}.Contig.GRCh38.{hap}"
    threads: 28
    shell:
         "{python} {my_script} benchmark -i {input.bam} -o {output} -m {input.ms_list} -r {input.ref} -t {threads} -b 500"
         "touch {output}"
rule benchmark_merge:
    input:
         hap1=dir_output + "{sample}/{sample}.Contig.GRCh38.hap1",
         hap2=dir_output + "{sample}/{sample}.Contig.GRCh38.hap2"
    output:
          "{sample}/{sample}.Contig.GRCh38.vcf.gz"
    shell:
         "{python} {my_script} benchmark_merge  -1 {input.hap1}.vcf.gz -2 {input.hap2}.vcf.gz -o {output}  -s {wildcards.sample}"
