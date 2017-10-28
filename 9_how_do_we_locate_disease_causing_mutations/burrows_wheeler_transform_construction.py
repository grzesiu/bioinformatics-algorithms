def transform(text):
    cyclic_rotations = [text[i:] + text[:i] for i in range(len(text))]
    bwt = [cyclic_rotation[-1] for cyclic_rotation in sorted(cyclic_rotations)]
    return ''.join(bwt)


def main(text):
    print(transform(text))


if __name__ == "__main__":
    main("GCGTGCCTGGTCA$")

'''
Construct the Burrows-Wheeler transform of a string.
Given: A string Text.
Return: BWT(Text).
Output:
ACTGGCT$TGCGGC
'''
