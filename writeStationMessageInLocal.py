from urlDownload import download
import re
import sqlite3

def filter_list(str1):
    return re.match('[\u4e00-\u9fa5]{2,5}|[A-Z]{2,5}',str1)
    
def fun(l):
    n = 2
    er = []
    flag = True
    while(n < len(l)):
        if n%2 == 0:
            if re.match('[\u4e00-\u9fa5]{2,5}',l[n]):
                pass
            else:
                er.append(n)
        else:
            if re.match('[A-Z]{2,5}',l[n]):
                pass
            else:
                er.append(n)
        n += 1
    return er
def get_stationMessage():
    req = download('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047')
    html = req.read().decode('utf-8')
    l = html.split('|')
    new_l = list(filter(filter_list, l))
    n = 0
    stationMessage = {}
    new_l.remove('KEQ')
    new_l.remove('JUQ')
    new_l.remove('SOB')
    '''while(n < len(new_l)):
        stationMessage[new_l[n]] = new_l[n+1]
        n += 2'''
    return new_l
def main():
    station = get_stationMessage()
    conn = sqlite3.connect('stationMessage.db3')
    if conn:
        n = 0
        cu = conn.cursor()
        while(n < len(station)):
            insert_into = "insert into stationMessage values('{}','{}')".format(station[n],station[n+1])
            print(insert_into)
            cu.execute(insert_into)
            conn.commit()
            n += 2
if __name__ == '__main__':
    main() 