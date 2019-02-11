#!/usr/bin/env python
import cgi
import cgitb
from fractions import Fraction
#import word_prob_k1
cgitb.enable()
print('Content-Type:text/html\n')

form = cgi.FieldStorage()
choice = form['choice'].value
level = form['level'].value
ans = form['ans'].value
solu = form['solu'].value
name = form['username'].value
link = 'http://dearmath.co.uk/cgi-bin/word_prob_k1.py?username={}&level={}&choice={}'.format(name,level,choice)
def result():
    if solu == ans:
        result = 'Well Done  ' + name.capitalize() +''
    else:
        result = 'Try Again  ' + name.capitalize() +''
    return result

html = '<html>'
html += '<head>'
html += "<title>Result Page</title>"
html += "</head>"
html += "<body style=background-color:#800080;text-align:center;margin:25%>"
html += "<button style=width:100%;height:80px;background-color:magenta;font-size:50px;text-align:center;color:white; onclick='goBack()'>"+result()+"</button>"
if result() == 'Try Again  ' + name.capitalize() +'':
    html += "<script>function goBack(){window.history.go(-1)}</script>"
else:
    html += "<script>function goBack(){window.location.assign('http://dearmath.co.uk/cgi-bin/word_prob_k1.py?username={}&level={}&choice={}'.format(name,level,choice))}</script>"
    html += "<a style='font-size:30px;color:white;' href='http://dearmath.co.uk/cgi-bin/word_prob_k1.py?username={}&level={}&choice={}'>Play Again</a></br></br>".format(name,level,choice)
    html += "<a style='font-size:30px;color:white;' href='http://dearmath.co.uk'>Take Rest</a>"
html += "<footer style='position:fixed;bottom:0;left:0'><code style=color:red;align:center'>Copyright: Abdulvahab Kharadi ,2019. </code></footer>"
html += "</body>"
html += "</html>"
print(html)
