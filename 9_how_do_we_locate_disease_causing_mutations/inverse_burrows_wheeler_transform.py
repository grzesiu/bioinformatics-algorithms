def join(cyclic_rotations, transform):
    return [transform[i] + cyclic_rotations[i] for i in range(len(transform))]


def inverse(transform):
    cyclic_rotations = transform
    for i in range(len(transform) - 1):
        cyclic_rotations = join(sorted(cyclic_rotations), transform)

    return next(filter(lambda x: x.endswith('$'), cyclic_rotations))


def main(transform):
    print(inverse(transform))


if __name__ == "__main__":
    main("TTCCTAACG$A")

'''
Reconstruct a string from its Burrows-Wheeler transform.
Given: A string Transform (with a single "$" sign).
Return: The string Text such that BWT(Text) = Transform.
Output:
TACATCACGT$
'''
