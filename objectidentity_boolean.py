#Object identity
a = [1,2,3]
b = [1,2,3]
'''
print(a==b)
print(id(a))
print(id(b))
print(a is b)

b = a
print('After b=a')
print(id(a))
print(id(b))
print(a is b)
'''
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = {'false':False,'None':None,'Zero_numeric':0,'empty_list': [],'empty_str':''}

for key,values in condition.items():
    if values:
        print(key,values)
    else:
        print(values)
