import requests
import pandas as pd


html = requests.get('https://alsod.ac.uk/')
df = pd.read_html(html.text)[1]

df = df.rename(columns={'Gene symbol': 'gene_name'})
df['citation'] = ';'.join([
    '10.1136/jmedgenet-2020-106866',
    '10.3109/17482968.2011.584629'
])

df[['gene_name', 'citation']] \
    .to_csv(snakemake.output['alsod'], index=False, sep='\t')

