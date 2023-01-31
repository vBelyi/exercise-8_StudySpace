def mane_function (*args):
    main_dict = {}
    for elements in args:
        main_dict.update(elements)
    return main_dict
dict1 = {'Audi': 'A3', 'Mercedes': 'A-Class', 'BMW': 1}
dict2 = {'Renault': 'Megan', 'Pegeout': '505'}
dict3 = {'Dacia': 'Logan', 'Volvo': 'S60'}
print(mane_function(dict1, dict2, dict3))
