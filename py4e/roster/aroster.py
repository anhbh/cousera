# chapter 15 - assignment 2

import json, sqlite3

conn=sqlite3.connect('D:\\OneDrive - DZS\\03-Courses\\04-Python\\roster\\roster.sqlite')
cur=conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;
	
	CREATE TABLE User (
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name	TEXT UNIQUE
	);
	
	CREATE TABLE Course (
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title	TEXT UNIQUE
	);
	
	CREATE TABLE Member (
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		user_id	INTEGER,
		course_id	INTEGER,
		role	INTEGER
	);
''')

fh=open('D:\\OneDrive - DZS\\03-Courses\\04-Python\\roster\\roster_data.json')
data=fh.read()

jdata=json.loads(data)
print('Loaded',len(jdata),'entries')
for node in jdata:
	print(node)
	name=node[0]
	course=node[1]
	role=node[2]
	
	cur.execute('INSERT or IGNORE INTO User (name) VALUES (?)', (name,))
	cur.execute('SELECT (id) FROM User WHERE name=(?)', (name,))
	user_id=cur.fetchone()[0]
	
	cur.execute('INSERT or IGNORE INTO Course (title) VALUES (?)', (course,))
	cur.execute('SELECT (id) FROM Course WHERE title=(?)', (course,))
	course_id=cur.fetchone()[0]
	
	cur.execute('''INSERT or REPLACE INTO Member (user_id,course_id,role) VALUES 
					(?,?,?)''', (user_id,course_id,role))
	
conn.commit()
cmd=''' SELECT User.name,Course.title,Member.role 
		FROM User JOIN Course JOIN Member 
		ON User.id=Member.user_id AND Course.id=Member.course_id
		ORDER BY User.name DESC, Course.title DESC, Member.role DESC
		LIMIT 2
	'''
for row in cur.execute(cmd):
	print(str(row[0]),'|',str(row[1]),'|',str(row[2]))

cmd=''' SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
		User JOIN Member JOIN Course 
		ON User.id = Member.user_id AND Member.course_id = Course.id
		ORDER BY X LIMIT 1
	'''
for row in cur.execute(cmd):
	print(str(row[0]))