"""Turring Machine"""

from collections import deque

type transition_rule = dict[int, tuple[str, int, str]]

class TurringMachine:
    """Turing Machine"""
    def __init__(self, initial_state: str, final_state: str,
                 rules: dict[str, list[transition_rule]]):
        """Initialisation of a turing machine

        Args:
            initial_state (str): _description_
            final_state (str): _description_
            rules (dict[str, list[dict[rule]]):
                set of rules with the form
                state : { letter_read: (letter_written, movement, new_state)}
                For example the set of rule described with this array
                | State  | read      | written   | movement     | next    |
                | ------ | --------- | --------- | ------------ | ------- |
                | I      | 0         | None      | 1            | D0      |
                | I      | 1         | None      | 1            | D1      |
                ...
                | D0     | 1         | 0         | 1            | D1      |
                Would look like
                'I' : {
                    '0': (None, 1, 'D0'),
                    '1': (None, 1, 'D1)
                }
                'D0' : {
                    '1': ('0', 1, 'D1')
                }
        """
        self.inittial_state = initial_state
        self.final_state = final_state
        self.rules = rules


class Configuration:
    """
    Configuration of TuringMachine with bi-infinite ribbon.
    Blanks are represented with None objects.
    """
    def __init__(self, state: str, input: deque):
        self.state = state
        self.__pos = 0
        self.ribbon = input

    def __str__(self) -> str:
        result: str = ""
        for i in range(0, len(self.ribbon)):
            if i == self.__pos:
                result += self.ribbon[i] + "(" + self.state + ")"
            else:
                result += str(self.ribbon[i])
        return result

    def read(self):
        """
        Read the current element on the ribbon

        Returns:
            the current element of the ribbon
        """
        return self.ribbon[self.__pos]

    def next(self, letter: str, movement: int, next_state: str) -> None:
        """
        Go to the next element of the ribbon

        Args:
            letter_to_write (str): letter of the alphabet to write on the
                ribbon before moving to next element
            movement (int): 1 to go right, -1 to go left, 0 to not move
            next_state (str): state of the machine after applying movement
        """
        self.ribbon[self.__pos] = letter  # 1. writting the letter
        self.__pos += movement  # 2. moving
        # to simulate the inifnite ribbon
        # If we move outside of the ribbon we had empty element
        if self.__pos < 0:
            self.ribbon.appendleft(None)
        elif self.__pos > len(self.ribbon):
            self.ribbon.append(None)
        self.state = next_state  # 3. changing state


def calcul(machine: TurringMachine, input: list) -> str:
    """_summary_

    Args:
        machine (TurringMachine): _description_
        input (str): _description_
    """
    config: Configuration = Configuration(machine.inittial_state, input)
    print(config)
    while config.state != machine.final_state:
        letter, movement, next_state =\
            machine.rules[config.state][config.read()]
        config.next(letter, movement, next_state)
        print(config)
    return config.ribbon
