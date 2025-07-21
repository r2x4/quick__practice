from sqlalchemy import create_engine

# Datos de conexión
usuario = "postgres"
contraseña = "Dragon2307*"
host = "localhost"
puerto = "5432"
base_datos = "basedatos_colab"

# Crear el engine
engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

# CLIENTES
df_clientes = base_limpia[[
    "documento_cliente", "nombre_cliente", "numero_telefono",
    "correo_cliente", "tipo_documento", "municipio", "departamento"
]].drop_duplicates()

# SERVICIOS
df_servicios = base_limpia[[
    "numero_del_servicio", "estado", "creado_por", "documento_cliente",
    "fecha_de_servicio", "direccion_servicio", "barrio", "zona",
    "descripcion", "tipo_servicio", "valor_del_pedido", "recaudo", "valor_flete"
]].drop_duplicates()

# CEDIS
df_cedis = base_limpia[[
    "codigo_cedi", "nombre_cedi"
]].drop_duplicates()

# CONDUCTORES
df_conductores = base_limpia[[
    "documento_conductor", "nombre_conductor", "recurso"
]].drop_duplicates()

# EVENTOS
df_eventos = base_limpia[[
    "numero_del_servicio", "llegado", "reprogramar", "cancelado", "atendido",
    "finalizado", "aceptado", "asignado", "recibido_picking"
]].drop_duplicates()

# Subir cada DataFrame a su tabla respectiva
df_clientes.to_sql("clientes", engine, index=False, if_exists="replace")
df_servicios.to_sql("servicios", engine, index=False, if_exists="replace")
df_cedis.to_sql("cedis", engine, index=False, if_exists="replace")
df_conductores.to_sql("conductores", engine, index=False, if_exists="replace")
df_eventos.to_sql("eventos_servicio", engine, index=False, if_exists="replace")

print("Datos subidos correctamente.")

