# id, nombre, cantidad, Activo
areas = [
    [0, "Staff", 0, "Activo"],
    [1, "Produccion", 3, "Activo"],               # Juanceto01, Juan Perez, Martin Sosa     
    [2, "Mantenimiento", 2, "Activo"],            # Maria Gonzalez, Nicolas Herrera
    [3, "Calidad", 2, "Activo"],                  # Lucas Fernandez, Antonella Benitez
    [4, "Logistica y Deposito", 2, "Activo"],     # Martin Sosa, Pablo Ruiz
    [5, "Administracion y Finanzas", 2, "Activo"],# Carla Rodriguez, Valeria Nunez
    [6, "Compras", 1, "Activo"],                  # Julian Medina
    [7, "Ingenieria y Desarrollo", 1, "Activo"],  # Florencia Castro
    [8, "Recursos Humanos", 2, "Activo"],         # Jazmin Romero, Camila Torres
    [9, "Ventas y Atencion al Cliente", 0, "Activo"],
    [10, "Direccion General", 0, "Activo"]
]

# id, id_empleado, fecha, id_justificacion, Activo
licencias = [
    [0, 1, "2024-2-2", 1, "Activo"],    # Juan Pérez - Enfermedad común
    [1, 1, "2024-3-12", 1, "Activo"],   # Juan Pérez - Enfermedad común
    [2, 2, "2024-5-10", 4, "Activo"],   # María González - Consulta médica
    [3, 3, "2024-6-15", 3, "Activo"],   # Lucas Fernández - Accidente no laboral
    [4, 5, "2024-1-20", 6, "Activo"],   # Martín Sosa - Vacaciones
    [5, 4, "2024-3-5", 7, "Activo"],   # Carla Rodríguez - Asuntos personales
    [6, 6, "2024-2-14", 2, "Activo"],   # Florencia Castro - Accidente laboral
    [7, 7, "2024-4-22", 10, "Activo"],  # Santiago López - Jornada electoral
    [8, 8, "2024-7-1", 8, "Activo"],   # Jazmín Romero - Trámite oficial
    [9, 9, "2024-6-28", 1, "Activo"],   # Nicolás Herrera - Enfermedad común
    [10, 10, "2024-2-2", 5, "Activo"], # Valeria Núñez - Internación
    [11, 11, "2024-3-8", 11, "Activo"],# Pablo Ruiz - Fallecimiento familiar directo
    [12, 12, "2024-4-17", 9, "Activo"], # Antonella Benítez - Examen académico
    [13, 13, "2024-1-11", 13, "Activo"],# Julián Medina - Nacimiento de hijo
    [14, 14, "2024-8-1", 14, "Activo"],# Camila Torres - Paternidad
    [15, 3, "2024-5-30", 6, "Activo"],  # Lucas Fernández - Vacaciones
]

# id, justificacion, tipo
justificaciones = [
    [0, "No enfermedad", "-"],
    [1, "Enfermedad comun", "Medicas"],
    [2, "Accidente laboral", "Medicas"],
    [3, "Accidente no laboral", "Medicas"],
    [4, "Consulta medica", "Medicas"],
    [5, "Internacion", "Medicas"],
    [6, "Vacaciones", "Personales / Legales"],
    [7, "Asuntos personales", "Personales / Legales"],
    [8, "Tramite oficial", "Personales / Legales"],
    [9, "Examen academico", "Personales / Legales"],
    [10, "Jornada electoral", "Personales / Legales"],
    [11, "Fallecimiento familiar directo", "Fallecimiento"],
    [12, "Fallecimiento familiar no directo", "Fallecimiento"],
    [13, "Nacimiento de hijo", "Familiar"],
    [14, "Paternidad", "Familiar"],
    [15, "Adopcion", "Familiar"]
]

# id, nombre y apellido, telefono, posicion, area, estado, fecha de ingreso, fecha de nacimiento,
empleados = [
    [0, "Juanceto01", "+541112345678", "Operario", 1, "Activo", "2019-3-15", "1987-6-12"],
    [1, "Juan Perez", "+541187654321", "Operario", 1, "Activo", "2019-3-15", "1987-6-12"],
    [2, "Maria Gonzalez", "+541198765432", "Tecnica", 2, "Activo", "2020-7-1", "1991-4-23"],
    [3, "Lucas Fernandez", "+541143216789", "Analista", 3, "Activo", "2021-1-10", "1995-9-18"],
    [4, "Carla Rodriguez", "+541154329876", "Administrativa", 5, "Activo", "2018-11-5", "1989-11-2"],
    [5, "Martin Sosa", "+541165498732", "Operario", 4, "Activo", "2022-2-20", "1994-1-30"],
    [6, "Florencia Castro", "+541176543219", "Ingeniera", 7, "Activo", "2017-6-12", "1985-7-19"],
    [7, "Santiago Lopez", "+541187654320", "Jefe de area", 1, "Activo", "2015-8-1", "1982-3-11"],
    [8, "Jazmin Romero", "+541132165498", "Recepcionista", 8, "Activo", "2023-4-1", "2000-5-7"],
    [9, "Nicolas Herrera", "+541154321987", "Tecnico", 2, "Activo", "2020-10-22", "1992-8-14"],
    [10, "Valeria Nunez", "+541165498713", "Contadora", 5, "Activo", "2016-9-12", "1988-12-5"],
    [11, "Pablo Ruiz", "+541143219876", "Chofer", 4, "Activo", "2021-12-3", "1990-6-25"],
    [12, "Antonella Benitez", "+541154329871", "Especialista", 3, "Activo", "2019-1-14", "1993-2-28"],
    [13, "Julian Medina", "+541165498721", "Encargado", 6, "Activo", "2018-5-22", "1986-10-10"],
    [14, "Camila Torres", "+541176543218", "HR Generalist", 8, "Activo", "2022-8-8", "1997-3-3"]
]

