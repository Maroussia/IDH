from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution("Your code might look like:\n\ncount = 6\n\nwhile count > 0:\n    if count %2 ==0:\n        print('tick')\n    else:\n        print('tock')\n    count = count-1\nprint('Ring!')")

E2 = Solution("from random import shuffle\ngame = ['duck', 'duck', 'duck', 'goose', 'duck']\n\nwhile game[0]=='duck':\n    print('safe')\n    shuffle(game)\n\nprint('Run!')")

E3 = Solution("value = 0\nwhile True:\n    if value%2==0:\n        print(value)\n    if value ==20:\n        break\n    value= value+1")

E4 = Solution("value = 0\n\nwhile value<=20:\n    value= value+1\n    if value%2==0:\n        print(value)\n")

E5 = Solution("You can choose the name you want for the variable. Preferably, choose a name that is straightforward, not ambiguous, and meaningful to the readers.\n\nauthor_name = 'Quevedo'\nfor book in pg_metadata:\n  if author_name in book['Authors']:\n    print(book['Title'], 'by', book['Authors']\n\n\n")

E6 = Solution("dict2 = {}\nfor key, value in dict1.items():\n    dict2[value] = key\nprint(dict2)")