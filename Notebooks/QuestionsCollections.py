from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution("authors = ['Jane Austen', 'Charlotte Brontë', 'Virginia Woolf', 'George Sand']")

E2 = Solution("authors[0:3]\n\nRecall that indexing starts at position 0, and slicing goes up to, but not including, the final number in our range. Thus, list[0:3] gives item 1 (position 0), item 2 (position 1), item 3 (position 2), up to, but not including item 4.")

E3 = Solution("authors[1] = 'Adeline Virginia Woolf'")

E4 = Solution("modern_authors = [Elif Shafak, Svetlana Alexievich, Elena Ferrante.]\n\nauthors.extend(modern_authors)\n\nlen(authors)\n\nauthors.pop()\n\nprint(authors)\n\nauthors.remove('Amantine Lucile Aurore Dupin de Francueil')\n\nauthors.append('George Sand')")

E5 = Solution("gender['Elena Ferrante']='unknown'")

E6= Solution("dict2 = {}\nfor key, value in a_dict.items():\n     dict2[value] = key\nprint(dict2)")