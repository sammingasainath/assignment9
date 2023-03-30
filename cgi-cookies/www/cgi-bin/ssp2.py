import os

headers=["Content-Type : text/html"]
cookies = os.environ['HTTP_COOKIE']
qs= os.environ['QUERY_STRING']

def sendHeader():
    for h in headers:
        print(h)
    print("\n")

def sendForm():
    print('''
    <html>
        <body>
            <form action="ssp2.py" method="get">
                <label for="myname">Enter Your Name</label>
                <input id="myname" type="text" name="firstname" value="Sainath"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    ''')

def sendPage(name):
    print('''
          <html>
            <body>
                <h1>Hello {0}</h1>
            </body>
          </html>'''.format(name))


if not qs:
    if cookies and 'firstname' in cookies:
        sendHeader()
        cvalues = cookies.split(';')
        for c in cvalues:
            if 'firstname' in c:
                name = c.split('=')[1]
        sendPage(name)
    else:
        sendHeader()
        sendForm()
else:
    if 'firstname' in qs:
        name = qs.split('=')[1]
        headers.append("Set-Cookie: firstname=%s" % name)
    else:
        name = 'No Name Provided'
    sendHeader()
    sendPage(name)