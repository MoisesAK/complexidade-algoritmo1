class Automaton:

    def __init__(self):
        self.states = set()
        self.initial_states = set()
        self.alphabet = set()
        self.final_states = set()
        self.transitions = {}

    def add_state(self, state):
        self.states.add(state)

    def set_initial_state(self, state):
        self.initial_states.add(state)

    def add_alphabet(self, character):
        self.alphabet.add(character)

    def add_final_state(self, state):
        if state in self.states:
            self.final_states.add(state)
        else:
            raise ValueError(f"O estado final '{state}' não existe no autômato.")

    def add_transition(self, from_state, symbol, to_state):
        if from_state in self.states and to_state in self.states:
            if symbol in self.alphabet or symbol == '&':
                if (from_state, symbol) in self.transitions:
                    self.transitions[(from_state, symbol)].add(to_state)
                else:
                    self.transitions[(from_state, symbol)] = {to_state}
            else:
                raise ValueError(f"O símbolo de transição '{symbol}' não existe no autômato.")
        else:
            raise ValueError(f"Os estados '{from_state}' e/ou '{to_state}' não existem no autômato.")

    def get_next_states(self, current_states, symbol):
        next_states = set()

        for state in current_states:
            transition = (state, symbol)
            if transition in self.transitions:
                next_states.update(self.transitions[transition])

        return next_states

    def epsilon_closure(self, states):
        closure = states.copy()
        print(closure)

        while True:
            new_states = self.get_next_states(closure, '&') - closure
            if new_states:
                print("transacao vazia para")
                print(new_states)
            if not new_states:
                print("sem transacao vazia")
                break
            closure.update(new_states)
        return closure

    def is_accepted(self, word):
        current_states = self.epsilon_closure(self.initial_states)

        for symbol in word:
            next_states = self.epsilon_closure(self.get_next_states(current_states, symbol))
            print(next_states)
            print("---------------")

            current_states = next_states

        return any(state in self.final_states for state in current_states)


def split_input(input_message):
    user_input = input(input_message)
    return [state.strip() for state in user_input.split(" ")]


def interact_with_user():
    automaton = Automaton()

    f = open("imput.txt", "r")
    contents = f.readlines()
    if len(contents) < 4:
        raise ValueError(f"precisa ter mais do que 4 linhas no arquivo")

    initial_state, alphabet, states, final_states = contents[0:4]
    print([state.strip() for state in initial_state.split(" ")])
    print([state.strip() for state in alphabet.split(" ")])
    print([state.strip() for state in states.split(" ")])
    print([state.strip() for state in final_states.split(" ")])

    for state in [state.strip() for state in initial_state.split(" ")]:
        automaton.set_initial_state(state)

    for state in [state.strip() for state in alphabet.split(" ")]:
        automaton.add_alphabet(state)

    for state in [state.strip() for state in states.split(" ")]:
        automaton.add_state(state)

    for state in [state.strip() for state in final_states.split(" ")]:
        automaton.add_final_state(state)

    for line in contents[4:]:
        transition = [item.strip() for item in line.split(" ")]
        if len(transition) == 3:
            from_state, to_state, symbol = transition
            automaton.add_transition(from_state, symbol, to_state)

        else:
            print("Formato de transição inválido.")
        print(line)

    while True:
        word = input("Informe uma palavra (ou digite 'fim' para encerrar): ")
        if word == "fim":
            break
        if automaton.is_accepted(word):
            print("Palavra aceita pelo autômato.")
        else:
            print("Palavra rejeitada pelo autômato.")


try:
    interact_with_user()
except ValueError as e:
    print(f"Erro: {e}")
