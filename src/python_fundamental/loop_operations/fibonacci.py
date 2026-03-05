def fibonacci(number: int):
    if number <= 0:
        return []
    
    sequence: list[int] = [0]
    if number == 1:
        return sequence
    
    sequence.append(1)

    for i in range(2, number):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence
