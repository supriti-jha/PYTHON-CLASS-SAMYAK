saurav = '''
Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation,[38] "plain English" naming, an extensive ("batteries-included") standard library, and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions. Beginning with Python 3.5,[39] capabilities and keywords for typing were added to the language, allowing optional static typing.[40] As of 2026, the Python Software Foundation supports Python 3.10, 3.11, 3.12, 3.13, and 3.14, following the project's annual release cycle and five-year support policy. Python 3.15 is currently in the alpha development phase, and the stable release is expected to come out in October 2026.[41] Earlier versions in the 3.x series have reached end-of-life and no longer receive security updates.
'''


website = '''
Python is a popular, high-level, interpreted programming language known for its simple, readable syntax that emphasizes code readability and reduces maintenance costs. It is widely used for web development, data analysis, artificial intelligence, and automation, making it ideal for both beginners and professionals.'''

# Convert it into set
set1 = set(saurav.split())
set2 = set(website.split())
print(len(set1),len(set2))
# remove gramatical words
# import nltk
# natural language processing toolkit
# nltk.download("stopwords")
from nltk.corpus import stopwords
sw = set(stopwords.words("english"))
set1 = set1.difference(sw)
set2 = set2.difference(sw)

# find simmilarity
# COMMON/TOTAL*100
common = len(set1.intersection(set2))
total = len(set1.union(set2))
print(common/total*100,"%")