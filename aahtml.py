def make_html(txt, ann):
    assert len(ann) == len(txt)

    html = ''
    header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style>
        * {
          /* font-family: MS P Gothic; */
          font-family: IPAMonaPGothic;
          font-size: 16px;
        }
        .Serifu { background:#ffd2a5; }
        .Jinobun { background:#d38cad; }
        .Comment { background:#8a79af; }
        .Gion { background:#5ea3a3; }
        .Scene_Description { background:#fb929e; }
        .AA { background: #b6f7c1; }
        .Res_Header { background: #8293ff; }
        .Text_in_AA { /*background: #00a3af;*/ background: #F3F781;}
        .Hidden_Text { color: white; background: black;}
    </style>
    <body>
    '''
    footer='</body></html>'

    html += header

    label = ann[0]
    start = 0
    for i, tag in enumerate(ann):
        if label != tag:
            html += '<span class="{}">{}</span>'.format(label, txt[start:i]).replace('\n', '↓<br />')
            label = tag
            start = i
    else:
            html += '<span class="{}">{}</span>'.format(label, txt[start:len(ann)]).replace('\n', '↓<br />')
    html += footer
    return html

if __name__ == '__main__':
    txt = \
'''
　 　 　　　＿＿＿_ 
　 　　　／⌒　　⌒＼ 
　　　／（ ●） 　（●）＼ 
　 ／::::::⌒（__人__）⌒::::: ＼ 　　だからニュー速でやるお! 
　 |　　　　　|r┬-|　　　　　| 
　 ＼ 　　 　 `ー'´ 　 　 ／
'''
    ann = ['AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'O', 'O', 'O', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'Serifu', 'O', 'O', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA', 'AA']
    print(make_html(txt, ann))

