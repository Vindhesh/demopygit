first_name=input(f'Enter your first name: ')
last_name = input(f'Enter your last name: ')
mobile = input(f'Enter your mobile number: ')
email_id = input(f'Enter your email id: ')

import xlsxwriter

workbook = xlsxwriter.Workbook('temp.xlsx')

worksheet = workbook.add_worksheet()
worksheet.write('A1', first_name)
worksheet.write('B1', last_name)
worksheet.write('C1', mobile)
worksheet.write('D1', email_id)

workbook.close()