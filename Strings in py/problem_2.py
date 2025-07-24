#to fill a letter template
letter = '''Dear <|Name|>
you are selected
<|Date|>'''
print(letter.replace("<|Name|>", "hari,").replace("<|Date|>", "05-april-2025").replace("selected","not selected"))
