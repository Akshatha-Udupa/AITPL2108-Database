import sqlite3

con = sqlite3.connect('db1.db')
c = con.cursor()

c.execute("create table student(regno 'text' primary key, name 'text', Address 'text')")
c.execute("insert into student values('A101','Akshatha','KS Layout')")
c.execute("insert into student values('A102','Rakshita','BTM')")
c.execute("insert into student values('A103','Prathap','Gandhibazar')")
con.commit()

c.execute("select * from student")
data = c.fetchall()
print("After inserting",data)

c.execute("update student set regno='A104' where regno='A102'")
c.execute("select * from student")
data = c.fetchall()
print("After updating",data)

#c.execute("insert into student values('A101','Darshan')")  #shows error like :sqlite3.IntegrityError: UNIQUE constraint failed: student.regno

c.execute("delete from student where regno='A104'")
c.execute("select * from student")
data = c.fetchall()
print("After deleting",data)

c.close()
con.close()

'''output
After inserting [('A101', 'Akshatha', 'KS Layout'), ('A102', 'Rakshita', 'BTM'), ('A103', 'Prathap', 'Gandhibazar')]
After updating [('A101', 'Akshatha', 'KS Layout'), ('A104', 'Rakshita', 'BTM'), ('A103', 'Prathap', 'Gandhibazar')]
After deleting [('A101', 'Akshatha', 'KS Layout'), ('A103', 'Prathap', 'Gandhibazar')]
'''

