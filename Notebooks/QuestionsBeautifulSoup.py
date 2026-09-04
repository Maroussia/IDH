from Questions import *

print("The exercises for this notebook have been successfully imported.")

E1 = Solution('type(soup)')

E2 = MultQuestion(
    "Which line will give the subject stored in the metadata?\n\n"
    "a) soup.find('subject').get_text(strip=True)\n\n"
    "b) soup.find('dcterms:subject').get_text(strip=True)\n\n"
    "c) soup.find('dcterms:subject').get_text(strip=False)\n\n"
    "d) soup.find('dcterms:subject').get_subject(strip=True)\n________________________________\n\n",
    "b",
    "Correct!",
    "Incorrect."
)

E3 = CodeLine(
    prompt="Type the line of code that will print the title using the dictionary:\n",
    answer="bib['Title']"
)

E4 = MultQuestion(
    "Which line will give the number of downloads?\n\n"
    "a) soup.select('li.booklink')[0].select_one('.downloads').get_text()\n\n"
    "b) soup.select('li.booklink')[5].select_one('.downloads').get_text()\n\n"
    "c) soup.select('li.downloads')[5].select_one('.extra').get_text()\n\n"
    "d) soup.select('li.booklink')[5].select_one('.extra').get_text()\n________________________________\n\n",
    "d",
    "Correct!",
    "Incorrect."
)

E5 = Solution('pgmed1800 = pd.DataFrame(records)')

E6 = Solution('data = {}')

E7 = Solution('pgmed1800_authors = pd.DataFrame(authors_data)')
