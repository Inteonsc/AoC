import os

language = input("Language: ").lower().capitalize()
year = input("Year: ").lower()
extension = input("File Extension(not including dot): ").lower()
Path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), year, language)

os.makedirs(Path,exist_ok=True)
for i in range(7,26):
    os.makedirs(os.path.join(Path,"Day" + f"{i:02d}"))
    f = open(os.path.join(Path, "Day" + f"{i:02d}", "p1." + extension),"a")
    f.write("import os\nif __name__ == \"__main__\":\n data = open(os.path.dirname(os.path.abspath(__file__)) + \"\input.txt\").readlines()")
    f.close()
    f = open(os.path.join(Path, "Day" + f"{i:02d}", "p2." + extension),"a")
    f.write("import os\nif __name__ == \"__main__\":\n data = open(os.path.dirname(os.path.abspath(__file__)) + \"\input.txt\").readlines()")
    f.close()
    f = open(os.path.join(Path, "Day" + f"{i:02d}", "input.txt"),"a")
    f.close()
    f = open(os.path.join(Path, "Day" +f"{i:02d}", "tests." + extension),"a")
    f.close()
    
