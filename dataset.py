
#id, nombre, cantidad
areas = [
    [1, "Produccion", 0],
    [2, "Mantenimiento", 0],
    [3, "Calidad", 0],
    [4, "Logística y Depósito", 0],
    [5, "Administración y Finanzas", 0],
    [6, "Compras", 0],
    [7 ,"Ingeniería y Desarrollo",0], 
    [8, "Recursos Humanos",0],
    [9, "Ventas y Atención al Cliente",0],
    [10, "Dirección General",0]
]
#id, id_empleado, fecha, id_justificacion
licencias = [
    [1, 1, "2024-03-12", 1],   # Juan Pérez - Enfermedad común
    [2, 2, "2024-05-10", 4],   # María González - Consulta médica
    [3, 3, "2024-06-15", 3],   # Lucas Fernández - Accidente no laboral
    [4, 5, "2024-01-20", 6],   # Martín Sosa - Vacaciones
    [5, 4, "2024-03-05", 7],   # Carla Rodríguez - Asuntos personales
    [6, 6, "2024-02-14", 2],   # Florencia Castro - Accidente laboral
    [7, 7, "2024-04-22", 10],  # Santiago López - Jornada electoral
    [8, 8, "2024-07-01", 8],   # Jazmín Romero - Trámite oficial
    [9, 9, "2024-06-28", 1],   # Nicolás Herrera - Enfermedad común
    [10, 10, "2024-02-02", 5], # Valeria Núñez - Internación
    [11, 11, "2024-03-08", 11],# Pablo Ruiz - Fallecimiento familiar directo
    [12, 12, "2024-04-17", 9], # Antonella Benítez - Examen académico
    [13, 13, "2024-01-11", 13],# Julián Medina - Nacimiento de hijo
    [14, 14, "2024-08-01", 14],# Camila Torres - Paternidad
    [15, 3, "2024-05-30", 6],  # Lucas Fernández - Vacaciones
]

#id, justificacion
justificaciones = [
    [1, "Enfermedad común", "Médicas"],
    [2, "Accidente laboral", "Médicas"],
    [3, "Accidente no laboral", "Médicas"],
    [4, "Consulta médica", "Médicas"],
    [5, "Internación", "Médicas"],
    [6, "Vacaciones", "Personales / Legales"],
    [7, "Asuntos personales", "Personales / Legales"],
    [8, "Trámite oficial", "Personales / Legales"],
    [9, "Examen académico", "Personales / Legales"],
    [10, "Jornada electoral", "Personales / Legales"],
    [11, "Fallecimiento familiar directo", "Fallecimiento"],
    [12, "Fallecimiento familiar no directo", "Fallecimiento"],
    [13, "Nacimiento de hijo", "Familiar"],
    [14, "Paternidad", "Familiar"],
    [15, "Adopción", "Familiar"]
]
#id, nombre y apellido, telefono, posición, area, estado, fecha de ingreso, fecha de nacimiento
empleados = [
    [1, "Juan", "Pérez", "1123456789", "Operario", 1, "Activo", "2019-03-15", "1987-06-12"],
    [2, "María", "González", "1165432109", "Técnica", 2, "Activo", "2020-07-01", "1991-04-23"],
    [3, "Lucas", "Fernández", "1132123456", "Analista", 3, "Activo", "2021-01-10", "1995-09-18"],
    [4, "Carla", "Rodríguez", "1145678910", "Administrativa", 5, "Activo", "2018-11-05", "1989-11-02"],
    [5, "Martín", "Sosa", "1176543210", "Operario", 4, "Activo", "2022-02-20", "1994-01-30"],
    [6, "Florencia", "Castro", "1198765432", "Ingeniera", 7, "Activo", "2017-06-12", "1985-07-19"],
    [7, "Santiago", "López", "1123987654", "Jefe de área", 1, "Activo", "2015-08-01", "1982-03-11"],
    [8, "Jazmín", "Romero", "1154321890", "Recepcionista", 8, "Activo", "2023-04-01", "2000-05-07"],
    [9, "Nicolás", "Herrera", "1167894321", "Técnico", 2, "Activo", "2020-10-22", "1992-08-14"],
    [10, "Valeria", "Núñez", "1134765890", "Contadora", 5, "Activo", "2016-09-12", "1988-12-05"],
    [11, "Pablo", "Ruiz", "1143217654", "Chofer", 4, "Activo", "2021-12-03", "1990-06-25"],
    [12, "Antonella", "Benítez", "1176549870", "Especialista", 3, "Activo", "2019-01-14", "1993-02-28"],
    [13, "Julián", "Medina", "1134567890", "Encargado", 6, "Activo", "2018-05-22", "1986-10-10"],
    [14, "Camila", "Torres", "1123897654", "HR Generalist", 8, "Activo", "2022-08-08", "1997-03-03"]
]
