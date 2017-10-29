def get_mapping(transform, position):
    transform = [(transform[i], i) for i in range(len(transform))]
    transform = sorted(transform)
    for i in range(len(transform)):
        if transform[i][1] == position:
            return i


def main(data_as_string):
    transform, position = data_as_string.split()
    print(get_mapping(transform, int(position)))


if __name__ == "__main__":
    main('''T$GACCA
3''')

'''
Given: A string Transform and an integer i.
Return: The position LastToFirst(i) in FirstColumn in the Burrows-Wheeler matrix if LastColumn = Transform.
Output:
1
'''
