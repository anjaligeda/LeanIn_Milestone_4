import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS USERS')

cur.execute('''
CREATE TABLE USERS (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = '/content/mbox (1).txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM USERS WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO USERS (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE USERS SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()
