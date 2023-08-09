import xlrd

loc= "C:\\Users\\hp\\OneDrive\\Desktop\\Data...fun.xlsx"
wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)  # choose sheet 1 by index 0
print(sheet.cell_value(3, 3))  # 3,3 index value will be printed

# print no. of row and colpoumns
print(sheet.ncols)
print(sheet.nrows)

for i in range(sheet.ncols):  # wiill print row 0
    print(sheet.cell_value(0, i))

# print row and coloumn
print(sheet.row_values(1))
print(sheet.col_values(1))