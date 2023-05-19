# -------Lista de lisbrerias y Modulos
try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    from app_Abstract.classAbm import AbmTablas

except Exception as e:
    print(f'Falta algun modulo {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def foundObject(idtabla):
    """
    OBTIENE UNA INSTANCIA DE UN DETERMINADO OBJETO\n
    Tiene un parametro.\n
    ges = es el ambiente donde esta la base de datos
    objeto_dal = idtabla es el numero de tabla\n
    dbslate = dbslate es el numero de tabla slate\n
    Retorna una instancia del objeto AbmTablas\n
    """
    try:
        return AbmTablas(
            **{'ges': GestionRegistros(ambiente=ConfigurarAplicacion.ENV_SOURCE), 'objeto_dal': idtabla, 'dbslate': None})

    except Exception as e:
        print(f'Error - foundObject {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestWrk(id, qry, idtabla):
    """
    OBTIENE LOS REGISTROS DE UNA TABLA\n
    Tiene dos parametros:\n
    id  = Es el id de inicio de busqueda si es cero se inicia desde el principio de la tabla\n
    qry = Es el codigo de consulta a utilizar segun la tabla de consultas\n
    idtabla = Es el id del objeto tabla a utilizar\n

    Lista de tabla:\n
    (1)-Estado (2)-Provincias (3)-TipoCuerpo (4)-TipoCuota (5)-TipoDocumento (6)-TipoMoneda\n
    (7)-TipoMovimiento (8)-TipoOrigen (9)-TipoPago (9)-TipoRegistro (10)-TipoSubRegistro (11)-TipoTitular\n
    (12)-TokenRegistro (13)-TokenUser (14)-ApiToken\n

    Retorna una lista de registros\n
            un dict con el error si lo hubiere\n
    """
    try:

        datos_list = list()

        # Si el id tiene el valor en cero significa que selecciona todos los registros
        # de la tabla
        if id == 0:
            consulta = {'*all': '*all'.upper()}

        # Si el id <> 0 significa que se debe tomar el id + 1 de la tabla la cantidad
        # de records esta en la etiqueta count
        else:
            if qry == 0:
                consulta = {'from': id, 'count': ConfigurarAplicacion.WRK_RECORDS}
            else:
                pass

        # Generamos una Instancia de la clase de Abm
        documentos = foundObject(idtabla)

        # Realizamos la consulta
        data_list, errores = documentos.getRecordWhere(**consulta)

        # Eliminamos ela instancia de la clase Abm
        del documentos

        return data_list, errores

    except Exception as e:
        print(f'Error - requestWrk {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Generacion de un nuevo registro en una tabla
def requestAdd(idtabla, **data):
    """
    GENERACION DE UN UN NUEVO REGISTRO EN UNA TABLA\n
    Tiene dos parametros:\n
    idtabla = Es el id del objeto tabla a utilizar\n
    data    = Es un dict con los campos para generar el registro\n

    Retorna una respuesta de la accion\n
    """

    try:

        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el insert del registro
        respuesta = documentos.insertRecord(**data)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return respuesta

    except Exception as e:
        print(f'Error - requestAdd {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestUpd(idtabla, **data):

    try:

        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el insert del registro
        respuesta = documentos.updateRecord(**data)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return respuesta

    except Exception as e:
        print(f'Error - requestUpd {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestUpdLote(idtabla, **data):

    try:

        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el update del registro por lotes
        respuesta = documentos.updateRecordLote(**data)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return respuesta

    except Exception as e:
        print(f'Error - requestUpdLote {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestGet(idtabla, **data):
    """
    GENERACION DE UN UN NUEVO REGISTRO EN UNA TABLA\n
    Tiene dos parametros:\n
    idtabla = Es el id del objeto tabla a utilizar\n
    data    = Es un dict con los campos para generar el registro\n

    Retorna una respuesta de la accion\n
            un dict con el error si lo hubiere\n
    """

    try:

        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el insert del registro
        registros, error = documentos.getRecord(**data)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return registros, error

    except Exception as e:
        print(f'Error - requestGet {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestGetCondicion(idtabla, **data):
    """
    GENERACION DE UN UN NUEVO REGISTRO EN UNA TABLA\n
    Tiene dos parametros:\n
    idtabla = Es el id del objeto tabla a utilizar\n
    data    = Es un dict con los campos para generar el registro\n

    Retorna una respuesta de la accion\n
            un dict con el error si lo hubiere\n
    """

    try:

        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el insert del registro
        registros, error = documentos.getRecordCondition(**data)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return registros, error

    except Exception as e:
        print(f'Error - requestGetCondicion {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestFormatUpdate(idtabla):
    """
    GENERACION DE UN UN NUEVO REGISTRO EN UNA TABLA\n
    Tiene dos parametros:\n
    idtabla = Es el id del objeto tabla a utilizar\n
    data    = Es un dict con los campos para generar el registro\n

    Retorna una respuesta de la accion\n
    """

    try:


        # Generamos una Instancia de la clase de AbmTabla
        documentos = foundObject(idtabla)

        # Realiza el insert del registro
        formatUpdate = documentos.update

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return formatUpdate

    except Exception as e:
        print(f'Error - requestFormatUpdate {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def requestComand(ambiente, sql, *parametros):
    """
    GENERACION DE UN COMANDO DEL MOTOR DE BASE DE DATOS\n
    Tiene dos parametros:\n
    ambiente = Es el ambiente del motor de base de datos\n
    sql    = Es la sentencia sql\n
    parametros = son los parametros que va a utilizar la sentencia sql\n

    Retorna una respuesta de la accion\n
    """
    try:
        # Generamos una Instancia de la clase de Gestion de Registros
        documentos = GestionRegistros(ambiente=ambiente)

        # Realiza la ejecucion del comando
        retorno = documentos.run_comando(sql, *parametros)

        # Eliminamos ela instancia de la clase de AbmTabla
        del documentos

        return retorno
    except Exception as e:
        print(f'Error - requestComand {e}')
