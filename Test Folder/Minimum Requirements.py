##The minimal requirement for this assignment is to:

    refine the dataset:

develop a procedure to check that the data match expected format, remove duplicates, and perform further refinement. This procedure should ensure that:

        1. the values of variables are of the expected format (numbers, strings, etc.);
        2. the values of variables are admissible (e.g. are within a given range or are from the list of admissible values);

        DONE - 3. in case of any inconsistencies and/or duplicates found, produce new file with refined data to be used in the subsequent analysis;

        this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);

        the refinement process should be documented (e.g. using comments in the code) in case one may need to modify and re-run it (although it’s not necessary to repeat it each time while re-running the analysis),

    1. perform the descriptive analysis of the dataset:

    2. determine the total number of records in the dataset;

    3. determine the type of each variable in the dataset;

    for each variable except “Record_Number” and “Region”, find all different values that it takes, and the number of occurrences for each value,

    build the following plots:

     1.   bar chart for the number of records for each age group;

     2.   bar chart for the number of records for each occupation,

    provide the Jupyter notebook to re-run the analysis, starting from refined data.
