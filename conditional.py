# a  calculator appllication made using
# varaiables and if statements 

# 1. get input from the user
# 2. do calculation based on the user input
#2.1 check what string did user typed
#2.2 if user string == *then do
# 3. give output to the user

print ('* for multiplication')
print('+ for addition')
print ('_ for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print ('user input_type', type(whatUserTyped))

if whatUserTyped == "+":
    print ('Doing Addition')
    print ('doing more addition')

if whatUserTyped == "_":
    print ('Doing subtraction')
    print ('doing more subtraction')

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')