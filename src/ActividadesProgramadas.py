df = pd.DataFrame([
    dict(Tarea="Revisar y analizar cada uno de los requisitos y exigencias del software", FechaInicio='2024-09-20', FechaFin='2024-09-29', Responsable='Sebastian'),
    dict(Tarea="Diseñar la estructura, funcionalidades y parte estetica del software", FechaInicio='2024-09-20', FechaFin='2024-11-22', Responsable='Lorena'),
    dict(Tarea="Clonar el repositorio inicial", FechaInicio='2024-09-24', FechaFin='2024-09-24', Responsable='Lorena'),
    dict(Tarea="Desarrollar las funciones para la gestion de turnos y el registro de pacientes", FechaInicio='2024-10-01', FechaFin='2024-10-20', Responsable='Sebastian'),
    dict(Tarea="Programar el registro de datos en DataFrame y exportación a archivos CSV", FechaInicio='2024-10-15', FechaFin='2024-10-30', Responsable='Lorena'),
    dict(Tarea="Probar el software y corregir errores", FechaInicio='2024-11-01', FechaFin='2024-11-22', Responsable='Lorena'),
    dict(Tarea="Probar el software y corregir errores", FechaInicio='2024-11-01', FechaFin='2024-11-22', Responsable='Sebastian'),
    dict(Tarea="Crear el manual del usuario", FechaInicio='2024-11-20', FechaFin='2024-11-23', Responsable='Sebastian'),
    dict(Tarea="Crear el manual del usuario", FechaInicio='2024-11-20', FechaFin='2024-11-23', Responsable='Lorena')
])

df = df.sort_values(by='Tarea')
fig = px.timeline(
    df,
    x_start="FechaInicio",
    x_end="FechaFin",
    y="Tarea",
    color='Responsable',
    category_orders={'Tarea': sorted(df['Tarea'].tolist(), reverse=True)}
)
fig.update_yaxes(autorange="reversed")
fig.show()
