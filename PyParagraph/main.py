import os
import re

paragraph = os.path.join(".","raw_data","paragraph_1.txt")
output = os.path.join(".","output.txt")

with open(paragraph, 'r', newline='') as para_file:
    p = para_file.read()

    sentences = []
    words = p.split()
    avg_count = (len(p)/len(words))
    splitted = re.split(r' *[\.\?!][\'"\)\]]* *', p)
    for sentence in splitted:
        if sentence != "":
            sentences.append(sentence)

with open(output,'w') as resultsfile:
    resultsfile.write("Paragraph Analysis\n")
    resultsfile.write("------------------\n")
    resultsfile.write("Approximate Word Count: " + str(len(words))+ "\n")
    resultsfile.write("Approximate Sentence Count: " + str(len(sentences)) + "\n")    
    resultsfile.write("Approximate Letter Count: " + str(avg_count) + "\n")
    resultsfile.write("Approximate Sentence Length: " + str(len(words)/len(sentences) )+ "\n")

with open(output, 'r') as readresults:
    print(readresults.read())