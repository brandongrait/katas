def life_path_number(birthdate):
    dic = birthdate.split("-")
    aux = 0
    for element in dic:
        suma_fecha = sum(list(map(int,list(element))))
        if len(str(suma_fecha)) > 1:
            suma_fecha = sum(list(map(int,list((str(suma_fecha))))))
        aux += suma_fecha
    while len(str(aux)) > 1:
        aux = sum(list(map(int,list(str(aux)))))
    return aux    
print(life_path_number("4266-11-17"))

