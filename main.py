import pandas as pd

def process_orders(rendeles_file):
    rendeles_dict = {}

    rendeles_df = pd.read_csv(rendeles_file, delimiter=';', encoding='utf-8')
    rendeles_szam = None
    for row in rendeles_df.itertuples(index=False):
        if row[0] == 'M':
            rendeles_szam = row[2]
            rendeles_dict[rendeles_szam] = {'termek': [], 'mennyiseg': []}
        elif row[0] == 'T' and rendeles_szam is not None and row[1] == rendeles_szam:
            termek = row[2]
            mennyiseg = int(row[3])
            rendeles_dict[rendeles_szam]['termek'].append(termek)
            rendeles_dict[rendeles_szam]['mennyiseg'].append(mennyiseg)

    return rendeles_dict

rendeles_dict = process_orders('rendeles.csv')
print(rendeles_dict)
