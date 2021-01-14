import glob

read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            y = []
            content = infile.readlines()
            for x in range(len(content)):
                try:
                    if content[x].rstrip() in content[x+1].rstrip():
                        y.append(x)
                except IndexError as error:
                    print('Termino un archivo')
            for ele in sorted(y, reverse = True):  
                del content[ele] 
            outfile.writelines(content)
            y.clear()