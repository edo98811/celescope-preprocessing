wget  --tries=3 ftp://ftp.ensembl.org/pub/release-99/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz
wget  --tries=3 ftp://ftp.ensembl.org/pub/release-99/gtf/mus_musculus/Mus_musculus.GRCm38.99.gtf.gz

gunzip Mus_musculus.GRCm38.dna.primary_assembly.fa.gz 
gunzip Mus_musculus.GRCm38.99.gtf.gz

# conda activate celescope

celescope utils mkgtf Mus_musculus.GRCm38.99.gtf Mus_musculus.GRCm38.99.filtered.gtf
celescope rna mkref \
 --genome_name Mus_musculus_ensembl_99_filtered \
 --fasta Mus_musculus.GRCm38.dna.primary_assembly.fa \
 --gtf Mus_musculus.GRCm38.99.filtered.gtf \
