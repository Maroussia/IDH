from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution("type(year_of_birth)\n\nWhen you run `type(year_of_birth), the output is 'str', Python abbreviation for a string. We enclosed the variable in quotes, so Python has interpreted them not as a number, but as text. This is desirable if we want to use the date as text, but it will also prevent us from conducting mathematical operations on its numerical value.")

Q1 = MultQuestion("How can you recognize that the string has been transformed into an integer?\n\na) The characters are digits \n\nb) The characters are not surrounded by quotes \n\nc) The characters are surrounded by quotes \n\nd) The characters are surrounded by digits\n\n","b")

E2 = Solution("year_of_birth = int(year_of_birth)")

E3 = Solution("x = 1\ny = 2\n(x - y)**2/2")

E4 = Solution("lifespan = year_of_death - year_of_birth\nprint(lifespan)")