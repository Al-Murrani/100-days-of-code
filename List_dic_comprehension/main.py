import pandas

student_dict = {
    "student": ["Amy", "Matt", "Sue"],
    "score": [48, 70, 56]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)

student_dict_df = pandas.DataFrame(student_dict)
print(student_dict_df)

# Loop through the data frame
# for (key, value) in student_dict_df.items():
#     print(value)

# Loop through rows of data frame
for (index, row) in student_dict_df.iterrows():
    # print(row)
    # print(row.student)
    if row.student == "Amy":
        print(row)
