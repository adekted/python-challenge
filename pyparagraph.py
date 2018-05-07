import os
import re

paragraph = os.path.join(".","PyParagraph","raw_data","paragraph_1.txt")

with open(paragraph, 'r', newline='') as para_file:
    paragraph = para_file.read()
    print(re.split("(?&lt;=[.!?]) +", paragraph))
