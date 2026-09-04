from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution("The best column from PG metadata to use as index is 'Text#', because it contains the unique text identification numbers.\n\n_______________________\n\n(1) To set the index in our existing dataframe, we use the set_index() method and the parameter inplace:\n\nPGmetadata.set_index('Text#', inplace=True)\n\n_______________________\n\n(2) To import the CSV with PG metadata and set the index from the beginning, we apply the read_csv() method and set the index with the parameter index_col and the name of the column that we want to use as index:\n\nPGmetadata = pd.read_csv('PG/pg_catalog.csv', index_col='Text#')")

E2 = Solution("(1)\nPGmetadata['Subjects']\n\n(2)\nPGmetadata[['Title','Authors', 'Subjects']]")

Q1 = MultQuestion("What type of containers were outputted by the two cells above? \n\na) A list (one-dimensional) and a dictionary (two-dimensional) \n\nb) A list (two-dimensional) and a DataFrame (one-dimensional)\n\nc) Two DataFrames (one-dimensional and two-dimensional) \n\nd) A Series (one-dimensional) and a DataFrame (two-dimensional)\n\n_____________________________________\n\n","d")

E3 = Solution("PGbookshelves = PGmetadata[['Title', 'Bookshelves']].copy()")

E4 = Solution("PGauthors = pd.read_csv(f'{module_path}/PG/pg_authors.csv')")
                  
E5 = Solution("PGauthors[PGauthors['languages']=='es']")

E6 = Solution("PGauthors[(PGauthors['death']<1400) & (PGauthors['languages']=='es')]")

E7 = Solution("PGauthors.loc[32979, 'raw_entry']")

E8 = Solution("PGauthors.loc[PGauthors['death']<1100,['last_name', 'first_name', 'death', 'languages']]")
