import pandas as pd
from chembl_webresource_client.new_client import new_client
uniprot_ids = {} 
uniprot_ids['EGFR'] = "P00533"
uniprot_ids['CMET'] = "P08581"
# Getting a target for the given accession:
for uid in list(uniprot_ids.keys()):
    targets = new_client.target.filter(target_components__accession=uniprot_ids[uid])
    # Retrieving activities:
    activities = new_client.activity.filter(target_chembl_id__in=[target['target_chembl_id'] for target in targets]).filter(pchembl_value__gt=3)
    # Creating a set of unique SMILES:
    df = pd.DataFrame(activities) 
    df.to_csv('CHEMBL_%s_GT3.csv'%uid,index=False)
