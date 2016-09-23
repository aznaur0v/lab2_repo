ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 24,
    },{
        "name": "petja",
        "age": 19,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    },{
        "name": "pavel",
        "age": 23,
    }],
}

maxim={
    "name": "maxim",
    "age": 45,
    "children": [{
        "name": "alex",
        "age": 23,
    },{
        "name": "pavel",
        "age": 19,
    }],
}
emps = [ivan, darja, maxim]

#функция для поиска сотрудников, у которых есть дети старше 18 лет
def filter(emps, age_limit):
    filtered =[]
    for emp in emps:
        for child in emp['children']:
            if child['age'] >= age_limit:
                #print(emp['name'])
                filtered.append(emp['name'])
                break
    for i in range(len(filtered)):
        print(i+1,':',filtered[i])
    return filtered
#sorted = filter(emps, 19)
print('Имена сотрудников, у которых есть дети старше 18 лет:')
filter(emps,19)
#print(sorted)