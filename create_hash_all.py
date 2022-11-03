import csv
import json
import hashlib


#handles getting data from json
def get_data():
    name_file = open('HNGi9_all_teams.csv')
    csvreader = csv.reader(name_file)
    
    rows = []
    for row in csvreader:
        rows.append(row)
    
    return rows


#Handles Hashing the file
def calculate_hash(name_file,team_name):
    team = team_name.split(' ')
    filename = 'json_files/'+team[1]+'_'+name_file+'.json'
    with open(filename,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        
        
    return readable_hash


#Handles creating json file
def handle_json(data,team_name):
    
    team = team_name.split(' ')
    
    # attributes = data[5].split(',')
    
    # attributes_list = []
    
    # for attr in attributes:
        
    #     temp_attributes = attr.split(':')
    #     attributes_list.append({temp_attributes[0]: temp_attributes[1]})
    
    
    # Data to be written
    dictionary = {
        "format": "CHIP-0007",
        "UUID": data[6],
        "name": data[2],
        "gender": data[4],
        "description": data[3],
        "minting_tool": "",
        "sensitive_content": False,
        "series_number": None,
        "series_total": None,
        "attributes": [],
        "collection": {},
        "data": {}
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to json file using uuid as name
    with open(f"json_files/{team[1]}_{data[6]}.json", "w") as outfile:
        outfile.write(json_object)


#Handles creating new CSV file
def create_csv_file(titles,team_name,team_data):

    # open the file in the write mode
    with open('Modified_HNGi9_all_teams.csv', 'w') as f:
        # create the csv writer
        
        writer = csv.writer(f)
        writer.writerow(titles)
        for team in team_name:
            writer.writerow([])
            writer.writerow([team])
            
            for data in team_data[team]:
                
                writer.writerow(data)


def main():
    
    #Get the data from spreadsheet
    data = get_data()
    
    titles = data[0]
    team_data = {}
    team_name = []
    new_team_data = {}
    
    #get all teams in a list
    for i in range(0,462,22):
        
        team_name.append(data[i+1][0])
        
    
    start = 2
    
    end = 22
    
    #sort data by team
    for team in team_name:
        
        team_data[team]  = data[start:end]
        start = start+22
        end = end+22

    #Create empty list for each team
    for team in team_name:
        new_team_data[team]=[]
    
    # process data for each of the teams
    for team in team_name:
        
        #Goes through the data for each team, create json file and hash file
        for data in team_data[team]:
            

            handle_json(data,team)
            
            #Adds hash to row
            data.append(calculate_hash(data[6],team))
            
            #adds the row to the list
            new_team_data[team].append(data)
    
    
    create_csv_file(titles,team_name,team_data)
    
    print("Done!! To view new CSV open Modified_HNGi9_all_teams.csv")
if __name__ == '__main__':
    main()

