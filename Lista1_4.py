def duplikaty(lista):
    listaWynikowa = list(set(lista))
    return listaWynikowa


print duplikaty(['kot', 'pies', 'pies', 'kot', 'kura', 'pies', 'ryba', 'pies', 'krowa'])