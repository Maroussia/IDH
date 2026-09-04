from Questions import *

print("The exercises for this notebook have been successfully imported.")

Q1 = MultQuestion("Fill in the blanks:\n\nBasic data types for storing ___ values include _____.\n\nBasic data types for storing multiple values are called _____, and include _____.\n\na) multiple, strings, booleans, lists.\n\nb) single, strings, collections, dictionaries.\n\nc) single, dictionaries, collections, strings\n\nd) string, integers, dictionaries, collections\n________________________________\n\n","b")

E1 = Solution("type(artists_birth)\nsorted(artists_birth)\nlen(artists_birth)")

Q2 = MultQuestion("What type of object is the following?\n\nopen()\n\nopen() is a ________\n\na) function\n\nb) variable\n\nc) method\n\nd) string\n________________________________\n\n","a")

Q3 = MultQuestion("In `string.replace()`, `replace()` is a type of ______ called a ________\n\na) function, method\n\nb) variable,method\n\nc) function,variable\n\nd) module,function\n________________________________\n\n","a")

E2 = Solution("(1) file_path_walrus = os.path.join(other_files, 'TheWalrusandtheCarpenter.txt')\n(2) file = open(file_path_walrus,'r')\n(3) walrus = file.read()\n(4) print(walrus)\n(5) file.close()\n\nYou can use other variable names,\nand you could potentially combine .open() and .read() methods: walrus = open('file_path_walrus,'r').read()")

E3 = Solution("walrus=open(file_path_walrus,'r')\nfor line in walrus:\n    print(line)")

Q4 = MultQuestion("In the cell above, which letter was used to indicate that we wanted to open a file in the mode writing and write in it?\n________________________________\n\n", "w")

Q5 = MultQuestion(
    "When plotting the number of texts per language in the Project Gutenberg dataset, we used a logarithmic scale on the y-axis. Why?\n\n"
    "a) Because it hides outliers in the data\n\n"
    "b) Because it makes very large and very small values easier to compare visually\n\n"
    "c) Because it reduces all values to a range between 0 and 1\n\n"
    "d) Because it makes bar plots look more colorful\n________________________________\n\n",
    "b",
    "Correct! A logarithmic scale helps compress large differences so smaller values are still visible on the plot.",
    "Incorrect. The purpose of using a log scale here is to make both large and small values more visually comparable."
)

E5= Solution("PGmetadata = pd.read_csv(csv_path).set_index('Text#')")