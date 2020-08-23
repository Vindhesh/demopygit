first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
mobile = input('enter your mobile number: ')
email_id = input('Enter your email id: ')

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
bold=workbook.add_format({'bold': True})


worksheet.write('A1', 'First Name')
worksheet.write('B1', 'Last Name')
worksheet.write('C1', 'Mobile')
worksheet.write('D1', 'Email id')
worksheet.write('A2', first_name)
worksheet.write('B2', last_name)
worksheet.write('C2', mobile)
worksheet.write('D2', email_id)

workbook.close()