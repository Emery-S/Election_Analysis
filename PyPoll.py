#Data to retrieve
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
   
#To do: read and analyze data 
    # Read the file object
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)
#1. Total number of votes cast
#2. Complete list of ccandidates that recieved votes
#3. Total number of votes each candidate recieved.
#4. Percentage of votes each candidate won.
#5. The winner of the election based on popular vote.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open to write data into the file
with open(file_to_save, "w") as txt_file:

    #three counties
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")