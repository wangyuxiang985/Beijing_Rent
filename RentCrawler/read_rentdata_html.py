# coding=utf-8

import sqlite3

def create_html(result_file, conn):

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rent ORDER BY itemtime DESC ,crawtime DESC')
    values = cursor.fetchall()
    # export to html file
    file = open(result_file, 'w')
    with file:
        file.writelines('<html><head>')
        file.writelines('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
        file.writelines('<title>Rent Crawer Result</title></head><body>')
        file.writelines('<table rules=all>')
        file.writelines('<h1>' + '租房信息' + '</h1>')
        file.writelines(
            '<tr><td>索引Index</td><td>标题Title</td><td>链接Link</td><td>发帖时间Page Time</td><td>抓取时间Crawl Time</td><td>作者Author</td><td>关键字Keyword</td><td>来源Source</td></tr>')
        for row in values:
            file.write('<tr>')
            for member in row:
                file.write('<td>')
                member = str(member)
                if 'http' in member:
                    file.write('<a href="' + member + '" target="_black">' + member + '</a>')
                else:
                    file.write(member)
                file.write('</td>')
            file.writelines('</tr>')
        file.writelines('</table>')
        file.writelines('</body></html>')
    cursor.close()

if __name__ == '__main__':
    create_html("result/rentdata_result.html", sqlite3.connect("result/rentdata.db3"))