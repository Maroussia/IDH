from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution("import pandas as pd\n\npg_authors = pd.read_csv(f'{module_path}/PG/pg_authors.csv')")

E2 = Solution("\npg_authors['testcolumn'] = ''\n\npg_authors = pg_authors.drop(columns ='testcolumn')")

E3 = Solution("ghettoes.melt(id_vars = ['GhettoID','GhettoName','Longitude','Latitude'], value_vars = ['UnspecE','UnknownE','UncertE','TyphusE','TyphoidE','TuberE','no_E','DysenteryE'], var_name ='Epidemic', value_name = 'EpidemicYN')")

Q1 = MultQuestion("How many topics are common to Subjects and Bookshelves?\n\n","67", "Correct!", "Incorrect. Run the next cell to see which line of code can help you find the right count.")

E4 = Solution("(len(pg_subjects) + len(pg_bookshelves)) - len(pg_topics) + 1\n_____________________________________\n\nIf we subtract the number of topics in pg_topics to the sum of topics of Subjects and Bookshelves, we get 66 and we need to add 1 because in Python count starts with 0.\n\n\n")

E5 = Solution("pg_topics_common = pd.merge(\n"
    "    pg_subjects,\n"
    "    pg_bookshelves,\n"
    "    on='Topics',\n"
    "    how='inner'\n"
").fillna(0)"
)
