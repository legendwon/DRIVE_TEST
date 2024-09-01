import gspread

# json 파일이 위치한 경로를 값으로 줘야 합니다.
json_file_path = r"C:\Users\won33\Desktop\CHO_TEST\SHEET_API\test-1-434206-6c192b145f78.json"
gc = gspread.service_account(json_file_path)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1S1yXz8d7ltAXrgnyyHPVu4NH-y62G6oMDsu1YtZ_iW0/edit?usp=sharing"
doc = gc.open_by_url(spreadsheet_url)


worksheet = doc.worksheet("시트1")
# worksheet.update('a1','자동화 끝!')

cell_data = worksheet.acell('B1').value
print(cell_data)

row_data = worksheet.row_values(1)
print(row_data)

range_list = worksheet.range('A1:D3')
for cell in range_list:
    print(cell.value)


