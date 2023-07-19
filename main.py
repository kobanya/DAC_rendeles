import csv

def process_orders(rendeles_file):
    rendeles_dict = {}

    with open(rendeles_file, newline='', encoding='utf-8') as csvfile:
        rendeles_reader = csv.reader(csvfile, delimiter=';')
        for row in rendeles_reader:
            if row[0] == 'M':
                rendeles_szam = row[2]
                rendeles_dict[rendeles_szam] = {'termek': [], 'mennyiseg': []}
            elif row[0] == 'T':
                rendeles_szam = row[1]
                termek = row[2]
                mennyiseg = int(row[3])
                rendeles_dict[rendeles_szam]['termek'].append(termek)
                rendeles_dict[rendeles_szam]['mennyiseg'].append(mennyiseg)

    return rendeles_dict

rendeles_dict = process_orders('rendeles.csv')
print(rendeles_dict)

