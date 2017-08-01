from unittest import (TestCase, main)


class MaxProdOfThree(object):
    def maximumKProduct(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        if k <= 0:
            raise ValueError('the number k cannot be non-positive!')

        if len(nums) < k:
            raise ValueError('the length of the array cannot be smaller than k!')

        # keep track of the max and min of k (<=3) elements among the first n, update dynamically
        maxProd = -float('Inf')
        prevExtreme = [{'max': None, 'min': None, 'exists': False}] * k

        for index, value in enumerate(nums):
            thisExtreme = []
            for i in range(0, k):
                thisExists = False
                if i == 0:
                    thisExists = True
                    if prevExtreme[0]['exists']:
                        ExtremeMax = max(prevExtreme[0]['max'], value)
                        ExtremeMin = min(prevExtreme[0]['min'], value)
                    else:
                        ExtremeMax = value
                        ExtremeMin = value
                else:
                    if prevExtreme[i]['exists']:
                        thisExists = True
                        ExtremeMax = max(prevExtreme[i]['max'], prevExtreme[i - 1]['max'] * value, prevExtreme[i - 1]['min'] * value)
                        ExtremeMin = min(prevExtreme[i]['min'], prevExtreme[i - 1]['max'] * value, prevExtreme[i - 1]['min'] * value)
                    elif prevExtreme[i-1]['exists']:
                        thisExists = True
                        ExtremeMax = max(prevExtreme[i - 1]['max'] * value,
                                         prevExtreme[i - 1]['min'] * value)
                        ExtremeMin = min(prevExtreme[i - 1]['max'] * value,
                                         prevExtreme[i - 1]['min'] * value)
                    else:
                        thisExists = False
                        ExtremeMax = None
                        ExtremeMin = None
                if thisExists:
                    if ExtremeMax == None:
                        raise ValueError('when exists, extreme max should not be None')
                    if ExtremeMin == None:
                        raise ValueError('when exists, extreme min should not be None')
                    thisExtreme.append({'max': ExtremeMax, 'min': ExtremeMin, 'exists': True})
                else:
                    thisExtreme.append({'max': None, 'min': None, 'exists': False})
            if thisExtreme[k-1]['exists']:
                maxProd = max(maxProd, thisExtreme[k - 1]['max'])

            prevExtreme = thisExtreme

        if maxProd == -float('Inf'):
            raise ValueError('should not expect a negative infinite answer!')

        return maxProd

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maximumKProduct(nums, 3)


class TestMaxProdOfThree(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_nums': [-1,-2,-3],
            'test_output': -6
        }, {
            'test_nums': [722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786],
            'test_output': 943695360
        }]

    def test_result(self):
        obj = MaxProdOfThree()

        for test_case in self.test_object:
            result = obj.maximumProduct(test_case['test_nums'])

            self.assertEqual(test_case['test_output'], result)

if __name__ == '__main__':
    main()
