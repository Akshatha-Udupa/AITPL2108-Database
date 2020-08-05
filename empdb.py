import sqlite3

con = sqlite3.connect('db1.db')
c = con.cursor()

c.execute("create table emp(empno 'text' primary key, name 'text', salary float)")
c.execute("insert into emp values('E101','Surya','250000')")
c.execute("insert into emp values('E102','Akash','280000')")
c.execute("insert into emp values('E103','Sanjay','30000')")
con.commit()

c.execute("select * from emp")
data = c.fetchall()
print("After inserting",data)

c.execute("update emp set empno='E100' where empno='E101'")
c.execute("select * from emp")
data = c.fetchall()
print("After updating",data)

#c.execute("insert into emp values('E101','Darshan',50000)")  #shows error like :sqlite3.IntegrityError: UNIQUE constraint failed: emp.empno

c.execute("delete from emp where empno='E102'")
c.execute("select * from emp")
data = c.fetchall()
print("After deleting",data)

c.close()
con.close()

'''output
After inserting [('E101', 'Surya', 250000.0), ('E102', 'Akash', 280000.0), ('E103', 'Sanjay', 30000.0)]
After updating [('E100', 'Surya', 250000.0), ('E102', 'Akash', 280000.0), ('E103', 'Sanjay', 30000.0)]
After deleting [('E100', 'Surya', 250000.0), ('E103', 'Sanjay', 30000.0)]
'''

