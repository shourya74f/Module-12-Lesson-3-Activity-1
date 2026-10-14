import os

print("Science Facts: ")
with open("Science Facts.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("Word Count in Math Facts: ")
with open("Geometry Facts.txt", "r") as f:
    for line in f:
        w=line.split()
        print(len(w), "words in line:", line.strip())
print()

if os.path.exists("Combined Facts.txt"):
    print("Combined Facts.txt already exists. It will be overwritten.\n")
else:
    print("Combined Facts.txt does not exist. It will be created.\n")

c=""
with open("Science Facts.txt", "r") as f:
    c+=f.read()+"\n"
with open("Geometry Facts.txt", "r") as f:
    c+=f.read()+"\n"
with open("Combined Facts.txt", "w") as o:
    o.write(c)
print("All facts have been stored into Combined Facts.txt")
print()

if os.path.exists("Combined Facts.txt"):
    os.remove("Combined Facts.txt")
    print("Combined Facts.txt has been deleted.")
else:
    print("Combined Facts.txt does not exist.")