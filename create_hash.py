import csv
import json
import hashlib


#handles getting data from json
def get_data():
    name_file = open('Team_Bevel.csv')
    csvreader = csv.reader(name_file)
    
    rows = []
    for row in csvreader:
        rows.append(row)
        
    del rows[0]
    # print(rows)
    
    return rows


#Handles Hashing the file
def calculate_hash(name_file):
    
    filename = 'json_files/'+name_file+'.json'
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print(readable_hash)
        
    return readable_hash


#Handles creating json file
def handle_json(data):
    # Data to be written
    dictionary = {
        "format": "CHIP-0007",
        "name": data[1],
        "description": data[2],
        "minting_tool": "SuperMinter/2.5.2",
        "sensitive_content": False,
        "series_number": 22,
        "series_total": 1000,
        "attributes": [
            {
                "trait_type": "Species",
                "value": "Mouse"
            },
            {
                "trait_type": "Color",
                "value": "Yellow"
            },
            {
                "trait_type": "Friendship",
                "value": 50,
                "min_value": 0,
                "max_value": 255
            }
        ],
        "collection": {
            "name": "Example Pokémon Collection",
            "id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
            "attributes": [
                {
                    "type": "description",
                    "value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
                },
                {
                    "type": "icon",
                    "value": "https://examplepokemoncollection.com/image/icon.png"
                },
                {
                    "type": "banner",
                    "value": "https://examplepokemoncollection.com/image/banner.png"
                },
                {
                    "type": "twitter",
                    "value": "ExamplePokemonCollection"
                },
                {
                    "type": "website",
                    "value": "https://examplepokemoncollection.com/"
                }
            ]
        },
        "data": {
            "example_data": "VGhpcyBpcyBhbiBleGFtcGxlIG9mIGRhdGEgdGhhdCB5b3UgbWlnaHQgd2FudCB0byBzdG9yZSBpbiB0aGUgZGF0YSBvYmplY3QuIE5GVCBhdHRyaWJ1dGVzIHdoaWNoIGFyZSBub3QgaHVtYW4gcmVhZGFibGUgc2hvdWxkIGJlIHBsYWNlZCB3aXRoaW4gdGhpcyBvYmplY3QsIGFuZCB0aGUgYXR0cmlidXRlcyBhcnJheSB1c2VkIG9ubHkgZm9yIGluZm9ybWF0aW9uIHdoaWNoIGlzIGludGVuZGVkIHRvIGJlIHJlYWQgYnkgdGhlIHVzZXIu"
        }
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to json file using uuid as name
    with open(f"json_files/{data[4]}.json", "w") as outfile:
        outfile.write(json_object)


#Handles creating new CSV file
def create_csv_file(data):

    # open the file in the write mode
    with open('Modified_Team_Bevel.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)

        for row in data:   
            # write a row to the csv file
            writer.writerow(row)


def main():
    
    #Get the data from spreadsheet
    data = get_data()
    
    new_list = []
    
    #Goes through the data and create json file and hash file
    for d in data:
        handle_json(d)
        
        #Adds hash to row
        d.append(calculate_hash(d[4]))
        
        #adds the row to the list
        new_list.append(d)
        
        
    print(new_list)
    
    create_csv_file(new_list)
    
    
if __name__ == '__main__':
    main()

