
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results (1).csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []

#Candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open("Resources/election_results (1).csv") as election_data:


    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        # 2. Add to the total vote count.
        total_votes += 1

        #print candidate name
        candidate_name = row[2]

        #find unique candidates
        if candidate_name not in candidate_options:

        #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #track the candidates vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:

     # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
        winning_count = votes

        winning_percentage = vote_percentage

        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

        

    # 4. Print the candidate name and percentage of votes.

    print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)