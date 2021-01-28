import os
import re

"""
    中文数字转阿拉伯数字
"""


class ConvertInt:
    char_dict = {
        u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4,
        u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9, u'十': 10,
        u'百': 100, u'千': 10 ** 3, u'万': 10 ** 4, u'〇': 0,
        u'壹': 1, u'贰': 2, u'叁': 3, u'肆': 4, u'伍': 5,
        u'陆': 6, u'柒': 7, u'捌': 8, u'玖': 9, u'拾': 10,
        u'佰': 100, u'仟': 10 ** 3, u'萬': 10 ** 4, u'亿': 10 ** 8, u'億': 10 ** 8,
        u'幺': 1, u'两': 2,
        u'０': 0, u'１': 1, u'２': 2, u'３': 3, u'４': 4,
        u'５': 5, u'６': 6, u'７': 7, u'８': 8, u'９': 9
    }

    @classmethod
    def convert_to_int(cls, temp, unit):
        pos = 0

        temp_len = len(temp)
        if temp_len <= 2 and temp[0] == 10:  # 十到十九需要单独转换
            for i in temp:
                pos += i
            return pos * unit

        for i in range(temp_len):
            if temp[i] > 9 and temp[i - 1] != 0:
                pos += temp[i] * temp[i - 1]

        if temp[-1] < 10:
            pos += temp[-1]

        return pos * unit

    @classmethod
    def split_unit(cls, temp, unit):
        number = []
        while True:
            if temp[0] != unit:
                number.append(temp.pop(0))
                continue
            temp.pop(0)
            return cls.convert_to_int(number, unit)

    @classmethod
    def main(cls, old_str):
        res = ''
        pos = 0

        com = re.compile('[十百千万]')
        if re.findall(com, old_str):
            temp = [cls.char_dict[i] for i in old_str]

            if 10 ** 8 in temp:
                pos += cls.split_unit(temp, 10 ** 8)

            if 10 ** 4 in temp:
                pos += cls.split_unit(temp, 10 ** 4)

            if temp:
                pos += cls.convert_to_int([i for i in temp], 1)

            return str(pos)

        else:
            for i in old_str:
                res += str(cls.char_dict[i])

        return res


if __name__ == '__main__':
    print(ConvertInt.main("一千七百八十二"))
