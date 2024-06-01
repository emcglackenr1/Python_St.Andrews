#!/usr/bin/env python
import sys
import argparse
import pandas as pd
import numpy as np


"""
This file can be ran on the command line with 3 optional arguments, like so:
python .\main.py remove
python .\main.py format
python .\main.py unique

The desired function and or output will take place.
"""

##importing panda and reading the file 
input_file = "../data/Scotland_teaching_file_1PCT.csv"
df = pd.read_csv(input_file)

""" Based on this result, here is the output put onto separate lines to be more legible:
# You can see the data type and that many are objects.
# Outcome: Type of data and unique values in the dataset are now visible
# The completes the requirement to:
# Determine the type of each variable in the dataset
"""
def unique_values():
    get_col = list(pd.read_csv(input_file,nrows=1).columns)
    #print(get_col)
    unique_values = {col: df[col].unique() for col in get_col}
    print(unique_values)

"""
 Refining Data Continued 
 Checking if values of variables are admissible and expected format
 From this part of the assignment guidelines: 

    develop a procedure to check that the data match expected format, remove duplicates, and perform further refinement. This procedure should ensure that:

        1. the values of variables are of the expected format (numbers, strings, etc.);

        2. the values of variables are admissible (e.g. are within a given range or are from the list of admissible values);
"""

def expected_format():
    # expected format of data
    Record_Number_EF = np.array(list(range(1, 63389)))
    Region_EF = np.array(['S92000003'])
    RESIDENCE_TYPE_EF = np.array(['C', 'P'])
    Family_Composition_EF = np.array(['0', '1', '2', '3', '4', '5', 'X'])
    sex_EF = np.array([1, 2])
    age_EF = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    Marital_Status_EF = np.array([1, 2, 3, 4, 5])
    student_EF = np.array([1, 2])
    Country_Of_Birth_EF = np.array([1, 2])
    health_EF = np.array([1, 2, 3, 4, 5])
    Ethnic_Group_EF = np.array([1, 2, 4, 3, 5, 6])
    religion_EF = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    Economic_Activity_EF = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'])
    Occupation_EF = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'])
    industry_EF = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'X'])
    Hours_Worked_Per_Week_EF = np.array(['1', '2', '3', '4', 'X'])
    Approximate_Social_Grade_EF = np.array(['1', '2', '3', '4', 'X'])

    # Taken from output of unique values
    ### Converting data to an array so it can be analysed using numpy
    Record_Number_RD = np.array(list(range(1, 63389)))
    Region_RD = np.array(['S92000003'])
    RESIDENCE_TYPE_RD = np.array(['P', 'C'])
    Family_Composition_RD = np.array(['1', '0', '4', '2', '5', '3', 'X'])
    sex_RD = np.array([1, 2])
    age_RD = np.array([4, 3, 6, 5, 1, 2, 7, 8])
    Marital_Status_RD = np.array([2, 1, 4, 3, 5])
    student_RD = np.array([2, 1])
    Country_Of_Birth_RD = np.array([2, 1])
    health_RD = np.array([2, 3, 1, 4, 5])
    Ethnic_Group_RD = np.array([1, 2, 4, 3, 6, 5])
    religion_RD = np.array([5, 1, 2, 9, 6, 8, 4, 7, 3])
    Economic_Activity_RD = np.array(['1', 'X', '5', '6', '9', '4', '2', '7', '3', '8'])
    Occupation_RD = np.array(['5', '1', '4', '2', '3', '9', 'X', '8', '6', '7'])
    industry_RD = np.array(['5', '8', '11', '9', 'X', '2', '4', '6', '7', '10', '3', '12', '13', '1'])
    Hours_Worked_Per_Week_RD = np.array(['4', '3', '2', 'X', '1'])
    Approximate_Social_Grade_RD = np.array(['3', '2', '4', 'X', '1'])

    #This code compares the expected format of the data to the real data recieved

    print('Values from dataset that do not match the expected format based on the file Teaching_File_Variable_List(1). Empty square brackets mean the data is the correct format and values')
    print('Record_Number:')
    print(np.setdiff1d(Record_Number_EF, Record_Number_RD)) 
    print('Region:')
    print(np.setdiff1d(Region_EF, Region_RD))
    print('RESIDENCE_TYPE:')
    print(np.setdiff1d(RESIDENCE_TYPE_EF, RESIDENCE_TYPE_RD))
    print('Family_Composition_TYPE:')
    print(np.setdiff1d(Family_Composition_EF, Family_Composition_RD))
    print('sex_TYPE:')
    print(np.setdiff1d(sex_EF, sex_RD))
    print('age_TYPE:')
    print(np.setdiff1d(age_EF, age_RD))
    print('Marital_Status_TYPE:')
    print(np.setdiff1d(Marital_Status_EF, Marital_Status_RD))
    print('student:')
    print(np.setdiff1d(student_EF, student_RD))
    print('Country_Of_Birth:')
    print(np.setdiff1d(Country_Of_Birth_EF, Country_Of_Birth_RD))
    print('health:')
    print(np.setdiff1d(health_EF, health_RD))
    print('Ethnic_Group:')
    print(np.setdiff1d(Ethnic_Group_EF, Ethnic_Group_RD))
    print('religion:')
    print(np.setdiff1d(religion_EF, religion_RD))
    print('Economic_Activity:')
    print(np.setdiff1d(Economic_Activity_EF, Economic_Activity_RD))
    print('Occupation:')
    print(np.setdiff1d(Occupation_EF, Occupation_RD))
    print('industry:')
    print(np.setdiff1d(industry_EF, industry_RD))
    print('Hours_Worked_Per_Week:')
    print(np.setdiff1d(Hours_Worked_Per_Week_EF, Hours_Worked_Per_Week_RD))
    print('Approximate_Social_Grade:')
    print(np.setdiff1d(Approximate_Social_Grade_EF, Approximate_Social_Grade_RD))


# Column Record_Number not included in analysis, as it is a unique number given to each record, so if the same response was recorded twice it would still have a unique column Record_Number 
def remove_duplicates():
    df = pd.read_csv(input_file)
    output_file = "../data/Scotland_teaching_file_1PCT_DUPLICATES_REMOVED.csv" 

    columns = ["Region", "RESIDENCE_TYPE", "Family_Composition", "sex", "age", \
            "Marital_Status", "student", "Country_Of_Birth", "health", "Ethnic_Group", \
            "religion", "Economic_Activity", "Occupation", "industry", \
            "Hours_Worked_Per_Week", "Approximate_Social_Grade"]

    deduplicated_data = df.drop_duplicates(subset=columns, keep="first")

    dd = pd.DataFrame(deduplicated_data)
    dd.to_csv(output_file, index=False)
    print("New file created with duplicates removed")

if __name__ == "__main__":
    if sys.argv[1] == "remove":
        remove_duplicates()
    if sys.argv[1] == "unique":
        unique_values()
    if sys.argv[1] == "format":
        expected_format()

