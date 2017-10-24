from unittest import (TestCase, main)


def comp(pair1, pair2):
    """
    :type pair1: (int, str) pair2: (int, str)
    :rtype: int
    """
    # compare a tuple of length and string
    length1, lex1 = pair1
    length2, lex2 = pair2
    if length1 < length2:
        return -1
    elif length1 > length2:
        return 1
    elif lex1 < lex2:
        return -1
    elif lex1 > lex2:
        return 1
    else:
        return 0


def findPrevIndex(array, target):
    """
   :type array: List[(int, str)] target: (int, str)
   :rtype: (int, bool)
   """
    # array of pairs of length, lex
    # if found, return the index; if not found, return the largest index below target; return -1 if target is the smallest
    # return index, whether or not found exactly

    low = -1
    high = len(array)

    if high == 0:
        return (-1, False)  # empty array always return -1

    while low < high - 1:
        mid = int((low + high + 1) / 2)  # guaranteed mid >= 0, low < mid < high
        if comp(array[mid], target) == 0:
            return (mid, True)
        elif comp(array[mid], target) < 0:
            low = mid
        else:
            high = mid

    # guaranteed low <= ans < high, now high = low + 1, so ans = low
    return (low, False)


class GroupAnagram(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = []
        sortedMarks = []  # sorted by lexicography order (length, lex) to make the search procedure quicker

        for item in strs:
            lenItem = len(item)
            sortedItem = sorted(item)

            index, found = findPrevIndex(sortedMarks, (lenItem, sortedItem))

            # insert into index + 1
            if found:
                groups[index].append(item)
            else:
                groups.insert(index + 1, [item])
                sortedMarks.insert(index + 1, (lenItem, sortedItem))

        return groups

class TestGroupAnagram(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [
{
    'test_strs': ["eat", "tea", "tan", "ate", "nat", "bat"],
    'test_output': [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
}
        ]

    def test_result(self):
        obj = GroupAnagram()

        for test_case in self.test_object:
            answer = obj.groupAnagrams(test_case['test_strs'])

            castedAnswer = ['-'.join(sorted(x)) for x in answer]
            castedOutput = ['-'.join(sorted(x)) for x in test_case['test_output']]

            self.assertEqual(set(castedAnswer), set(castedOutput))

if __name__ == '__main__':
    main()

