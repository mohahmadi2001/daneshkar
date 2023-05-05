
"""
module providing valid_postal_code function
"""
# def vaild_postal_code(postal_code: list) -> list:
#     """
#     This function is created to validate
#     and correct the postal code
#     """
#     valid=[]
#     for code in postal_code:
#         if len(code) != 11:
#             continue
#         if code[5] != '-':
#             continue
#         for i in range(10):
#             if not code[i].isdigit():
#                 continue
#         valid.append(code)
#     return valid

# postal_codes = ["12345-6789", "9876-54321", "ABCD-12345", "67890-12345", "12345-67890"]
# valid_postal_codes = vaild_postal_code(postal_codes)
# print(valid_postal_codes)

def is_valid_zip_code(zip_code: str) -> bool:
   
    return (
    isinstance(zip_code, str) 
    and len(zip_code) == 11
    and zip_code[5] == '-'
    and zip_code[:5].isdigit()
    and zip_code[6:].isdigit()
    )

# print(
# is_valid_zip_code('12345-hello'),
# is_valid_zip_code('12345-43215'),
# is_valid_zip_code(12345),
# is_valid_zip_code('12345-123'),
# is_valid_zip_code('1234-12345'),
# is_valid_zip_code('1234512345'),
# is_valid_zip_code('123-12345'),
# is_valid_zip_code('123.4-hello'),
# )

zip_codes =[
'12345-43215',
12345,
'12345-123',
'1234-12345',
'1234512345',
'123-12345',
'123.4-hello',
'12345-hello',
' 1234-1234 '
]
# result = []
# for zip_code in zip_codes:
#     if is_valid_zip_code(zip_code):
#         result.append(zip_code)
# result = [zip_code for zip_code in zip_codes if is_valid_zip_code(zip_code)]
# print(result)

print(list(filter(is_valid_zip_code,zip_codes)))