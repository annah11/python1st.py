from re import*
match('[a-z]+','abcd').group()
# matches the begining of string (^) OR EXCEPT
match('[^a-z])+','hana').group()
# matches the end of string ($)
match('[a-z]+$','abcd').group()
# matches either regex R or regex S
match('[a-z]+)|([A-Z]+)','abcD').group()
# (.) ANY THING  Every character  of  the string matches
match('.+','abcd').group()
