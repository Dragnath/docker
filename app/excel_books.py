import xlrd
from collections import OrderedDict
import simplejson as json

file = './Books.xlsx'

wb = xlrd.open_workbook(file)
sh = wb.sheet_by_index(0)

books_list = []

for rownum in range(2, sh.nrows):
    books = OrderedDict()
    row_values = sh.row_values(rownum)
    books['ID'] = int(row_values[0])
    books['Name'] = row_values[1]
    books['Surname'] = row_values[2]
    books['Title'] = row_values[3]
    books['Series'] = row_values[4]
    books['Genre'] = row_values[5]
    books_list.append(books)

books_json = json.dumps(books_list)

