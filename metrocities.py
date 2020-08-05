#metrocities
import csv
with open('Metro city.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    line = csv_file.readline()
    print(len(line))
    next(readcsv)
    for row in readcsv:
        print(row)

'''outpt
25
['Chennai', '13.0827', '80.2707']
['Delhi', '28.7041', '77.1025']
['Bangalore', '12.9716', '77.5946']
['Hyderabad', '17.385', '78.4867']
['Ahmedabad', '23.0225', '72.5714']
['Kochi', '9.9312', '76.2673']
['Kanpur', '26.4499', '80.3319']
['Surat', '21.1702', '72.8311']
['Visakhapatnam', '17.6868', '83.2185']
['Kolkatta', '22.5726', '88.3639']
['Uttarpradesh', '26.8467', '80.9462']
['Pune', '18.5204', '73.8567']
'''