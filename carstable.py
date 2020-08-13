#cars table
import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',user='root',password='India12345',database='db1')
c = con.cursor()
def create_table():
    c.execute("create table akshatha_cars(modelno varchar(10), manufacturer varchar(20), carname varchar(10), price float)")
def insert_table():
    c.execute("insert into akshatha_cars values('TOY20101', 'Toyota', 'Yaris',8800000)")
    c.execute("insert into akshatha_cars values('MAZ20205', 'Suzuki', 'Baleno',5700000)")
    c.execute("insert into akshatha_cars values('HYN20192', 'Hyundai', 'Tuscon',22000000)")
    c.execute("insert into akshatha_cars values('MER20209', 'Mercedes', 'Benz-C',42000000)")
    c.execute("insert into akshatha_cars values('FORD20205', 'FORD', 'Ecosport',2900000)")
    con.commit()
def update_table():
    c.execute("update akshatha_cars set modelno='MRZ202090' where carname='Baleno'")
def delete_table():
    c.execute("delete from akshatha_cars where carname='Tuscon'")
def select():
    c.execute("select * from akshatha_cars")
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
('TOY20101', 'Toyota', 'Yaris', 8800000.0)
('MAZ20205', 'Suzuki', 'Baleno', 5700000.0)
('HYN20192', 'Hyundai', 'Tuscon', 22000000.0)
('MER20209', 'Mercedes', 'Benz-C', 42000000.0)
('FORD20205', 'FORD', 'Ecosport', 2900000.0)


#after updating 
('TOY20101', 'Toyota', 'Yaris', 8800000.0)
('MRZ202090', 'Suzuki', 'Baleno', 5700000.0)
('HYN20192', 'Hyundai', 'Tuscon', 22000000.0)
('MER20209', 'Mercedes', 'Benz-C', 42000000.0)
('FORD20205', 'FORD', 'Ecosport', 2900000.0)

after deleting
('TOY20101', 'Toyota', 'Yaris', 8800000.0)
('MAZ20205', 'Suzuki', 'Baleno', 5700000.0)
('MER20209', 'Mercedes', 'Benz-C', 42000000.0)
('FORD20205', 'FORD', 'Ecosport', 2900000.0)
'''

