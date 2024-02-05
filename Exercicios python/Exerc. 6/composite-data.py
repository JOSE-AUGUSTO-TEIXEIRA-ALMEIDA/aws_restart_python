#O arquivo executa os códigos apenas se estiver na raiz do sistema '/home/ec2-user/environment' conjuntamente com o arquivo 'car_fleet.csv'

import csv
import copy

my_vehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in my_vehicle.items():
    print("{} : {}".format(key,value))
    
my_inventory_list = []

with open('car_fleet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')  
    line_count = 0  
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')  
            line_count += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            current_vehicle = copy.deepcopy(my_vehicle)  
            current_vehicle["vin"] = row[0]  
            current_vehicle["make"] = row[1]  
            current_vehicle["model"] = row[2]  
            current_vehicle["year"] = row[3]  
            current_vehicle["range"] = row[4]  
            current_vehicle["topSpeed"] = row[5]  
            current_vehicle["zeroSixty"] = row[6]  
            current_vehicle["mileage"] = row[7]  
            my_inventory_list.append(current_vehicle)  
            line_count += 1  
    print(f'Processed {line_count} lines.')
    
    for my_car_properties in my_inventory_list:
        for key, value in my_car_properties.items():
            print("{} : {}".format(key,value))
            print("-----")