from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook(
    
sheet = wb['Report']

sheet['A1'] = "Sales Report"
sheet['A2'] = "January"
sheet['A1'].font = Font('Arial', bold=True, size=24)
sheet['A2'].font = Font('Times', bold=True, size=10)

wb.save('barchartwithstyle.xlsx')
