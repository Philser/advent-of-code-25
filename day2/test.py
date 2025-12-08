from day2 import is_repeating_sequence

assert is_repeating_sequence(111), True
assert is_repeating_sequence(11), True
assert is_repeating_sequence(112112), True
assert is_repeating_sequence(121212), True
assert is_repeating_sequence(1212121212), True
assert is_repeating_sequence(5) == False
assert is_repeating_sequence(12123) == False
assert is_repeating_sequence(121) == False
assert is_repeating_sequence(11114) == False
assert is_repeating_sequence(12312312) == False