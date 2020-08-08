import matplotlib.pyplot as p
fig = p.figure(figsize=(8,8))
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
p.subplot(321)
p.title('Line Chart')
p.grid()
p.plot(x,y)

ax1 = fig.add_subplot(322)
ax1.bar([1,2,3],[3,4,5])
p.title("Bar chart")
p.grid()


my_data = fig.add_subplot(325)
my_data= [60.11,15.69,10.24,4.88]
my_labels = 'Asia','Africa','Europe','North America'
p.pie(my_data, labels=my_labels, autopct='%1.1f%%', shadow="true")
p.axis('equal')
p.title('Pie Chart')

p.subplot(324)
p.title('scatter')
p.scatter(x, y)


p.subplot(323)
p.title('histogram')
p.hist(x, y)
p.show()

