def hello_func(greeting):
    return '{} Function'.format(greeting)

print(hello_func)
print(hello_func('Hey!'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Maths','History',name='Purvak',age=20)

#output -
# Args gives tuples as output while kwargs gives Dictionary
#('Maths', 'History')
#{'name': 'Purvak', 'age': 20}
