# -*- coding:utf8 -*-
class Solution:
    def maxValue_failed(self, _str):
        left_sum = 0
        right_sum = 0
        max_value =0
        left_mul = 1
        right_mul = 1
        max_left = 0
        max_right = 0
        list_str = list(_str)
        for i in range(0, len(list_str)-1):
            if '0' in list_str:
                list_str.remove('0')
        #print list_str
        if len(list_str) == 0 : return 0
        if len(list_str) == 1 : return list_str[0]

        if list_str[0] == '1':
            list_str[1] = str(int(list_str[1]) + 1)
            list_str.remove(list_str[0])
        print list_str
        print len(list_str)
        if list_str[len(list_str)-1] == '1':
            list_str[len(list_str)-1-1] = str(int(list_str[len(list_str)-1-1]) + 1)
            list_str.pop()

        #print list_str

        #_str =''.join(i for i in list_str)

        print list_str
        for i in range(1, len(list_str)):
            for j in range(0, i):
                left_sum = left_sum + int(list_str[j])
                left_mul = left_mul * int(list_str[j])
                max_left = max(left_sum, left_mul, max_left)
                #print 'max_left: ' + str(max_left)


            for p in range(i, len(list_str)):
                right_sum = right_sum + int(list_str[p])
                right_mul = right_mul * int(list_str[p])
                max_right = max(right_sum, right_mul, max_right)
                #print 'max_right: ' + str(max_right)
            max_value = max_left * max_right
            print max_value , max_left, max_right
            if max_left* max_right > max_value:
                max_value =  max_left * max_right
            left_sum, right_sum, left_mul, right_mul, max_right, max_left = 0, 0, 1, 1,0, 0

        return max_value


    def maxValue(self, _str):
        item = list(_str)
        item_len = len(item)
        N = 5
        for i in range(0, item_len):
            item[i] = int(item[i])

        arr_max = [[0 for i in range(N)] for i in range(N)]
        mmax = 0

        for i in range(0, item_len):
            arr_max[i][i] = item[i]

        for i in range(1, item_len):
            for j in range(0, item_len):
                for k in range(0, i):
                    print 'i=' + str(i) + '  j=' +str(j) + '   k=' + str(k)
                    print arr_max
                    arr_max[j][j+i] = max(arr_max[j][j+i], arr_max[j][j+k] * arr_max[j+k+1][j+i])
                    print arr_max
                    arr_max[j][j+i] = max(arr_max[j][j+i], arr_max[j][j+k] + arr_max[j+k+1][j+i])
                    print arr_max
                    mmax = max(mmax, arr_max[j][j+i])


        print mmax



if __name__ == "__main__":
    s = Solution()
    _str = "123"
    print(s.maxValue(_str))