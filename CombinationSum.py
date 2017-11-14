from unittest import (TestCase, main)


class CombinationSum(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        DFS: sort the candidate numbers first. push single element sets into the stack first: [2], [3], [6], [7]. then take out the last set, try all other candidates that are less than or equal to the last element in the set, augment it into a new combination and push into the stack (but still discard the original last set), continue until the combination stack is empty
        """
        n = len(candidates)
        candidates.sort()

        combinationStack = [[]]
        answerList = []

        while len(combinationStack):
            currentCombination = combinationStack.pop()
            currentSum = sum(currentCombination)
            if currentSum > target:
                raise ValueError(
                    'our stack has a combination {c} whose sum is {s}, exceeding {t}; this is unexpected!'.format(
                        c=' '.join([str(x) for x in currentCombination]), s=currentSum, t=target))
            elif currentSum == target:
                answerList.append(currentCombination)
            elif len(currentCombination) == 0:
                # if the current combination is empty, we use every candidate to augment it into a new combination and push into the combination stack
                for elem in candidates:
                    if elem > target:
                        break

                    combinationStack.append([elem])
            else:
                # if the current combination is not empty, we use every candidate that is <= the last element in the current combination to augment it into a new combination and push into the combination stack
                largestAllowedCandidate = currentCombination[-1]

                for elem in candidates:
                    if currentSum + elem > target or elem > largestAllowedCandidate:
                        break

                    newCombination = [c for c in currentCombination]
                    newCombination.append(elem)
                    combinationStack.append(newCombination)

        return answerList


class TestGroupAnagram(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
        'test_candidates': [],
        'test_target': 1,
        'test_output': [],
    }, {
        'test_candidates': [2],
        'test_target': 2,
        'test_output': [[2]],
    }, {
        'test_candidates': [2],
        'test_target': 1,
        'test_output': [],
    }, {
        'test_candidates': [2],
        'test_target': 3,
        'test_output': [],
    }, {
        'test_candidates': [2,3],
        'test_target': 6,
        'test_output': [[3,3], [2,2,2]],
    }, {
        'test_candidates': [2, 3, 6, 7],
        'test_target': 7,
        'test_output': [[7], [2, 2, 3]],
    }
        ]

    def test_result(self):
        obj = CombinationSum()

        for test_case in self.test_object:
            answer = obj.combinationSum(test_case['test_candidates'], test_case['test_target'])

            answer.sort(key=len)
            for item in answer:
                item.sort()

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()

