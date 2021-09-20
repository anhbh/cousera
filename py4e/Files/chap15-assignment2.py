import urllib.request, urllib.parse, urllib.error
import ssl, re
import sqlite3

conn=sqlite3.connect('D:\\SQLiteDB\\orgdb.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
conn.commit()

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#url='https://www.py4e.com/code3/mbox.txt?PHPSESSID=3a20e4b14af08d1d48e61874fa395c25'
#data=urllib.request.urlopen(url, context=ctx).read().decode()

filename=('D:\\SQLiteDB\\mbox.txt')
data=open(filename)

for line in data:
	words=line.strip().split()
	if len(words) < 3 or words[0] != 'From':
		continue

	org=re.findall('@([a-zA-Z0-9.]*)', words[1])[0]
	cur.execute('SELECT count FROM Counts where org=?', (org,))
	row=cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)', (org,))
	else:
		cur.execute('UPDATE Counts SET count=count+1 WHERE org=?', (org,))
	
	#conn.commit()
conn.commit()

sqlstr='SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
	print(str(row[0]),'\t',row[1])

cur.close()