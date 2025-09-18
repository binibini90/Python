# -*- coding: utf-8 -*-
class OutRangeError(Exception):
    def __init__(self, strname):
        super(OutRangeError, self).__init__(strname)
    def show_info(self):
        return '사용자가 정의한 예외입니다.'

try : 
    number = 100
    if not 0 <= number <= 10 :
        raise OutRangeError('0~10사이의 값이 아닙니다.')
    int('asda')
except OutRangeError as e:
    print('에러발생: {}'.format(e))
except ValueError as e:
    print('값에러', e)