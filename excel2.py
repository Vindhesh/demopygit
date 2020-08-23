import xlsxwriter

workbook = xlsxwriter.Workbook('excel2.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
content = ["Vindhesh", "Aditya", "Nikita", "Nafeesa"]

for item in content:
    worksheet.write(row, column, item)
    row += 1

workbook.close()    