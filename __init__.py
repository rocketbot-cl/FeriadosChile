# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import requests



"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "getFeriado":

    try:

        date_ = GetParams('date_')
        var_ = GetParams('var_')
        print(date_,var_)

        URL_ = r"https://apis.digital.gob.cl/fl/feriados/{fecha}".format(fecha=date_)

        headers = {
            'User-Agent': 'My User Agent 1.0',
        }

        data = requests.get(URL_, headers=headers)
        data = data.json()

        print(data)

        if "error" in data:
            res = False
        else:
            res = True

        SetVar(var_, res)
    except Exception as e:
        PrintException()
        raise e

