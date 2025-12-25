from day5 import IDRange, challenge2

id_ranges = [
    IDRange(start=3, end=5),
    IDRange(start=10, end=14),
    IDRange(start=16, end=20),
    IDRange(start=12, end=18),
]
result = challenge2(id_ranges)
assert result == 14

id_ranges = [
    IDRange(start=4, end=7),
    IDRange(start=12, end=34),
    IDRange(start=1, end=4),
    IDRange(start=7, end=13),
]
result = challenge2(id_ranges)
assert result == 34
