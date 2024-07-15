string1 = 'abc'
string2 = 'string'

if len(string1) >= 3:
    if string1.endswith('ing'):
        modified_string1 = string1 + 'ly'
    else:
        modified_string1 = string1 + 'ing'
else:
    modified_string1 = string1

if len(string2) >= 3:
    if string2.endswith('ing'):
        modified_string2 = string2 + 'ly'
    else:
        modified_string2 = string2 + 'ing'
else:
    modified_string2 = string2

print("Modified string 1:", modified_string1)
print("Modified string 2:", modified_string2)