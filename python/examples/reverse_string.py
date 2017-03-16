def sillycase(string):
    half_length = int(len(string) / 2)
    first_half = string[:half_length]
    second_half = string[half_length:]
    return first_half.lower() + second_half.upper()

print(sillycase('sharknado'))
