# coding=utf8

import sys

sys.path.append('../')
sys.path.append('../utils')
sys.path.append('../script')

from utils.get_json_from_page import get_json_by_retry


def crawl_and_save(date_str):
    link = 'http://www.shfe.com.cn/data/dailydata/kx/pm%s.dat' % date_str
    # print('linke = %s' % link)
    ret_json = get_json_by_retry(link)
    if not ret_json:
        print('The date [%s] is not work day.' % date_str)
        return None
    # print(ret_json)

    csv_path = '../csv/result_%s.csv' % date_str
    with open(csv_path, 'a', encoding='utf-8-sig') as f:
        f.write('商品名称' + ',')
        f.write('合约代码' + ',')
        f.write('名次' + ',')
        f.write('期货公司会员简称' + ',')
        f.write('成交量' + ',')
        f.write('比上交易日增减' + ',')
        f.write('期货公司会员简称' + ',')
        f.write('成交量' + ',')
        f.write('比上交易日增减' + ',')
        f.write('期货公司会员简称' + ',')
        f.write('成交量' + ',')
        f.write('比上交易日增减' + ',')
        f.write('\n')

        for line in ret_json.get('o_cursor'):
            if not str(line.get('RANK', '')) == '999':
                f.write(line.get('PRODUCTNAME', '') + ',')
                f.write(line.get('INSTRUMENTID', '') + ',')

                f.write(str(line.get('RANK', '')) + ',')

                f.write(str(line.get('PARTICIPANTABBR1', '')) + ',')
                f.write(str(line.get('CJ1', '')) + ',')
                f.write(str(line.get('CJ1_CHG', '')) + ',')

                f.write(str(line.get('PARTICIPANTABBR2', '')) + ',')
                f.write(str(line.get('CJ2', '')) + ',')
                f.write(str(line.get('CJ2_CHG', '')) + ',')

                f.write(str(line.get('PARTICIPANTABBR3', '')) + ',')
                f.write(str(line.get('CJ3', '')) + ',')
                f.write(str(line.get('CJ3_CHG', '')) + ',')
                f.write('\n')
    return True


def main(date_str):
    crawl_and_save(date_str)


if __name__ == '__main__':
    date_str = sys.argv[1]
    if not len(date_str) == 8:
        print('The date string is invalid.')
    else:
        print('date_str = %s' % date_str)
        main(date_str)
