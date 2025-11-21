try:
    with open("../data/test.cnf", "r") as file:
        problem = file.readlines()
        SAT = []
        for lines in problem:
            if lines.startswith("c"):
                continue
            else:
                SAT.append(lines)
                
except:
    print("An error occurred!") #placeholder

print(SAT)