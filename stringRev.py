# name="saksham"
# reverse_name=name[::-1]
# print(reverse_name)

# string="hello world"
# rev=""
# for char in string:
#     rev=char + rev 
# print(rev)

def reverse_string(s):
    if len(s) == 0 :
        return s 
    else :
        return reverse_string(s[1:]) + s[0]
string="milan world"
rev=reverse_string(string)
print(rev)


