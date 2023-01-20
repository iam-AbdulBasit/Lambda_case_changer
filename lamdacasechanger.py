mysmall_list = ['a','b','c','d','e']

#def case_changer(character_value):
#   return character_value.upper()
case_changer = lambda mysmall_list : mysmall_list.upper()
final_values = map(case_changer,mysmall_list)
print(list(final_values))