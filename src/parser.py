try:
    with open("../data/test.cnf", "r") as file:
        problem = file.readlines()
        SAT = []
        clause = []
        num_of_var = 0
        num_of_clauses = 0
        valid = True
        neg_switch = False
        for lines in problem:
            if lines.startswith("c"):
                continue
            elif lines.startswith("p"):
                for i in lines:
                    try:
                        int(i)
                        if num_of_var == 0:
                            num_of_var = i
                        elif num_of_var != 0 and num_of_clauses == 0:
                            num_of_clauses = i
                        else:
                            print("An error occurred!")  # placeholder
                    except:
                        continue
                continue
            try:
                int(lines[0])
                lines = lines.strip()
                lines = lines.replace(" ", "")
                for i in lines:
                    try:
                        if i != "-":
                            int(i)
                    except:
                        valid = False
                        print("errorrr!")  # placeholder
                    if i != "-" and valid:
                        if not neg_switch:
                            num = int(i)
                        else:
                            num = -int(i)
                            neg_switch = False
                    elif i == "-" and valid:
                        neg_switch = True
                        continue
                    if num != 0:
                        clause.append(num)
                    elif num == 0:
                        if len(clause) != 0:
                            SAT.append(clause[:])
                            clause.clear()
            except:
                print("error!")  # placeholder
except:
    print("An error!") #placeholder
