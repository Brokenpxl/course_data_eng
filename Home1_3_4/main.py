def checkio(expression):
    list_backets = []

    for i in expression:
        if i == "[" or i == "]" or i == "(" or i == ")" or i == "{" or i == "}":
            list_backets.append(i) #создаю список нужных нам элементов

    if len(list_backets) == 0: #если нет элементов вовсе
        return True

    elif list_backets.count("[") == list_backets.count("]") and list_backets.count("(") == list_backets.count(")") and list_backets.count("{") == list_backets.count("}"):
      #если количество "(" равно количеству ")" и так далее...
        j = 0
        try:
            while j != range(len(list_backets)): #попытка найти в списке соседние скобки
                if list_backets[j] == "(" and list_backets[j+1] == ")":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "{" and list_backets[j+1] == "}":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                elif list_backets[j] == "[" and list_backets[j+1] == "]":
                    list_backets.pop(j)
                    list_backets.pop(j)
                    j = 0
                else:
                    j += 1

        except:
            if (len(list_backets)) == 0:
                return True
            else:
                return False

    else:
            return False