-- TABLA (FICHA) UNION FICHA PROGRAMA --



CREATE VIEW Vista_Ficha AS
SELECT 
    f.id,
    f.numero_ficha,
    f.jornada,
    p.nombre AS nombre_programa,
    p.nivel,
    p.duracion,
    p.etapa
FROM Ficha f
INNER JOIN Programa p ON f.idPrograma = p.id;



---------------------------------------



-- TABLA (REGISTROROL) UNION REGISTRO ROL --


CREATE VIEW Vista_registro_Rol AS
SELECT 
    r.id as id_registro,
    r.username,
    r.contraseña,
	r.correo,
    r.telefono,
    r.nombre_completo,
    rl.nombre_rol,
    rl.descripcion
FROM registroROL rr
INNER JOIN registro r ON rr.idregistro = r.id
INNER JOIN Rol rl ON rr.idRol = rl.id;



----------------------------------------


-- TABLA (REGISTROFICHA) UNION REGISTRO FICHA --


CREATE VIEW Vista_Registro_Ficha AS
SELECT 
    r.id AS id_registro,
    r.username,
    r.nombre_completo,
    f.id AS id_ficha,
    f.numero_ficha,
    f.jornada,
    p.nombre AS nombre_programa,
    p.nivel,
    p.duracion,
    p.etapa
FROM registro r
INNER JOIN registroRol rr ON r.id = rr.idregistro
INNER JOIN programaFicha pf ON pf.id = rr.idRol  -- Revisa esta relación
INNER JOIN Ficha f ON f.id = pf.idFicha
INNER JOIN Programa p ON p.id = pf.idprograma;

-----------------------------------------


-- TABLA (INSTRUCTORASIGNATURA)  UNION INTRUCTOR, ASIGNATURA Y REGISTRO)  --



CREATE VIEW Vista__Asignatura AS
SELECT 
    e.idregistro AS id_especialidad,
    r.username,
    r.nombre_completo,
    a.id AS id_asignatura,
    a.nombre AS nombre_asignatura,
    a.intensidad_horaria
FROM especialidadAsignatura e
INNER JOIN especialidad e ON ia.idespecialidad = e.idregistro
INNER JOIN registro r ON i.idregistro = r.id
INNER JOIN Asignatura a ON ea.idAsignatura = a.id;



--------------------------------------------

-- TABLA (CLASE) UNION DE ASIGNATURA, INSTRUCTOR, REGISTRO, FICHA, PROGRAMA --




CREATE VIEW Vista_Clase AS
SELECT 
    c.id AS id_clase,
    a.nombre AS asignatura,
    a.intensidad_horaria,
    r.nombre_completo AS instructor,
    f.numero_ficha,
    f.jornada,
    p.nombre AS programa
FROM Clase c
INNER JOIN Asignatura a ON c.idAsignatura = a.id
INNER JOIN Instructor i ON c.idInstructor = i.idregistro
INNER JOIN registro r ON i.idregistro = r.id
INNER JOIN Ficha f ON c.idFicha = f.id
INNER JOIN Programa p ON f.idPrograma = p.id;



------------------------------------------

-- TABLA (HORARIO)  UNION CON CLASE, ASIGNATURA, INSTRUCTOR, REGISTRO, FICHA, PROGRAMA, SALON --

CREATE VIEW Vista_Horario AS
SELECT 
    h.id AS id_horario,
    h.dia,
    h.hora_inicio,
    h.hora_fin,
    a.nombre AS asignatura,
    r.nombre_completo AS instructor,
    f.numero_ficha,
    f.jornada,
    p.nombre AS programa,
    s.numero_salon AS salon
FROM Horario h
INNER JOIN Clase c ON h.idClase = c.id
INNER JOIN Asignatura a ON c.idAsignatura = a.id
INNER JOIN Instructor i ON c.idInstructor = i.idregistro
INNER JOIN registro r ON i.idregistro = r.id
INNER JOIN Ficha f ON c.idFicha = f.id
INNER JOIN Programa p ON f.idPrograma = p.id
INNER JOIN Salon s ON h.idSalon = s.id;


