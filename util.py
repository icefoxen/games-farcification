# Used like so:
# >>> Numbers = enum('ZERO', 'ONE', 'TWO')
# >>> Numbers.ZERO
# 0
# >>> Numbers.ONE
# 1

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)
