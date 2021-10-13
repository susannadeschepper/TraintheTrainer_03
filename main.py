import pandas as pd

df = pd.read_csv(r"dmg.csv", delimiter=",")
print(df)

#print(df['object_name'][0:5])

#kolommen
#print(df[['object_name', 'creator']])

#nieuw dataframe met lijst van 2 kolommen
#df2 = df[['object_name', 'creator']]

#rijen
#print(df.iloc[0:4])

#specifieke locatie
#print(df.iloc[0:10, 0:3])

#df = df.rename(columns={'object_name': 'objectnaam', 'object_number': 'objectnummer'})
#print(df)

#1 is om de kolommen te kiezen (en niet de index, 0)
#df3 = df.drop('institution.name', 1)
#print(df3)

#kolom toevoegen
#df['Test'] = df['objectnummer'] + df['institution.name']
#print(df)

#kolom verplaatsen
cols = list(df.columns.values)
#print(cols)
#df = df[cols[0:3] + [cols[-1]] + cols[4:34]]
#print(df)

#sorteren
#df = df.sort_values('objectnaam', ascending=False)
#print(df)

#combi ene oplopend, andere aflopend
#df4 = df.sort_values(['creator', 'title'], ascending=[1,0])
#print(df4)

#filteren
#df5 = df.loc[df['production.place'] == 'Gent']
#print(df5)

df6 = df.loc[(df['production.place'] == 'Gent') & (df['creator.role'] == 'ontwerper')]
print(df6)

#csv opslaan
#df6.to_csv('Gentseontwerpers.csv')

#waarden tellen (variabelen aanmaken voor grafieken later, moet via count)
aantal_records = df['institution.name'].count()
print(aantal_records)

#aantal records met beschrijving
aantal_beschrijving = df["description"].count()
print(aantal_beschrijving)

#aantal in Gent vervaardigd
filterplaatsGent = df.loc[df['production.place'] == 'Gent']

records_vervaardigdinGent = filterplaatsGent['production.place'].count()
print(records_vervaardigdinGent)

#visualiseren met matplotlib

from matplotlib import pyplot as plt

#aantal records vervaardigd in Gent
vervaardigingGent = [aantal_records-records_vervaardigdinGent, records_vervaardigdinGent]
plt.pie(vervaardigingGent)
plt.show()

#voorbeeld



