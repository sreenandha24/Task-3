import pandas as pd
import numpy as np

netflix= pd.read_csv(r'C:\Users\sreen\OneDrive\Documents\Mallow Internship\DA Tasks\DA Task 3\netflix_titles.csv')


netflix['date_added']=pd.to_datetime(netflix['date_added'])
netflix['date_added']=netflix['date_added'].dt.strftime('%d-%m-%y')

netflix['director']=netflix['director'].fillna('unknown')
netflix['cast']=netflix['cast'].fillna('Unknown')
netflix['country']=netflix['country'].fillna('Unknown')
netflix['rating']=netflix['rating'].fillna('NA')

netflix['duration']=netflix['duration'].astype(str)
#netflix['listed_in'] = netflix['listed_in'].apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(','))


# netflix['category'] = netflix.apply(lambda x : if x['listed_in'].split(', ')[0] in x['duration'] else '', axis = 1)
# netflix['duration'] = netflix.apply(lambda x : x['duration'].split(' ')[0] if 'Season' not in x['duration'] else '', axis = 1)

# nc=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'seasons', 'listed_in', 'description']
# netflix=netflix.reindex(columns=nc)
#netflix.columns=netflix.columns.str.upper()


netflix.to_csv('netflix_titles_transformed.csv', index=False)


#print(netflix.isna().any())
#print(netflix.loc[2,'duration'])
#print(netflix['seasons'].str.contains('min').tolist().count(True))
#netflix.fillna('Null',inplace=True)

