#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("final_project/final_project_dataset.pkl", "r"))
# number of poi in enron_data
poi_count = 0
poi_payment_count = 0
for person in enron_data:
    if enron_data[person]['poi'] == 1:
        poi_count += 1
        if enron_data[person]['total_payments'] != 'NaN':
            poi_payment_count += 1
print poi_count, poi_payment_count

# number of poi in poi_names.txt
import csv
filename = 'final_project/poi_names.txt'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    poi_names = list(reader)
print len(poi_names)-2

# What is the total value of the stock belonging to James Prentice?
print enron_data['PRENTICE JAMES']['total_stock_value']

# How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# What's the value of stock options exercised by Jeffrey K Skilling
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Skilling', enron_data['SKILLING JEFFREY K']['total_payments']
print 'Fastow', enron_data['FASTOW ANDREW S']['total_payments']
print 'Lay', enron_data['LAY KENNETH L']['total_payments']

salary_count = 0
email_count = 0
payments_count = 0
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salary_count += 1
    if enron_data[person]['email_address'] != 'NaN':
        email_count += 1
    if enron_data[person]['total_payments'] != 'NaN':
        payments_count += 1
print salary_count, email_count, payments_count, len(enron_data)


