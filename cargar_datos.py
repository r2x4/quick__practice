import pandas as pd
from sqlalchemy import create_engine

# Cargar CSV
df = pd.read_csv('base_limpia.csv', encoding='utf-8', low_memory=False)

# Verificar columnas
print("Columnas disponibles:", df.columns.tolist())

# Conexión a PostgreSQL
usuario = "postgres"
contraseña = "Dragon2307*"
host = "localhost"
puerto = "5432"
base_datos = "basedatos_colab"

# Crear motor de conexión
engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

# Preparar tabla: clientes
df_clientes = df[[ 
    "documento_cliente", "nombre_cliente", "numero_telefono",
    "Correo Cliente", "Tipo de Documento", "Municipio", "Departamento"
]].drop_duplicates()

# Preparar tabla: servicios
df_servicios = df[[ 
    "numero_del_servicio", "estado", "creado_por", "documento_cliente",
    "fecha_de_servicio", "direccion_servicio", "barrio", "zona",
    "descripcion", "Tipo de servicio", "Valor del pedido", "Recaudo", "Valor Flete",
    "codigo_cedi", "Documento del Conductor del Recurso"
]].drop_duplicates()

# Preparar tabla: cedis
df_cedis = df[[ 
    "codigo_cedi", "nombre_cedi"
]].drop_duplicates()

# Preparar tabla: conductores
df_conductores = df[[ 
    "Documento del Conductor del Recurso", "Conductor", "Recurso"
]].drop_duplicates()

# Preparar tabla: eventos del servicio
columnas_eventos = [
    "numero_del_servicio", "fecha_de_servicio", "fecha_cirugia", "fecha_de_creacion",
    "tiempo_de_promesa", "asignado", "atendido", "finalizado", "recibido_picking",
    "duracion_total", "tiempo_desplazamiento", "tiempo_atencion",
    "tiempo_atencion_min", "duracion_total_min", "tiempo_desplazamiento_min",
    "tiempo_total_creacion_final", "tiempo_total_creacion_final_hrs",
    "cumple_promesa", "tiempo_real", "cumplimiento_promesa",
    "diferencia_total_creacion_final_hrs", "diferencia_total_creacion_final_min",
    "diferencia_tiempo_real_teorico_hrs", "diferencia_tiempo_real_teorico_min",
    "velocidad_servicio", "nivel_cumplimiento", "desempeno_operador",
    "categoria_servicio", "estado_cumplimiento"
]

# Validación: solo incluir columnas que sí existen en el DataFrame
columnas_existentes = [col for col in columnas_eventos if col in df.columns]

# Crear el DataFrame final
df_eventos = df[columnas_existentes].drop_duplicates()



# Cargar los DataFrames a PostgreSQL
df_clientes.to_sql("clientes", engine, index=False, if_exists="replace")
df_servicios.to_sql("servicios", engine, index=False, if_exists="replace")
df_cedis.to_sql("cedis", engine, index=False, if_exists="replace")
df_conductores.to_sql("conductores", engine, index=False, if_exists="replace")
df_eventos.to_sql("eventos_servicio", engine, index=False, if_exists="replace")

print("✅ Datos cargados exitosamente en PostgreSQL.")


