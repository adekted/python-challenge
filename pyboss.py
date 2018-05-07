import os
import csv

csvfile = os.path.join(".","PyBoss","raw_data","employee_data2.csv")
output = os.path.join(".","PyBoss","formatted_employee.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_list = []
with open(csvfile, newline = '') as employeedata:
    employee_reader = csv.DictReader(employeedata, delimiter = ",")

    for row in employee_reader:
        dob_split = row["DOB"].split("-")
        new_dob = str(dob_split[1]) + "/" + str(dob_split[2]) + "/" + str(dob_split[0])

        employee_dict = {
            "Emp ID" : row["Emp ID"],
            "First Name" : row["Name"].split()[0],
            "Last Name" : row["Name"].split()[1],
            "DOB" : new_dob,
            "SSN" : "***-**-"+row["SSN"][7:],
            "State" : us_state_abbrev[(row["State"])],
        }
        employee_list.append(employee_dict)

with open(output,'w',newline="") as output:
    fieldnames = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
    writer = csv.DictWriter(output,fieldnames=fieldnames)
    writer.writeheader()
    for i in employee_list:
        writer.writerow(i)