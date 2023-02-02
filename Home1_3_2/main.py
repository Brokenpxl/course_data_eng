string = input('Введите слово: ')
string = string.replace(" ", "")
string_reversed = reversed(string)
#
if "yes" == "".join(set(["yes" if i == j else "no" for i, j in zip(string, string_reversed)])):
    print("yes")
else:
    print("no")