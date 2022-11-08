#Data to retrieve
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
   
#To do: read and analyze data 
    # Read the file object
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    #1 Initialize a total voter counter
    total_votes = 0

    # Candidate Options
    candidate_options = []  

    # Declare empty dictionary
    candidate_votes = {}

    # Open the election results and read the file
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

    # read the header row
        headers = next(file_reader)

        # Print each row in the CSV file.
        for row in file_reader:
            #2 add to the total vote count.
            total_votes += 1


            #print the candidate name from each row
            candidate_name = row[2]

            # if not in
            if candidate_name not in candidate_options:

                #add candidate name to candidate list
                candidate_options.append(candidate_name)

                #set vote count to zero to begin tracking
                candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1

    #print the candidate list
    print(candidate_votes)

#determine vote percentage
for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #calculate vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # print out candidate name, vote count and percent of votes to the terminal.
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage

         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    
# winning candidate summary
print(f"----------------------\nWinner: {winning_candidate}\nWinning Vote COunt: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}\n-----------------------")


#5. The winner of the election based on popular vote.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open to write data into the file
with open(file_to_save, "w") as txt_file:

    #three counties
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")