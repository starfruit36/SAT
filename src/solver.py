class DPLLSolver:
    def __init__(self, n_vars, clauses):
        self.n_vars = n_vars
        self.clauses = clauses
        # State Dictionary: {1: True, 2: False}
        # If a variable isn't here, it is Unassigned.
        self.assignments = {}

    def get_literal_value(self, literal):
        """
        Retrieves the truth value of a literal based on current assignments.
        Returns: True (satisfied), False (unsatisfied), or None (unassigned).
        """
        node  = abs(literal)
        # 1. Check if the variable is unassigned 
        try:
            assignment = self.assignments[node]
        except KeyError:
            return None # Variable is unassigned
        # 2. Determine the literal's value based on assignment and sign
        if assignment: # Var is True
            return literal > 0
        else: # Var is False
            return literal < 0
    def check_clause_status(self, clause):
        """
        Determines the status of a single clause.
        Returns: 'SAT', 'CONFLICT', or 'UNRESOLVED'.
        """
        # Track existence of unassigned variables
        remained_unresolved = False
        # Iterate through all literals to find truth value
        for literal in clause:
            sat  = self.get_literal_value(literal)
            if sat:
                #Clause is satisfied CNF properties
                return 'SAT'
            elif sat is None:
                remained_unresolved = True
            # If False just continue to find True
        if remained_unresolved:
            # No True literals were found, but at least one is Unassigned
            return 'UNRESOLVED'
        # If no True and no None were found, all literals must be False
        return 'CONFLICT'