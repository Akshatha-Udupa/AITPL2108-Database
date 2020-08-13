#employee table
import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',user='root',password='India12345',database='db1')
c = con.cursor()
def create_table():
    c.execute("create table akshatha_emp(empid varchar(10),empname varchar(20), salary float)")
def insert_table():
    c.execute("insert into akshatha_emp values('AITPL2108','Akshatha',30000)")
    c.execute("insert into akshatha_emp values('AITPL2101','Rakshita',33000)")
    c.execute("insert into akshatha_emp values('AITPL2102','Prathap',50000)")
    c.execute("insert into akshatha_emp values('AITPL2103','Kiran',50000)")
    c.execute("insert into akshatha_emp values('AITPL2104','Surya',20000)")
    con.commit()
def update_table():
    c.execute("update akshatha_emp set salary=40000 where empid='AITPL2108'")
def delete_table():
    c.execute("delete from akshatha_emp where empname='Kiran'")
def select():
    c.execute("select * from akshatha_emp")
    data = c.fetchall()
    for row in data:
        print(row)
create_table()
insert_table()
update_table()
delete_table()
select()
c.close()
con.close()
'''
output
after inserting
('AITPL2108', 'Akshatha', 30000.0)
('AITPL2101', 'Rakshita', 33000.0)
('AITPL2102', 'Prathap', 50000.0)
('AITPL2103', 'Kiran', 50000.0)
('AITPL2104', 'Surya', 20000.0)

#after updating 
('AITPL2108', 'Akshatha', 40000.0)
('AITPL2101', 'Rakshita', 33000.0)
('AITPL2102', 'Prathap', 50000.0)
('AITPL2103', 'Kiran', 50000.0)
('AITPL2104', 'Surya', 20000.0)

after deleting
('AITPL2108', 'Akshatha', 30000.0)
('AITPL2101', 'Rakshita', 33000.0)
('AITPL2102', 'Prathap', 50000.0)
('AITPL2104', 'Surya', 20000.0)
'''

