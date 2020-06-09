
# T3020   Repo for ELEN3020

Name: Gift Maposa


Date: 8 June 2020

# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

## List of errors encountered

In line 16 there was an index error with the sys.argv arguments, I debugged the error by printing the size of sys.argv and I got one indicating to me that there is only item the list and thus I replaced the one with the a 0 as there is only 1 index in the list fixing the error.

In line 20 (E1), there is an indexing error in the for loop, while computing the total it starting at index 2 instead of 1 and this resulted in incorrect values for TALL.

In line 29 (E2) to check for increasing monotonic behaviour, we need to check if the next entry in a row of the same coloum is larger than the previous entry or equal to , now the if statement presented tries to check if this condition is not met and returns an error message if the condition is met however the statement checks if the previous entry is greater or equal to the current entry which will provide incorrect results  if we encounter equal entries thus I only made it to check if the previous entry is greater than the current one to check for monotonicity.

In line 28 since we are only checkin columns TALL, T1-T7 there is no need for us to loop through the entire list therefore I changed the loop condition to go through the required places.

In line 39(E3) the loop through the curr_str list is not explicit as to how the list should be iterated, by stating that the program should start from [0:last index], it eliminates further errors that might arise while data is being processed through the list.

