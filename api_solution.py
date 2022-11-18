import requests
import json

response = requests.get('https://api.datos.gob.mx/v1/calidadAire').text
json_ = json.loads(response)

  # Funcion para extraers valores de json
def keys_get_values(_json):
    list_values=[]
    for items,values in _json.items():
        list_values.append(items)
        list_values.append(values)
    return list_values

 # Funcion para coincidencia
def get_value(_list,name,value):
    lista = []
    for k in _list:
        if value in k[name]:
            lista.append(k)
    return lista

 # Funcion para encontrar coincidencias en otras clases
def found_match(_list,string):
    lista_value = []
    for key in range(len(_list)):
        value = _list[key]['stations'][0]['measurements']
        if value == []:
            continue
        else:
            extraction = value[0]['pollutant']
            if extraction == string:
                lista_value.append(_list[key])
    return lista_value


 # PRIMER PUNTO 
init_list = keys_get_values(json_)
data =get_value(init_list[3],'_id','58c780bf281e87010078f491')
dictionary = (data[0]['stations'][0]['measurements'][0])
data_save = {'value':dictionary['value'],'unit':dictionary['unit'],'pollutant':dictionary['pollutant']}
print(data_save)

 # SEGUNDO PUNTO
value_match = data_save['pollutant']
dictionary_end = found_match(init_list[3],value_match)
result = {'_id':dictionary_end[len(dictionary_end)-1]['_id']}
print(result)