# id, username, password, dni, nivel_acceso, email, estado
usuarios = [
    {"id": 0, "username": "juanp", "password": "juanp", "dni": "40123456", "nivel_acceso": "admin", "email": "juanp@empresa.com", "estado": "Activo"},
    {"id": 1, "username": "maria.g", "password": "mg2024", "dni": "38987456", "nivel_acceso": "user", "email": "maria.g@empresa.com", "estado": "Activo"},
    {"id": 2, "username": "lucasf", "password": "lfpass", "dni": "42111444", "nivel_acceso": "admin", "email": "lucasf@empresa.com", "estado": "Activo"},
    {"id": 3, "username": "c.rodriguez", "password": "cro2025", "dni": "40998877", "nivel_acceso": "user", "email": "c.rodriguez@empresa.com", "estado": "Activo"},
    {"id": 4, "username": "martins", "password": "mssecure", "dni": "37123987", "nivel_acceso": "admin", "email": "martins@empresa.com", "estado": "Activo"},
    {"id": 5, "username": "florcastro", "password": "florc99", "dni": "43111822", "nivel_acceso": "user", "email": "florcastro@empresa.com", "estado": "Activo"},
    {"id": 6, "username": "slopez", "password": "slpass01", "dni": "39100234", "nivel_acceso": "guest", "email": "slopez@empresa.com", "estado": "Activo"},
    {"id": 7, "username": "jazminr", "password": "jrpass23", "dni": "45122119", "nivel_acceso": "user", "email": "jazminr@empresa.com", "estado": "Activo"},
    {"id": 8, "username": "nicolas.h", "password": "nh4567", "dni": "36123455", "nivel_acceso": "user", "email": "nicolas.h@empresa.com", "estado": "Activo"},
    {"id": 9, "username": "valenunez", "password": "vnpass77", "dni": "38122345", "nivel_acceso": "guest", "email": "valenunez@empresa.com", "estado": "Activo"},
    {"id": 10, "username": "pablor", "password": "prpass33", "dni": "40123345", "nivel_acceso": "user", "email": "pablor@empresa.com", "estado": "Activo"},
    {"id": 11, "username": "antonella.b", "password": "abpass22", "dni": "42110999", "nivel_acceso": "user", "email": "antonella.b@empresa.com", "estado": "Activo"},
    {"id": 12, "username": "julianm", "password": "jmsecure", "dni": "37111777", "nivel_acceso": "admin", "email": "julianm@empresa.com", "estado": "Activo"},
    {"id": 13, "username": "cami.t", "password": "ctpass44", "dni": "45122000", "nivel_acceso": "guest", "email": "cami.t@empresa.com", "estado": "Activo"},
    {"id": 14, "username": "sofia.l", "password": "slkey55", "dni": "38122999", "nivel_acceso": "user", "email": "sofia.l@empresa.com", "estado": "Activo"}
]

# operacion, entidad afectada, fecha
historial_operaciones = [
    ("Registrar Licencia", "Juan Perez" , "2025-3-15"),
    ("Eliminar Empleado", "Maria Gonzalez" , "2025-3-16"),
    ("Editar Area", "Staff" , "2025-3-17"),
    ("Registrar Empleado", "Carla Rodriguez" , "2025-3-18"),
    ("Registrar Usuario", "Martin Sosa" , "2025-3-19"),
    ("Eliminar Usuario", "Florencia Castro" , "2025-3-20"),
    ("Editar Empleado", "Santiago Lopez" , "2025-3-21"),
    ("Registrar Area", "Ventas y Atencion al Cliente" , "2025-3-22"),
    ("Editar Area", "Staff" , "2025-3-23"),
    ("Editar Usuario", "Valeria Nunez" , "2025-3-24"),
    ("Registrar Licencia", "Pablo Ruiz" , "2025-3-25"),
    ("Eliminar Empleado", "Antonella Benitez" , "2025-3-26"),
    ("Editar Area", "Direccion General" , "2025-3-27"),
    ("Registrar Empleado", "Camila Torres" , "2025-3-28"),
    ("Registrar Usuario", "Sofia Lopez" , "2025-3-29"),
    ("Eliminar Usuario", "Lucas Fernandez" , "2025-3-30"),
    ("Editar Empleado", "Maria Gonzalez" , "2025-3-31"),
    ("Registrar Area", "Staff" , "2025-4-1"),
    ("Eliminar Area", "Staff" , "2025-4-2"),
    ("Editar Usuario", "Martin Sosa" , "2025-4-3")
]

archivos = [
    r'matrices/empleados.csv',
    r'matrices/areas.csv',
    r'matrices/licencias.csv',
    r'matrices/justificaciones.csv'
]