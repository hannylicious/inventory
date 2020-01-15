import csv

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
    for row in reader:
        if row[7]:
            inventory.append({ 'description': row[0], 'availability': row[7]})
        else:
            inventory.append({ 'description': row[0], 'availability': '0' })
            

# marry the data
results = []
for part in parts:
    for item in inventory:
        if item['description'].startswith(part) and not item['description'].startswith(part + '-PC')  and not item['description'].startswith(part + '-B'):
            results.append({
            'part': part,
            'description': item['description'],
            'availability': int(item['availability'])
            })

# write out to a new csv
with open('inventory.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    for result in results:
            if result['availability'] > 20: writer.writerow([ result['part'], 20])
            elif result['availbility'] < 0: writer.writerow([ result['part'], 0])
            else:
                writer.writerow([ result['part'], result['availability'] ])
            