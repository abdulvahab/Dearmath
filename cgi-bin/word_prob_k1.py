#!/usr/bin/env python
import cgi
import cgitb
from random import randint,sample
from fractions import Fraction
from decimal import Decimal
cgitb.enable
print('Content-Type:text/html\n')

form = cgi.FieldStorage()
level = form['level'].value
choice = form['choice'].value
username = form['username'].value

def prob():
    if  level == 'KS1' and choice == 'Plus':
        a = randint(1,15)
        b = randint(1,10)
        prob = 'Add  ' + str(a) + '  and  ' +str(b)+ '?'
        #prob = 'Add  ' + str(add[0]) + '  and  ' +str(add[1])+ '?'
        solu = a+b
    elif level == 'KS1' and choice =='Minus':
        a = randint(11,20)
        b = randint(1,9)
        prob = 'What is  ' + str(a) + '  minus  ' +str(b)+ '?'
        #prob = 'Minus  ' + str(minus[0]) + '  and  ' +str(minus[1])+ '?'
        solu = a-b
    elif level == 'KS2' and choice=='Division':
        a = 3
        b = 2
        while a%b != 0:
            a = randint(1,5000)
            b = randint(1,20)
        prob = ''+ str(a)  + '  Divided by  ' +str(b)+ '?'
        #prob = ''+ str(div[0])  + '  Divided by  ' +str(div[1])+ '?'
        solu = a/b
    elif level == 'KS2' and choice=='Multiply':
        a= randint(1,1000)
        b = randint(1,100)
        prob = ''+ str(a)  + '  multiply by  ' +str(b)+ '?'
        #prob = ''+ str(multiply[0])  + '  multiply by  ' +str(multiply[1])+ '?'
        solu = a*b
    elif level == 'KS2' and choice=='Fraction':
        a= randint(1,9)
        b = randint(1,9)
        c = randint(1,9)
        d = randint(1,9)
        prob = 'Simplify  '+str(a)+'/'+str(b)+  ' Plus ' +str(c)+'/'+str(d)+' (write answer in a/b format)'
        #prob = 'Simplify  '+str(frac[0])+'/'+str(frac[1])+  'Plus' +str(frac[2])+'/'+str(frac[3])+''
        solu = (Fraction(a,b)+Fraction(c,d))
    elif level == 'KS2' and choice=='Decimal':
        a = randint(11,5000)
        l = [10,100,1000]
        b = sample(l,1)
        prob = 'Write in decimal ' +str(a)+ '/' +str(b[0])+ ''
        solu = float(a)/b[0]

    return [prob,solu]

prob = prob()
html = '<html>'
html += '<head>'
html += "<title>Math Problem</title>"
html += '</head>'
html += "<body style='background-color:#800080;text-align:center;margin:15%;color:white;'>"
html += '<h1>Dear Math</h1>'
html += '<p style=font-size:50px>' + prob[0] + '</p>'
html += "<form action ='http://dearmath.co.uk/cgi-bin/ansk1.py' method='post'>"
html += "<input style=width:100%;height:75px;text-align:center;font-size:50px; name ='ans' type='text' placeholder ='Your answer'></br></br>"
html += "<input type = 'hidden' name='solu' value={0}>".format(prob[1])
html += "<input type = 'hidden' name='username' value={0}>".format(username)
html += "<input type = 'hidden' name='choice' value={0}>".format(choice)
html += "<input type = 'hidden' name='level' value={0}>".format(level)
html += "<button style=width:30%;height:50px;background-color:magenta;font-size:40px;text-align:center;color:white; type='submit'><b>Submit</b></button>"
html += "</form>"
html += "<footer style='position:fixed;bottom:0;left:0'><code style=color:red;align:center'>Copyright: Abdulvahab Kharadi ,2018. </code></footer>"
html += '</body>'
html += '</html>'
print(html)
