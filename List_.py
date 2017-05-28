'''
Python - List, set and tuples

'''
courses = ['History','Maths','CompSci','Geo']

#Slicing

print(courses[0:2])
print(courses[:2])
print(courses[2:])

#Methods
#Append at the end

courses.append('Art')
courses.insert(0,'SPCC')
print(courses)


courses_2 = ['Arts','SPCC']
courses.insert(0,courses_2)
print(courses)

[['Arts', 'SPCC'], 'History', 'Maths', 'CompSci', 'Geo']

courses.remove()

pop = courses.pop()
print(courses)
print(pop)
courses.reverse()
print(courses)

courses.sort()
print(courses)

numbers = [3,1,2,6,8]
numbers.sort()
print(numbers)

#Sorting in reverse direction

numbers.sort(reverse=True)
print (numbers)

# Inorder to not change the orignal list we can use sorted function

temp = sorted(courses)
temp1 = min(numbers)
temp2 = max(numbers)
temp3 = sum(numbers)

print(temp,temp1,temp2,temp3)




print(courses.index("CompSci"))
print ('CompSci' in courses)

#Enumerate is used to capture the index of item.

for index,items in enumerate(courses,start = 1):
    print(index,items)

#JOIN method

course_str = ' - '
join_ = course_str.join(courses)
print(join_)

new_list = join_.split(' - ')
print(new_list)


# tuples
# tuples are immutable that is we can change there value once assigned
courses_tuple = ('History','CompSci','Maths','SPCC')
courses_tuple2 = courses_tuple
#Throw and error
courses_tuple2[0] = 'xyz'


#SETS - unordered collection, doesnot contain duplicate items used to removeduplicates
#and perform set operations like union.intersection

courses_set = {'History','CompSci','Maths','SPCC','History'}
courses_set2 = {'Art','History'}
print(courses_set)
print(courses_set.union(courses_set2))
print(courses_set.intersection(courses_set2))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
