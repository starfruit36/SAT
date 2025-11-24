import cnf_parser
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

    def find_unit_literal(self, clause):
        """
        Scans a clause to see if it forces a move (Unit Propagation).

        Returns:
            int: The literal that MUST be assigned True (e.g., -3).
            None: If the clause is already satisfied, or has >1 unassigned vars (not unit).
        """
        unresolved_count = 0
        unit_propagation = None

        for literal in clause:
            # Check the current status of the literal
            sat = self.get_literal_value(literal)
            if sat:
                # CNF property
                return None

            elif sat is None:
                # Found an unassigned literal
                unresolved_count += 1
                unit_propagation = literal
                if unresolved_count >= 2:
                    # If there are 2 or more unassigned vars, not a unit clause.
                    return None
        #If exactly one unassigned literal remains, that literal must be True.
        if unresolved_count == 1:
            return unit_propagation
        # If count is 0, all literals are False (Conflict), so no move to suggest.
        return None
