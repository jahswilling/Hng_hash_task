# Hash Json Task

A simple script written using Python to create a JSON Hash for each entry in a given csv. The Output will be a modified CSV 

This project contains two different script written using Python create a JSON Hash for each entry in a given csv. The create_hash.py script handle only a single team CSV (E.g Team_bevel) while the create_hash_all.py script handles for all the team with data in the HNGi9_all_teams.csv
## Want to run create_hash.py?

To run the create_hash.py that runs for only one team, format your CSV file to the same format as the Team_Bevel.csv file in the repo, then run
```
$ python3 create_hash.py
```
The script will generate a modified file (Modified_Team_Bevel.csv) with a json hash in a new column at the end, and the hashed json files will be saved in the json files folder. Currently the script handles the name and description for each team, but can be update subsequently when the team data is updated.

## Want to run create_hash_all.py?

To run the create_hash_all.py that runs for only one team, format your CSV file to the same format as the HNGi9_all_teams.csv file in the repo, then run
```
$ python3 create_hash_all.py
```
The script will generate a modified file (Modified_HNGi9_all_teams.csv) with a json hash in a new column at the end, and the hashed json files will be saved in the json files folder as the team name and uuid. Currently the script handles the name,gender,description, and uuid for each team, but can be update subsequently when the team data is updated. The attribute field is present but the data format is not yet consistent to work with.


