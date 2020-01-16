import csv

# parse the parts list
parts = []
with open('parts_list.csv', newline='') as partscsv:
    reader = csv.reader(partscsv, delimiter=' ')
    for row in reader:
        parts.append(row[0])

# parse the inventory list
inventory = []
with open('QB Inventory.CSV', newline='') as qbinventorycsv:
    reader = csv.reader(qbinventorycsv, delimiter=',')
    next(qbinventorycsv)
    for row in reader:
        if row[7]:
            part_number = row[0].split(" ", 1)
            inventory.append(
                {'number': part_number[0], 'availability': int(row[7])}
            )

# marry the data
results = []
for part in parts:
    for item in inventory:
        if (
        part == item['number']
        and '-PC' not in item['number']
        and '-B' not in item['number']
        ):
            results.append({
                'part': part,
                'number': item['number'],
                'availability': item['availability']
            })

# write out to a new csv
with open('inventory.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    for result in results:
        writer.writerow(
            [result['part'], str(max(0, min(result['availability'], 20)))]
        )
