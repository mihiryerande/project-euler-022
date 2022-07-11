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

from typing import List

# Delta to convert from ordinal char value to uppercase letter's number value
ORD_BASE = ord('A') - 1


def read_names(filename: str) -> List[str]:
    """
    Returns the list of names from `filename`.

    Args:
        filename (str): File containing list of names

    Returns:
        (List[str]): Names from `filename`

    Raises:
        AssertError: if incorrect args are given
    """
    with open(filename, 'r') as f:
        names = [name.strip('"').upper() for name in f.readline().strip().split(',')]
        names.sort()
        return names


def alphabet_score(name: str) -> int:
    """
    Given an uppercase name,
      return the 'alphabet score' of the name,
      which is the sum of the number values of the constituent letters.

    Args:
        name (str): A name

    Returns:
        (int): Alphabet score of name

    Raises:
        AssertError: if incorrect args are given
    """
    global ORD_BASE
    return sum(map(lambda c: ord(c) - ORD_BASE, list(name)))


def main(filename: str) -> int:
    """
    Returns the sum of all the 'name scores' in the given `filename`.

    Args:
        filename (str): File containing names

    Returns:
        (int): Sum of all name scores in `filename`

    Raises:
        AssertError: if incorrect args are given
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
