class DFA:

    def __init__(self, states, alphabets, transition_dict, start_state, accept_states):
        """Initialize DFA object"""
        self.STATES = states
        self.SIGMA = alphabets
        self.DELTA = transition_dict
        self.START_STATE = start_state
        self.ACCEPT_STATES = accept_states
        self.CURRENT_STATE = None
        self.logs = ""

    def clear_logs(self):
        self.logs = ""

    def run_state_transition(self, input_symbol):
        """Takes in current state and goes to next state based on input symbol."""
        if self.CURRENT_STATE == 'REJECT':
            return False

        current_state_dict = self.DELTA.get(self.CURRENT_STATE, "TRAP")
        if current_state_dict != "TRAP":
            next_state = current_state_dict.get(input_symbol, "TRAP")
            self.logs += "CURRENT STATE : {}\tINPUT SYMBOL : {}\t NEXT STATE : {}\n".format(self.CURRENT_STATE,
                                                                                            input_symbol, next_state)
            if next_state != "TRAP":
                self.CURRENT_STATE = next_state
            else:
                # enter trap state
                self.CURRENT_STATE = "REJECT"

        else:
            # enter trap state
            self.CURRENT_STATE = "REJECT"

    def check_if_accept(self):
        """Checks if the current state is one of the accept states."""
        if self.CURRENT_STATE in self.ACCEPT_STATES:
            return True
        else:
            return False

    def run_machine(self, in_string):
        """Run the machine on input string"""
        self.CURRENT_STATE = self.START_STATE

        for ele in in_string:
            check_state = self.run_state_transition(ele)
            # Check if new state is not REJECT
            if check_state == 'REJECT':
                return False
        return self.check_if_accept(), self.logs
