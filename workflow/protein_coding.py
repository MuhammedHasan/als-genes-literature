import pyranges as pr


df_gtf = pr.read_gtf(snakemake.input['gtf'], as_df=True)

df_gtf = df_gtf[
    (df_gtf['Feature'] == 'gene') 
    & (df_gtf['gene_type'] == 'protein_coding')
]

df_gtf = df_gtf[['gene_id', 'gene_name']]
df_gtf['gene_id'] = df_gtf['gene_id'].str.split('.').str[0]

df_gtf.to_csv(snakemake.output['protein_coding'], index=False)