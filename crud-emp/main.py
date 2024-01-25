from fastapi import FastAPI, Body,Path,Query#body,path y query son funciones que no utilizas ya que optamos por otro tipo de filtrado
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List



app = FastAPI()
app.title = "Sistema de Gestion de Empleados"
app.version = "0.0.1" 


#Schema

class Empleado(BaseModel):
    id: Optional[int] = None
    Nombre: Optional[str]  = Field ()
    Apellido: Optional[str] = Field()
    Nacimiento: Optional[str] = Field(max_length=10, min_length=10)
    Puesto: Optional[str] = Field()
    Empresa: Optional[str] = Field()
    Ingreso: Optional[str] = Field(max_length=10, min_length=10)

    class Config:
        json_schema_extra = {
            "example": [
                {
                "id":"id",
                "Nombre":"Ingrese el nombre",
                "Apellido":"Ingrese el Apellido",
                "Nacimiento":"Fecha de nacimiento con formato 00/00/0000",
                "Puesto":"Ingrese el Puesto",
                "Empresa":"Ingrese la Empresa",
                "Ingreso":"Fecha de ingreso con formato 00/00/0000"
                }
            ]
        }
    


empleados = [
     {
        "id"        : 1,
        "Nombre"    : "Jeremias",
        "Apellido"  : "De souza",
        "Nacimiento": "20/02/1990",
        "Puesto"    : "Proximity",
        "Empresa"   : "NPO",
        "Ingreso"   : "01/05/2023",              
    },
    {
        "id"        : 2,
        "Nombre"    : "Nicolas",
        "Apellido"  : "Vicentini",
        "Nacimiento": "20/02/1990",
        "Puesto"    : "Proximity",
        "Empresa"   : "NPO",
        "Ingreso"   : "01/09/2023",              
    },
    {
        "id"        : 3,
        "Nombre"    : "Marcos",
        "Apellido"  : "Ludueña",
        "Nacimiento": "20/02/1990",
        "Puesto"    : "Proximity",
        "Empresa"   : "NyC",
        "Ingreso"   : "02/02/2022",              
    },
    {
        "id"        : 4,
        "Nombre"    : "Juan",
        "Apellido"  : "Pessini",
        "Nacimiento": "20/02/1990",
        "Puesto"    : "Proximity",
        "Empresa"   : "NyC",
        "Ingreso"   : "02/06/2022",              
    }
]


# FUNCIONES 


# Muestra html en local   

@app.get('/', tags = ["home"])
def message():
    return  HTMLResponse('<html lang="es"><head><meta charset="utf-8"><title>Sistema de gestion de empleados</title></head><body><h1>Sistema de gestion de empleados</h1> <p>Nuevo empleado</p><p>Borrar empleado</p><p>Editar empleado</p></body></html> ')


#Trae la lista de empleados

@app.get('/empleados', tags = ["empleados"], response_model = List[Empleado], status_code = 200)
def get_empleados() -> List [Empleado] :
    return JSONResponse(status_code = 200, content=empleados)


  
#Filtrado de empleados

@app.get('/empleados/', tags = ["empleados"], response_model = List[Empleado])
def filter_empleados(id:int= None,Nombre:str = None, Apellido:str = None, Nacimiento:str = None, Puesto:str = None, Empresa:str = None, Ingreso:str = None) -> List[Empleado]:
    for item in empleados:
        if item["id"] == id:
            return item
        elif item["Nombre"] == Nombre:
            return [ item for item in empleados if item ["Nombre"] == Nombre] 
        elif item["Apellido"] == Apellido:
            return [ item for item in empleados if item ["Apellido"] == Apellido]
        elif item["Nacimiento"] == Nacimiento:
            return [ item for item in empleados if item ["Nacimiento"] == Nacimiento]
        elif item["Puesto"] == Puesto:
            return [ item for item in empleados if item ["Puesto"] == Puesto]
        elif item["Empresa"] == Empresa:
            return [ item for item in empleados if item ["Empresa"] == Empresa]
        elif item["Ingreso"] == Ingreso:
            return [ item for item in empleados if item ["Ingreso"] == Ingreso]
    return JSONResponse(status_code=404, content=[])

#Creacion de empleados

@app.post('/empleados', tags = ["empleados"], response_model = dict, status_code = 201)
def crear_empleado(empleado: Empleado) -> dict:
    empleados.append(empleado) 
    return JSONResponse(status_code = 201, content = {"message":"Se ha creado correctamente el empleado"})

#Eliminacion de empleados

@app.delete('/empleados/{id}', tags = ["empleados"], response_model = dict, status_code = 200)
def borrar_empleado(id:int) -> dict:
      for item in empleados:
        if item["id"]==id:
            empleados.remove(item)
            return JSONResponse(status_code = 200, content = {"message":"Se ha eliminado correctamente el empleado"})
        else:
            return JSONResponse(status_code=404, content=[])
      
#Edicion de empleados
      
@app.put('/empleados/{id}', tags = ["empleados"], response_model = dict, status_code = 200)
def editar_empleado(id:int, empleado:Empleado) -> dict:
    for item in empleados:
        if item["id"] == id:
            item['Nombre'] = empleado.Nombre,
            item['Apellido'] = empleado.Apellido,
            item['Nacimiento'] = empleado.Nacimiento,
            item['Puesto'] = empleado.Puesto,
            item['Empresa'] = empleado.Empresa,
            item['Ingreso'] = empleado.Ingreso,
            return JSONResponse(status_code = 200, content={"message":"Se ha editado correctamente el empleado"})
        else:
            return JSONResponse(status_code=404, content=[])
        
