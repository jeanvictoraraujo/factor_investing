# %%
import pandas as pd
import numpy as np

# %%
df = (
    pd.read_excel(
        r"DIRETORIO"
    )
    .dropna()
    .sort_values(by=["CRITERIO"], 
                 ascending=False)
    .reset_index(drop=True)
)
df
# %%
quantil = df["CRITERIO"].quantile([0.25, 0.50, 0.75, 1.00])

def classificar_quartil(valor):
    if valor <= quantil[0.25]:
        return "Quartil 1"
    elif valor <= quantil[0.50]:
        return "Quartil 2"
    elif valor <= quantil[0.75]:
        return "Quartil 3"
    else:
        return "Quartil 4"
    
df['Quartil_Classificado'] = df['CRITERIO'].apply(classificar_quartil)
