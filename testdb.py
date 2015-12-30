#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mysql

db = mysql.connect("localhost" , "root" , "soft2015" ,"dbDemonstration")

cursor = db.cursor()


cursor.execute("set names utf8")
cursor.execute("SELECT * FROM testtb")

result = cursor.fetchall()

total = len(result)

entries = []

if total < 1:

    print 'No entries'

else:

    for record in range(total):

        entry = {}

        entry['uid'] = result[record][0]

        entry['name'] = result[record][1]

        entry['age'] = result[record][2]

        entries.append(entry)

for entry in entries:

    print '이름: ' + entry['name'] + ', 나이: ' + str(entry['age'])

cursor.close()
