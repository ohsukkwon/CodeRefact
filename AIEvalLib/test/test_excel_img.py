from openpyxl import load_workbook
from openpyxl.drawing.image import Image

T_workbook = load_workbook("result.xlsx" , data_only=True )
T_worksheet = T_workbook.active
for row in T_worksheet.values:
    for cell in row:
        if cell is None :
            continue
        else:
            print(cell)


img = Image('res/2.jpg')

T_worksheet.add_image(img, 'I2')

T_workbook.save('result_img.xlsx')