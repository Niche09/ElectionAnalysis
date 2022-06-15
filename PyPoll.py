
#Import our dependencies

import csv
import os 


#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create and filename variable to a direct or indirect path to the file
file_to_save= os.path.join("analysis", "election_analysis.txt")

total_votes=0

#Print the candidate name from each row
candidate_options=[]

#Declare an empty dictionary
candidate_votes ={}

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read and print the header row.
    headers=next(file_reader)


    #Print each row in the CSV file.
    for row in file_reader:
        #2Add to the total count
        total_votes +=1

    #Print the candidate name from each row
        candidate_name =row[2]

        

    #If the candidate does not match and exisiting candidates
    if candidate_name not in candidate_options:

#Add the candidate name to the candidate list
         candidate_options.append(candidate_name)

    #Begin tracking the candidate's vote count
         candidate_votes[candidate_name]=0

    candidate_votes[candidate_name] +=1


#Print the candidate list
print(candidate_votes)

#3Print the total votes
#print(total_votes)


#Close the file







