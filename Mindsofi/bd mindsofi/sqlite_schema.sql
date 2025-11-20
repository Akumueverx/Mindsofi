-- Esquema convertido de MySQL a SQLite para Mindsofi

-- registrarse (entidad general: aprendices, instructores, personal)
CREATE TABLE registro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL,
    correo TEXT,
    telefono TEXT,
    nombre_completo TEXT NOT NULL
);

-- Roles
CREATE TABLE Rol (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_rol TEXT NOT NULL,
    descripcion TEXT,
    id_registro INTEGER,
    FOREIGN KEY (id_registro) REFERENCES registro(id)
);

CREATE TABLE registroRol (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idregistro INTEGER NOT NULL,
    idRol INTEGER NOT NULL,
    FOREIGN KEY (idregistro) REFERENCES registro(id),
    FOREIGN KEY (idRol) REFERENCES Rol(id)
);

-- Programa
CREATE TABLE Programa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel TEXT NOT NULL,
    duracion TEXT NOT NULL,
    etapa TEXT NOT NULL,
    registroRol_id INTEGER,
    FOREIGN KEY (registroRol_id) REFERENCES registroRol(id)
);

-- Ficha
CREATE TABLE Ficha (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_ficha INTEGER NOT NULL UNIQUE,
    jornada TEXT NOT NULL,
    idPrograma INTEGER,
    CHECK (jornada IN ('Diurna','Nocturna','Mixta')),
    FOREIGN KEY (idPrograma) REFERENCES Programa(id)
);

CREATE TABLE programaFicha (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idprograma INTEGER NOT NULL,
    idFicha INTEGER NOT NULL,
    FOREIGN KEY (idprograma) REFERENCES Programa(id),
    FOREIGN KEY (idFicha) REFERENCES Ficha(id)
);

-- Instructor (solo atributos específicos de instructores)
CREATE TABLE Instructor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    especialidad TEXT NOT NULL,
    programaFicha_id INTEGER,
    FOREIGN KEY (programaFicha_id) REFERENCES programaFicha(id)
);

-- Asignatura
CREATE TABLE Asignatura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    intensidad_horaria TEXT NOT NULL,
    Instructor_id INTEGER,
    FOREIGN KEY (Instructor_id) REFERENCES Instructor(id)
);

-- Relación N:M entre Instructor y Asignatura
CREATE TABLE InstructorAsignatura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idInstructor INTEGER NOT NULL,
    idAsignatura INTEGER NOT NULL,
    FOREIGN KEY (idInstructor) REFERENCES Instructor(id),
    FOREIGN KEY (idAsignatura) REFERENCES Asignatura(id)
);

-- Clase (conecta Asignatura + Instructor + Ficha)
CREATE TABLE Clase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAsignatura INTEGER NOT NULL,
    idInstructor INTEGER NOT NULL,
    idFicha INTEGER NOT NULL,
    FOREIGN KEY (idAsignatura) REFERENCES Asignatura(id),
    FOREIGN KEY (idInstructor) REFERENCES Instructor(id),
    FOREIGN KEY (idFicha) REFERENCES Ficha(id)
);

-- Salón
CREATE TABLE Salon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_salon TEXT NOT NULL,
    ubicacion TEXT,
    capacidad INTEGER,
    clase_id INTEGER,
    FOREIGN KEY (clase_id) REFERENCES Clase(id)
);

-- Horario (cada clase se dicta en un salón)
CREATE TABLE Horario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dia TEXT,
    hora_inicio TEXT,
    hora_fin TEXT,
    idSalon INTEGER,
    FOREIGN KEY (idSalon) REFERENCES Salon(id)
);
