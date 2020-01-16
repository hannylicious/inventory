import csv
import pandas

# parse the parts list
parts = []
with open('parts_list.csv', newline='') as partscsv:
    reader = csv.reader(partscsv, delimiter=' ')
    for row in reader:
        parts.append(row[0])

# parse the inventory list
inventory = []
with open('QB inventory.csv', newline='') as qbinventorycsv:
    reader = csv.reader(qbinventorycsv, delimiter=',')
    next(qbinventorycsv)
    for row in reader:
        if row[7]:
            inventory.append({ 'description': row[0], 'availability': int(row[7])})

# marry the data
results = []
for part in parts:
    for item in inventory:
        if item['description'].startswith(part) and not item['description'].startswith(part + '-PC')  and not item['description'].startswith(part + '-B'):
            results.append({
                'part': part,
                'description': item['description'],
                'availability': item['availability']
            })

# write out to a new csv
with open('inventory.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    for result in results:
        writer.writerow([ result['part'], str(max(0, min(result['availability'], 20))) ])


df = pandas.read_csv('inventory.csv', header = 0)
df[row[0]] = df.groupby(row[0])[row[1]].transform('sum')
df.drop_duplicates(take_last=True)
    writer = csv.writer(output, delimiter=",")
        write.results
