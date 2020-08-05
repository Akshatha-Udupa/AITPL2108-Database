#states with thier capital
import csv
with open('states.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    next(readcsv)
    for row in readcsv:
        print(row[1:])

'''output
['Andhra Pradesh', 'Amaravathi']
['Arunachal Pradesh', 'Itanagar']
['Assam ', 'Dispur']
['Bihar', 'Patna']
['Cchattisgarh', 'Naya Raipur']
['Goa', 'Panaji']
['Gujarat', 'Gandhinagar']
['Haryana', 'Chandigarh']
['Himachal Pradesh', 'Shimla']
['Jammu & Kashmir', 'Srinagar']
['Jharkand', 'Ranchi']
['Karnataka', 'Bengaluru']
['Kerala', 'Thiruvananthapuram']
['Madhya Pradesh', 'Bhopal']
['Maharashtra', 'Mumbai']
['Manipur', 'Imphal']
['Meghalaya', 'Shiilong']
['Mizoram', 'Aizwal']
['Nagaland', 'Kohima ']
['Odisha', 'Buvaneshwar']
['Punjab', 'Chandigarh']
['Rajasthan', 'Jaipur']
['Sikkim', 'Gangtok']
['Tamil Nadu', 'Chennai']
['Telangana', 'Hyderabad']
['Tripura', 'Agartala']
['Uttar Pradesh', 'Lucknow']
['Uttarkhand', 'Dehradun']
['West Bengal', 'Kolkatta']
'''