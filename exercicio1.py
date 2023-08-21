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
        # if state in self.states:
        self.initial_states.add(state)
        # else:
        #     raise ValueError(f"O estado inicial '{state}' não existe no autômato.")

    def add_alphabet(self, character):
        self.alphabet.add(character)

    def add_final_state(self, state):
        if state in self.states:
            self.final_states.add(state)
        else:
            raise ValueError(f"O estado final '{state}' não existe no autômato.")

    def add_transition(self, from_state, symbol, to_state):
        if from_state in self.states and to_state in self.states:
            if symbol in self.alphabet:
                if (from_state, symbol) in self.transitions:
                    self.transitions[(from_state, symbol)].add(to_state)
                else:
                    self.transitions[(from_state, symbol)] = {to_state}
            else:
                raise ValueError(f"O simbolo de transicao '{symbol}' não existem no autômato.")
        else:
            raise ValueError(f"Os estados '{from_state}' e/ou '{to_state}' não existem no autômato.")

    def is_accepted(self, word):
        current_states = self.initial_states
        for symbol in word:
            next_states = set()
            for state in current_states:
                transition = (state, symbol)
                if transition in self.transitions:
                    next_states.update(self.transitions[transition])
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


    # automaton.set_initial_state([state.strip() for state in initial_state.split(" ")])
    # automaton.add_alphabet([state.strip() for state in alphabet.split(" ")])
    # automaton.add_state([state.strip() for state in states.split(" ")])
    # automaton.add_final_state([state.strip() for state in final_states.split(" ")])

    for line in contents[4:]:
        transition = [item.strip() for item in line.split(" ")]
        if len(transition) == 3:
            from_state, to_state, symbol = transition
            automaton.add_transition(from_state, symbol, to_state)
        else:
            print("Formato de transição inválido.")
        print(line)



    # for state in split_input("Informe os estados iniciais (separados por vírgula Ex.: q0, q1): "):
    #     automaton.set_initial_state(state)
    #
    # for state in split_input("Informe o alfabeto (separados por vírgula. Ex.: a, b, c): "):
    #     automaton.add_alphabet(state)
    #
    # for state in split_input("Informe os estados (separados por vírgula. Ex.: q0, q1, q2): "):
    #     automaton.add_state(state)
    #
    # for state in split_input("Informe os estados finais (separados por vírgula Ex.: q0, q1): "):
    #     automaton.add_final_state(state)

    # print("Informe as transições (Digite 'fim' para encerrar)")
    # while True:
    #     transition_input = input("Transição (formato: estado atual, símbolo, estado destino Ex.: q0, a, q1): ")
    #     if transition_input == "fim":
    #         break
    #     transition = [item.strip() for item in transition_input.split(" ")]
    #     if len(transition) == 3:
    #         from_state, to_state, symbol = transition
    #         automaton.add_transition(from_state, symbol, to_state)
    #     else:
    #         print("Formato de transição inválido.")

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
