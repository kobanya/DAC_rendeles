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

def compare_orders_stock(rendeles_dict, keszlet_df):
    keszlet_df['rendelt_mennyiseg'] = 0

    for rendeles_szam, rendeles_data in rendeles_dict.items():
        for termek, mennyiseg in zip(rendeles_data['termek'], rendeles_data['mennyiseg']):
            if termek in keszlet_df['termek'].values:
                keszlet_df.loc[keszlet_df['termek'] == termek, 'rendelt_mennyiseg'] += mennyiseg

    keszlet_df['kulonbseg'] = keszlet_df['mennyiseg'] - keszlet_df['rendelt_mennyiseg']

    return keszlet_df

rendeles_dict = process_orders('rendeles.csv')
keszlet_df = pd.read_csv('keszlet.csv', delimiter=';', encoding='utf-8')

merged_df = compare_orders_stock(rendeles_dict, keszlet_df)
print(merged_df)
