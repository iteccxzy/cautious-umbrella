
my_dict = {'name': 'Gabrielito', 'dir': 'pasaje villanueba'}

def main(my_dict):
    my_dict['id'] = 10
    del my_dict['name']
    my_dict.clear()

    my_dict = [{'name': 'Horacio', 'id': 88},
               {'name': 'Gabrielito', 'id': 147}]

    print(sorted(my_dict, key=lambda e: e['id'], reverse=True))


if __name__ == '__main__':
    main(my_dict)
