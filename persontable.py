#person table
import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',user='root',password='India12345',database='db1')
c = con.cursor()
def create_table():
    c.execute("create table akshatha_person(name varchar(10), DOB varchar(12), address varchar(30), panno varchar(10))")
def insert_table():
    c.execute("insert into akshatha_person values('Akshatha', '06/05/1998', 'KS Layout','AP1234S')")
    c.execute("insert into akshatha_person values('Rakshitha', '30/07/1996', 'BTM','AR1243S')")
    c.execute("insert into akshatha_person values('Prathap', '30/05/1996', 'KS Layout','PA87654A')")
    c.execute("insert into akshatha_person values('Sindhu', '26/08/1998', 'Mysore','SS2345A')")
    c.execute("insert into akshatha_person values('Meghana', '05/09/1997', 'Mangalore','Mg9876A')")
    con.commit()
def update_table():
    c.execute("update akshatha_person set address='Bangalore' where name='Prathap'")
def delete_table():
    c.execute("delete from akshatha_person where name='Meghana'")
def select():
    c.execute("select * from akshatha_person")
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
('Akshatha', '06/05/1998', 'KS Layout', 'AP1234S')
('Rakshitha', '30/07/1996', 'BTM', 'AR1243S')
('Prathap', '30/05/1996', 'KS Layout', 'PA87654A')
('Sindhu', '26/08/1998', 'Mysore', 'SS2345A')
('Meghana', '05/09/1997', 'Mangalore', 'Mg9876A')


#after updating 
('Akshatha', '06/05/1998', 'KS Layout', 'AP1234S')
('Rakshitha', '30/07/1996', 'BTM', 'AR1243S')
('Prathap', '30/05/1996', 'Bangalore', 'PA87654A')
('Sindhu', '26/08/1998', 'Mysore', 'SS2345A')
('Meghana', '05/09/1997', 'Mangalore', 'Mg9876A')

after deleting
('Akshatha', '06/05/1998', 'KS Layout', 'AP1234S')
('Rakshitha', '30/07/1996', 'BTM', 'AR1243S')
('Prathap', '30/05/1996', 'KS Layout', 'PA87654A')
('Sindhu', '26/08/1998', 'Mysore', 'SS2345A')
'''

