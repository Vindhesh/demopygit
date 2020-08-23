





import xlsxwriter

workbook = xlsxwriter.Workbook('excel3.xlsx')
worksheet = workbook.add_worksheet("My Sheet")

scores = (
    ['ankit', '1000'],
    ['Rahul', '100'],
    ['Priya', '300'],
    ['Harshita', '50'],
)
row = 0
col = 0

for name, score in scores:
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score)
    row += 1

workbook.close()