#Student Record System with Tuples & Sets

# Intialize students ids that is not mutable
studentsids=(101,102,103,104)
print("Students IDS:",studentsids)
#Set of unique courses
courses={"AI","Ml","Data Science","NLP"}
print("/n List of Courses",courses)

#add new course
#set automatically to remove duplicates
courses.add("python")
print("/n List of updated Courses",courses)

#do not add already exists
courses.add("Data Science")
print("/n List of courses remain same",courses)

#remove course
courses.remove("python")
print("/n List of courses after remove python",courses)

#final list of course
print("/n final list of courses",courses)



