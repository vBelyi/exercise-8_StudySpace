def mane_function (*args):
    main_dict = {}
    for elements in args:
        main_dict.update(elements)
    return main_dict
dict1 = {'Audi': 'A3', 'Mercedes': 'A-Class', 'BMW': 1}
dict2 = {'Renault': 'Megan', 'Pegeout': '505'}
dict3 = {'Dacia': 'Logan', 'Volvo': 'S60'}
dict4 = {'Apple': 'fruit', 'Potato': 'vegetable'}
dict5 = {'Rabbit':'animal', 'Jake': 'human' }
dict6 = {'Asus':'TUF gaming', 'DELL':'Latitude'}
print(mane_function(dict1, dict2, dict3, dict4, dict5, dict6))

def test_function(month):
    if month == 1 or month == 2 or month == 12:
        return 'Winter'
    elif month == 3 or month == 4 or month == 5:
        return 'Spring'
    elif month == 6 or month == 7 or month == 8:
        return 'Summer'
    elif month == 9 or month == 10 or month == 11:
        return 'Autumn'
    else:
        return 'There is only 12 monthes in the year'
print(test_function(int(input('Click here to input a number of month to know a time of the year: '))))
