#-------------------------------------------------------------------------
# AUTHOR: Siwen Wang
# FILENAME: find_s.py
# SPECIFICATION: read the file contact_lens.csv and output the hypothesis of Find-S algorithm (the hypothesis you got in part a). The output should be in this format: [‘Sunny’, ‘?’, ‘Strong’, ‘?’].
# FOR: CS 4200- Assignment #1
# TIME SPENT: 20 Minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

counter = 0


#find the first positive training data in db and assign it to the vector hypothesis
for row in db:
    counter += 1
    if row[4] == 'Yes':
        hypothesis = row
        break

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
for i in range(counter, len(db)):
    if db[i][4] == 'Yes':
        for j in range(len(hypothesis)-1):
            if db[i][j] != hypothesis[j]:
                hypothesis[j] = '?'

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
