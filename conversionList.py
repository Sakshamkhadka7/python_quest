# list to tuple conversion
my_list=[1,2,3,4,5]
my_tuple=tuple(my_list)
print(my_tuple);

# tuple to list conversion
tuple_array=(2,4,6,8)
list_array=list(tuple_array)
print(list_array)

# string conversion
string_conversion="hello"
tuple_string=tuple(string_conversion)
print(tuple_string)

# tuplestring to string 
tuples_string=["s","a","k","h","a","m"]
string_conv="".join(tuples_string)
print(string_conv)

# dict into tuple 
student={
    "name":"saksham",
     "class":"4 sem",
     "roll":32
}

dict_to_tuple=tuple(student)
print(dict_to_tuple)

# tuple into dict 
tuple_dict=(('name','saksham'),('roll',30),('address','balkumari'))
print(dict(tuple_dict))
