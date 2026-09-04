from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution('pg_med = pd.read_csv(f"{module_path}/PG/pg_medperiodicals.csv", index_col=0)')

Q1 = MultQuestion("The function `fetch_text_from_id` takes two arguments, pgid and timeout. What is the 'type' of pgid?\n\na) string \n\nb) integer \n\nc) number \n\nd) tuple\n\n",
                  "b", 
                  "Correct! The Python name for integer is `int`.", 
                  "Incorrect. The Python name for integer is `int`, it is given in the function definition, after the name of the argument, namely 'pgid: int'.")

Q2 = MultQuestion("If we run the function with the text ID 22336, what will be the URL used in the function?\n\na)https://www.gutenberg.org/cache/epub/pg22336.txt \n\nb)https://www.gutenberg.org/cache/epub/{22336}/pg{22336}.txt \n\nc) https://www.gutenberg.org/cache/epub/22336/pg22336.txt.\n\n", 
                  "c", 
                  "Correct! The curly brackets will be automatically replaced by the text ID.",
                  "Incorrect. The curly brackets will be automatically replaced by the text ID: https://www.gutenberg.org/cache/epub/22336/pg22336.txt.")

E2 = Solution("text_22336 = fetch_text_from_id(22336)")

E3 = Solution("def trans_text(text: str) -> str:\n    return text.translate(table)")
