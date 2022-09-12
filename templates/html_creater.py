from controller import array, file_name
import time
# Из массива формирует html файл и записывает его в папку export с именем файла: текущая дата и время.html
def new_html():
    mas = array(file_name())
    style = '<style>table{font-family:arial,sans-serif;border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;text-align:left;padding:8px}tr:nth-child(even){background-color:#ddd}</style>'
    html = '<html>\n  <head>{}</head>\n  <body>\n'.format(style)
    html += '<h2>HTML Table</h2>'
    html += '<table>\n<tr><th>ID</th><th>Name</th><th>Phone</th><th>Email</th></tr>'
    for i in range(0, len(mas)):
        html += '<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>'.format(mas[i][0], mas[i][1], mas[i][2], mas[i][3])
    html += '\n</table>\n</body>\n</html>'
    time_string = time.strftime("%m-%d-%Y-%H-%M", time.localtime())
    t = 'export/{}.html'.format(time_string)
    with open(t, 'w') as page:
        page.write(html)
    print('Экспорт прошел успешно :)')
    return True