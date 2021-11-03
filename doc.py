import mammoth
import os
os.system('textutil -convert docx doc.doc')
custom_styles = "b => i"
with open("doc.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('doc.html', 'w') as html_file:
        html_file.write(text)
