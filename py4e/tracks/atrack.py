# chapter 15 - Assignment 1

import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('D:\\OneDrive - DZS\\03-Courses\\04-Python\\tracks\\atrack.sqlite')
cur=conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS Track;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;

	
	CREATE TABLE Track (
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title	TEXT UNIQUE,
		album_id	INTEGER,
		genre_id	INTEGER,
		artist_id	INTEGER,
		len INTEGER, rating INTEGER, count INTEGER
	);
	CREATE TABLE Album (
		id 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title		TEXT UNIQUE,
		artist_id	INTEGER
	);
	CREATE TABLE Artist (
		id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name	TEXT UNIQUE
	);
	CREATE TABLE Genre (
		id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name 	TEXT UNIQUE
	);
''')

data=ET.parse('D:\\OneDrive - DZS\\03-Courses\\04-Python\\tracks\\Library.xml')
tracks=data.findall('dict/dict/dict')
print("There are",len(tracks),'tracks')

#def lookup(track, key):
#	
#	for element in track:
#		if 'key'==element.tag and key==element.text:
#			return element.

def lookup(track, key):
    found = False
    for element in track:
        if found : return element.text
        if element.tag == 'key' and element.text == key :
            found = True
    return None

for track in tracks:
	if lookup(track, 'Track ID') is None:
		continue
	
	title=lookup(track, 'Name')
	artist=lookup(track, 'Artist')
	album=lookup(track, 'Album')
	genre=lookup(track, 'Genre')
	length=lookup(track, 'Total Time')
	rating=lookup(track, 'Rating')
	count=lookup(track, 'Play Count')
	
	if title is None or artist is None or album is None or genre is None:
		continue
		
	cur.execute('INSERT or IGNORE INTO Artist (name) VALUES (?)', (artist,))
	cur.execute('SELECT id FROM Artist WHERE name=?',(artist,))
	artist_id=cur.fetchone()[0]
	
	cur.execute('INSERT or IGNORE INTO Genre (name) VALUES (?)', (genre,))
	cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
	genre_id=cur.fetchone()[0]
	
	cur.execute('INSERT or IGNORE INTO Album (title,artist_id) VALUES (?,?)', (album,artist_id))
	cur.execute('SELECT id FROM Album WHERE title=?',(album,))
	album_id=cur.fetchone()[0]
	
	cur.execute('''INSERT or REPLACE INTO Track 
		(title,album_id,genre_id,artist_id,len,rating,count)
		VALUES (?,?,?,?,?,?,?)''', (title,album_id,genre_id,artist_id,length,rating,count))
		
conn.commit()

cmd='''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''


for row in cur.execute(cmd):
	print(str(row[0]),'\t',str(row[1]),'\t',str(row[2]),'\t',str(row[3]))