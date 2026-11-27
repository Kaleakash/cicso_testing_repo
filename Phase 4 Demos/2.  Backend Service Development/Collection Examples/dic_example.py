dd = {"EMP1":"John Doe", "EMP2":"Jane Smith", "EMP3":"Alice Johnson"}    # dictionary with employee IDs and names
print(dd)
dd["EMP4"] = "Bob Brown"    # add a new employee
print(dd)
del dd["EMP2"]    # remove an employee using key
print(dd)
for emp_id, emp_name in dd.items():
    print(emp_id, emp_name)
print(dd["EMP1"])    # print the final state of the dictionary
#print(dd["EMP10"])    # attempt to print a non-existent employee, will raise KeyError