#product table
import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',user='root',password='India12345',database='db1')
c = con.cursor()
def create_table():
    c.execute("create table akshatha_product(pid varchar(10), pname varchar(15), pdesc varchar(20), pprice float)")
def insert_table():
    c.execute("insert into akshatha_product values('p01', 'Pen', 'Blueink',20)")
    c.execute("insert into akshatha_product values('p02', 'Shirt', 'Cotton',500)")
    c.execute("insert into akshatha_product values('p03', 'Phone', 'smartphone',20000)")
    c.execute("insert into akshatha_product values('p04', 'Noodles', 'vegfood',100)")
    c.execute("insert into akshatha_product values('p05', 'Shoes', 'Sportswear',4000)")

    con.commit()
def update_table():
    c.execute("update akshatha_product set pprice=150 where pname='Noodles'")
def delete_table():
    c.execute("delete from akshatha_product where pname='Noodles'")
def select():
    c.execute("select * from akshatha_product")
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
('p01', 'Pen', 'Blueink', 20.0)
('p02', 'Shirt', 'Cotton', 500.0)
('p03', 'Phone', 'smartphone', 20000.0)
('p04', 'Noodles', 'vegfood', 100.0)
('p05', 'Shoes', 'Sportswear', 4000.0)


#after updating 
('p01', 'Pen', 'Blueink', 20.0)
('p02', 'Shirt', 'Cotton', 500.0)
('p03', 'Phone', 'smartphone', 20000.0)
('p04', 'Noodles', 'vegfood', 150.0)
('p05', 'Shoes', 'Sportswear', 4000.0)

after deleting
('p01', 'Pen', 'Blueink', 20.0)
('p02', 'Shirt', 'Cotton', 500.0)
('p03', 'Phone', 'smartphone', 20000.0)
('p05', 'Shoes', 'Sportswear', 4000.0)
'''

