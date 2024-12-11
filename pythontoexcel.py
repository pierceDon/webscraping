import openpyxl as xl
from openpyxl.styles import Font

wb = xl.Workbook()
ws = wb.active
ws.title = 'First Sheet'

# create a new worksheet
wb.create_sheet(index=1,title='Second Sheet')

ws['A1'] = 'Invoice'

fontobj = Font(name='Times New Roman', size=24, bold=True)

ws['A1'].font = fontobj

ws['A2'] = 'Tires'
ws['A3'] = 'Brakes'
ws['A4'] = 'Alignmment'

ws['B2'] = 450
ws['B2'] = 225.50
ws['B2'] = 150

ws['A8'] = 'Total'

ws['A8'].font = fontobj

ws.column_dimensions['A'].width = 25

ws.merge_cells('A1:B1')

ws['B8'] = '=SUM(B2:B7)'


# write_sheet = wb['Second Sheet']

# read_wb = xl.load_workbook('ProduceReport.xlsx')