import sys

infile = "output_Cleared_file.txt"
outfile = "output_aCleared_file.txt"

delete_list = ["(", ")"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()