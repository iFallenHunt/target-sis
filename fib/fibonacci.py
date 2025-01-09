def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth term.
    :param n: Number of terms of the sequence to be generated
    :return: List containing the Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def is_in_fibonacci(number, sequence):
    """
    Checks if a number is in the generated Fibonacci sequence.
    :param number: Number to be checked
    :param sequence: List with the Fibonacci sequence
    :return: True if the number is in the sequence, False otherwise
    """
    return number in sequence


# Example of usage
n_terms = int(input(
    "How many terms of the Fibonacci sequence do you want to generate? "))
number_to_check = int(input("Enter the number you want to check: "))

fibonacci_sequence = generate_fibonacci(n_terms)
print("Generated sequence:", fibonacci_sequence)

if is_in_fibonacci(number_to_check, fibonacci_sequence):
    print(f"The number {number_to_check} is in the generated Fibonacci "
          "sequence.")
else:
    print(
        f"The number {number_to_check} is not in the generated Fibonacci "
        "sequence."
    )
