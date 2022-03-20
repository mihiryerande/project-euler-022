# Problem 22:
#     Names Scores
#
# Description:
#     Using names.txt (right click and 'Save Link/Target As...'),
#       a 46K text file containing over five-thousand first names,
#       begin by sorting it into alphabetical order.
#
#     Then working out the alphabetical value for each name,
#       multiply this value by its alphabetical position in the list to obtain a name score.
#
#     For example, when the list is sorted into alphabetical order,
#       "COLIN", which is worth 3 + 15 + 12 + 9 + 14 = 53,
#       is the 938th name in the list.
#
#     So, COLIN would obtain a score of 938 × 53 = 49714.
#
#     What is the total of all the name scores in the file?

# Delta to convert from ordinal char value to uppercase letter's number value
ORD_BASE = ord('A') - 1


def read_names(filename):
    """
    Returns the list of names from `filename`

    Args:
        filename (str): File containing list of names

    Returns:
        List[str] of names from `filename`
    """
    with open(filename, 'r') as f:
        names = [name.strip('"').upper() for name in f.readline().strip().split(',')]
        names.sort()
        return names


def alphabet_score(name):
    """
    Given an uppercase name,
      return the 'alphabet score' of the name,
      which is the sum of the number values of the constituent letters.

    Args:
        name (str): A name

    Returns:
        Alphabet score of name
    """
    global ORD_BASE
    return sum(map(lambda c: ord(c) - ORD_BASE, list(name)))


def main(filename):
    """
    Returns the sum of all the 'name scores' in the given `filename`.

    Args:
        filename (str): Name of file containing names

    Returns:
        Sum of all name scores in `filename`
    """
    assert type(filename) == str

    names = read_names(filename)

    total = 0
    for i, name in enumerate(names):
        total += (i+1) * alphabet_score(name)
    return total


if __name__ == '__main__':
    names_file = 'names.txt'
    total_score = main(names_file)
    print('Total of all Name Scores in `{}`:'.format(names_file))
    print('  {}'.format(total_score))
