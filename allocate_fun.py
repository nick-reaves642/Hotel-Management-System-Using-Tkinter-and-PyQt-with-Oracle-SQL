# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author: nimis
"""
import cx_Oracle as cx
import random
def allocate_rooms():
    conn=cx.connect('hr/hr@localhost/orcl')
    str1="insert into avail select available,room_no from test where available='y'"
    cur=conn.cursor()
    cur.execute(str1)
    cur=conn.cursor()
    str2="select room_no from avail"
    cur.execute(str2)
    l=list()
    cnt=0
    for x in cur:
        l.append(x[0])
        cnt=cnt+1
    z=random.randint(0,cnt-1)
    room,fl=0,0
    room=int(l[z]%100)
    fl=int(l[z]/100)
    str3="delete from avail where room_no="+str(room)
    cur=conn.cursor()
    cur.execute(str3)
    str4="update test set available='n',name='something_name',entry=sysdate where room_no="+str(room)
    cur=conn.cursor()
    cur.execute(str4)
    conn.commit()
    conn.close()
    return (room,fl)
