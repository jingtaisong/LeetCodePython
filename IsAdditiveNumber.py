from unittest import (TestCase, main)


class IsAdditiveNum(object):
    def isAdditiveNumber(self, num):
        """
        iteratively populate two lists: success and prepare 
        success[i] stores a list of maps {first, second} where first and second are the last two elements in an additive sequence up to the i-th element
        prepare[i] stores a list of maps {first, second} where first and second combine to produce the segment up to the i-th element
        time complexity O(n^2)
        space complexity O(n^2)
        :type num: str
        :rtype: bool
        """
        N = len(num)

        if N <= 2:
            return False

        # start with the success and prepare lists at the 2nd element
        success = [[], []]
        prepare = [[], [{'first': int(num[0]), 'second': int(num[1])}]]

        index = 2
        while index < N:
            this_success = []
            this_prepare = []

            for marker in range(0, index):
                if num[marker+1] == '0' and marker != index - 1:   # cannot split into a segment starting with zero unless the segment is a single digit
                    continue

                this_segment = int(num[(marker + 1):(index + 1)])

                # check the success instances up to marker
                for success_instance in success[marker]:
                    if success_instance['first'] + success_instance['second'] == this_segment:
                        this_success.append({'first': success_instance['second'], 'second': this_segment})

                # check the prepare instances up to marker
                for prepare_instance in prepare[marker]:
                    if prepare_instance['first'] + prepare_instance['second'] == this_segment:
                        this_success.append({'first': prepare_instance['second'], 'second': this_segment})

                # produce a prepare instance as long as the first segment is not like '0%'
                if num[0] != '0' or marker == 0:
                    this_prepare.append({'first': int(num[0:(marker + 1)]), 'second': this_segment})

            #print('\n\nat index {i}:\nthe success instances are\n'.format(i=index))
            #print(this_success)
            #print('the prepare instances are\n')
            #print(this_prepare)

            success.append(this_success)
            prepare.append(this_prepare)
            index += 1

        return len(success[N - 1]) > 0

class TestAdditiveNumber(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [{
            'test_num': '112358',
            'test_output': True
        }, {
            'test_num': '199100199',
            'test_output': True
        }, {
            'test_num': '1023',
            'test_output': False
        }, {
            'test_num': '000',
            'test_output': True
        }, {
            'test_num': '11011',
            'test_output': True
        }, {
            'test_num': '0235',
            'test_output': False
        }]

    def test_result(self):
        obj = IsAdditiveNum()

        for test_case in self.test_object:
            output = obj.isAdditiveNumber(test_case['test_num'])

            self.assertEqual(output, test_case['test_output'])

if __name__ == '__main__':
    main()
