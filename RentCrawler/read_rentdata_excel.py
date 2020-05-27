# coding=utf-8

import sqlite3
import xlwt

def create_excel(excel_file, conn):

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rent ORDER BY itemtime DESC, crawtime DESC')
    values = cursor.fetchall()

    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('北京租房信息')
    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style
    worksheet.write_merge(0, 0, 0, 7, '北京租房信息统计', style)
    worksheet.write(1, 0, '索引Index')
    worksheet.write(1, 1, '标题Title')
    worksheet.write(1, 2, '链接Link')
    worksheet.write(1, 3, '发帖时间Page Time')
    worksheet.write(1, 4, '抓取时间Crawl Time')
    worksheet.write(1, 5, '作者Author')
    worksheet.write(1, 6, '关键字Keyword')
    worksheet.write(1, 7, '来源Source')

    # 参数对应 行, 列, 值
    # worksheet.write(1, 0, label='this is test')
    i = 2
    j = 0
    max_len = [10, 0, 0, 0, 0, 0, 0, 0]
    for row in values:
        for member in row:
            member = str(member)
            if j == 2:
                worksheet.write(i, j, xlwt.Formula('HYPERLINK("%s")' % member))
            elif j == 8:
                continue
            else:
                worksheet.write(i, j, member)

            if max_len[j] < 256 * len(member):
                max_len[j] = 256 * len(member)
            j += 1
        j = 0
        i += 1
    for i in range(len(max_len)):
        worksheet.col(i).width = max_len[i]
    # worksheet.col(0).width = 10
    # 保存
    workbook.save(excel_file)

if __name__ == '__main__':
    create_excel("result/rentdata_result.xls", sqlite3.connect("result/rentdata.db3"))