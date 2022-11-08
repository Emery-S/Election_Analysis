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

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (f"\nElection Results\n-------------------------\nTotal Votes: {total_votes:,}\n-------------------------")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):

         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage

         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    
# winning candidate summary
    winning_candidate_summary = (f"----------------------\nWinner: {winning_candidate}\nWinning Vote COunt: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}\n-----------------------")

    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)