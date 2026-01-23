"""test of TurringMachine with a machine that increment a binary number
"""

from collections import deque

from src.turring.machine import TurringMachine, calcul, rule


rules_incr: dict[str, list[rule]] = {
    'A': {
        '0': ('0', 1, 'A'),
        '1': ('1', 1, 'A'),
        None: (None, -1, 'B')
    },
    'B': {
        '0': ('1', 0, 'F'),
        '1': ('0', -1, 'B'),
        None: ('1', 0, 'F')
    }
}

machine_incr = TurringMachine('A', 'F', rules_incr)


def test_incr_19():
    assert calcul(machine_incr, deque("10011")) == ["1", "0", "1", "0", "0"]
