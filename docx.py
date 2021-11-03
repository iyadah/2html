import mammoth

custom_styles = "b => i"

with open("docx.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('docx.html', 'w') as html_file:
        html_file.write(text)
