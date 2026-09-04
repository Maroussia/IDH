from Questions import *

print("The exercises for this notebook have been successfully imported.")

Q1 = MultQuestion("I want to run the line of code 'import spacy' and add a comment about what I am doing ('here i am importing a python module named spacy'). Which of these would *not* work?\n\na) import spacy # here i am importing a python module named spacy\n\nb) #below I am importing a python module named spacy \nimport spacy\n\nc) #here I import a python module named spacy import spacy \n\nd) All of the above should work.\n\n","c","Correct! Comments can be added with a hashtag after code or in a separate line.","Incorrect, the hashtag invalidates any code after it on the same line.")

Q2 = MultQuestion("Python interprets whitespace as part of the structure of the language. Which of the following are true?\n\na) Lines represent statements \n\nb) Lines indented at the same level form part of a block of code \n\nc) Extra whitespace within a line, and extra blank lines, are not interpreted by Python \n\nd) All of the above.\n\n", "d", "Correct! Whitespace is important in Python in all these ways.", "Incorrect. Python uses whitespace in all the ways above.")

E1 = Solution("count = 10 \nwhile count > 0: \n    print(str(count) +'!') \n    count = count - 1 \nprint('lift off!')")

E2= Solution("You could choose any name for this variable, although it is best to choose one that makes sense to the reader as well (we chose 'authors', but you could also use 'authors_names', for instance. The variable should be assigned to a list object, and remember to surround strings with quotes.\n\nauthors = ['Jane Austen', 'Charlotte Brontë', 'Virginia Woolf']")

Q3=MultQuestion('Which of these statements assigns a value to a variable?\n\na) value = variable \n\nb) variable == value \n\nc) value == variable \n\nd) variable = value\n\n','d',"Correct! When assigning a value to a variable, the variable is on the left, followed by a single equals sign and the value comes on the right.","Incorrect. When assigning a value to a variable, the variable is on the left, followed by a single equals sign and the value comes on the right.")

E3 = Solution("authors = ['Jane Austen', 'Charlotte Brontë', 'Virginia Woolf']\n\nprint(authors)\n\n\nThe problem was that the variable x we were trying to print is not defined. Instead, we should have written the name of our variable, 'authors', in the print statement, as shown in the solution above.\n\nAlternatively, you could define a variable x to be printed by the print(x) statement.\nFor example:\n\nx= 'Virginia Woolf'\n\nprint(x).\n\n\nNote that x is not the best variable name.")