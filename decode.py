def decode(message_file):
    # Read the content of the message_file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers and words from each line
    pairs = [line.split() for line in lines]

    # Sort pairs based on the numbers
    sorted_pairs = sorted(pairs, key=lambda x: int(x[0]))

    # Extract words corresponding to the first index and indices divisible by 3
    message_words = [pair[1] for i, pair in enumerate(sorted_pairs) if i == 0 or (i + 1) % 3 == 0]

    # Combine the words into a decoded message
    decoded_message = ' '.join(message_words)

    return decoded_message