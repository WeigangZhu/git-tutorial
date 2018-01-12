#!python3

'''
the file is about how to use python to deal with excel
'''

'''

xlrd和xlwt两个模块分别用来读Excel和写Excel，只支持.xls和.xlsx格式，Python不默认包含。这两个模块之间相互独立，没有依赖关系，也就是说可以根据需要只安装其中一个。

xlutils模块可以同时读写一个已存在的Excel文件，依赖于xlrd和xlwt。
使用xlrd读Excel
xlrd提供的接口比较多，常用的如下：

open_workbook()打开指定的Excel文件，返回一个Book对象。

通过Book对象可以得到各个Sheet对象（一个Excel文件可以有多个Sheet，每个Sheet就是一张表格）。

Book.nsheets返回Sheet的数目。

Book.sheets()返回所有Sheet对象的list。

Book.sheet_by_index(index)返回指定索引处的Sheet。相当于Book.sheets()[index]。

Book.sheet_names()返回所有Sheet对象名字的list。

Book.sheet_by_name(name)根据指定Sheet对象名字返回Sheet。

通过Sheet对象可以获取各个单元格，每个单元格是一个Cell对象。

Sheet.name返回表格的名称。

Sheet.nrows返回表格的行数。

Sheet.ncols返回表格的列数。

Sheet.row(r)获取指定行，返回Cell对象的list。

Sheet.row_values(r)获取指定行的值，返回list。

Sheet.col(c)获取指定列，返回Cell对象的list。

Sheet.col_values(c)获取指定列的值，返回list。

Sheet.cell(r, c)根据位置获取Cell对象。

Sheet.cell_value(r, c)根据位置获取Cell对象的值。

Cell.value返回单元格的值。

'''

import xlrd

wb = xlrd.workbook('test.xls')

# 打印每张表的最后一列
# 方法1
for s in wb.sheets():
    print "== The last column of sheet '%s' ==" % (s.name)
    for i in range(s.nrows):
        print s.row(i)[-1].value

# 方法2
for i in range(wb.nsheets):
    s = wb.sheet_by_index(i)
    print "== The last column of sheet '%s' ==" % (s.name)
    for v in s.col_values(s.ncols - 1):
        print v

# 方法3
for name in wb.sheet_names():
    print "== The last column of sheet '%s' ==" % (name)
    s = wb.sheet_by_name(name)
    c = s.ncols - 1
    for r in range(s.nrows):
        print s.cell_value(r, c)


'''

相对来说，xlwt提供的接口就没有xlrd那么多了，主要如下：

Workbook()是构造函数，返回一个工作簿的对象。

Workbook.add_sheet(name)添加了一个名为name的表，类型为Worksheet。

Workbook.get_sheet(index)可以根据索引返回Worksheet（前提是已经添加到Workbook中了）。

Worksheet.write(r, c, vlaue)是将vlaue填充到指定位置。

Worksheet.row(n)返回指定的行。

Row.write(c, value)在某一行的指定列写入value。

Worksheet.col(n)返回指定的列。

通过对Row.height或Column.width赋值可以改变行或列默认的高度或宽度。（单位：0.05 pt，即1/20 pt）

Workbook.save(filename)保存文件。

有这么几点需要注意一下：

1 xlwt模块最大能写65535行，256列，如果超过这个范围，程序运行就会出现错误，那么可能需要找一些其他方法来解决。如果我们只注重数据的处理，那么可以采用csv模块来替代。

2 文件默认的编码方式是ascii，如果要改变编码方式，指定Workbook()的encoding参数，如 
Workbook(encoding='utf-8')。

3 表的单元格默认是不可重复写的，如果有需要，在调用add_sheet()的时候指定参数cell_overwrite_ok=True即可。


'''

import xlwt

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet_test', cell_overwrite_ok=True)

sheet.write(0, 0, 'Python')
sheet.row(0).write(1, 'is')
sheet.write(0, 2, 'very very useful.')
sheet.col(2).width = 4000

book.save('test.xls')

'''

除了基本的写入数据之外，xlwt还可以改变单元格格式。上面的write方法允许接受一个XFStyle（意为eXcel File Style）类型的参数，放在最后的位置。easyxf()可以快速生成一个XFStyle对象。

这里简单介绍一下其用法：
'''

import datetime, xlwt

# ... some code

font = xlwt.Font()
font.name = 'Arial'
font.height = 240 # font size: 12pt

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 0x0A

style = xlwt.XFStyle()
style.num_format_str = '0.00%'
style.font = font
style.pattern = pattern

a = 8
b = 10
# 以百分比的形式显示，保留两位小数
sheet.write(0,3, float(a) / b, style)

# 显示日期
sheet.row(0).write(4, datetime.date(2016,8,14), xlwt.easyxf(
        'font: name Arial, height 240;'
        'pattern: pattern squares, fore_color red;',
        num_format_str = 'YYYY-MM-DD'
    )
)

'''

使用xlutils修改Excel
通过xlrd.open_workbook()打开的Book对象是只读的，不能直接对其进行修改操作，而xlwt.Workbook()返回的Workbook对象虽然可写，但是写的时候只能从零写起，那如果要修改一个已经存在的Excel该怎么办呢？

庆幸的是，在xlutils.copy中有个copy()方法，我们可以将一个xlrd.Book对象转化为一个xlwt.Workbook对象，这样我们就可以直接对已存在的Excel文件进行修改了。

用法举例如下：

import xlrd
import xlutils.copy

book = xlrd.open_workbook('test.xls', formatting_info=True)
wtbook = xlutils.copy.copy(book)
wtsheet = wtbook.get_sheet(0)
wtsheet.write(0, 0, 'Ok, changed!')
wtbook.save('test.xls')

要注意的是：

调用xlrd.open_workbook()时，如果不指定formatting_info=True，那么修改后整个文档的样式会丢失。对一个单元格进行write操作时，如果不指定样式，也会将原来的样式丢失。

注意调用copy()的方法。也可以通过声明from xlutils.copy import copy来直接调用copy()。

'''
