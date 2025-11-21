def parse_dimacs(filename):
    SAT = []
    clause = []
    num_of_var = 0
    num_of_clauses = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                # 1. Skip comments and empty lines
                if not line or line.startswith("c"):
                    continue
                # 2. Parse Header
                if line.startswith("p"):
                    parts = line.split()  
                    num_of_var = int(parts[2])
                    num_of_clauses = int(parts[3])
                    continue
                tokens = line.split() 
                for token in tokens:
                    try:
                        num = int(token) 
                        if num == 0: # 0 means end of clause
                            if clause:
                                SAT.append(clause[:])
                                clause = []
                        else:
                            clause.append(num)
                    except ValueError:
                        print(f"Error parsing token: {token}")
                        continue
    except FileNotFoundError:
        print("File not found!")
        return [], 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], 0
    return SAT, num_of_var, num_of_clauses