use mindsofi;



-- registrarse (entidad general: aprendices, instructores, personal)
create table registro (
    id int auto_increment primary key,
    username varchar(50) unique not null,
    contraseña varchar(100) not null,
    correo varchar(100),
    telefono varchar(20),
    nombre_completo varchar(100) not null
);


-- Roles
create table Rol (
    id int auto_increment primary key,
    nombre_rol varchar(50) not null,
    descripcion varchar(200),
    id_registro int,
    foreign key (id_registro) references registro(id)
);


create table registroRol (
	id int auto_increment primary key,
    idregistro int not null,
    idRol int not null ,
    foreign key (idregistro) references registro(id),
    foreign key (idRol) references Rol(id)
);


-- Programa
CREATE TABLE Programa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    duracion varchar(20) NOT NULL,
    etapa VARCHAR(20) NOT NULL,
    registroRol_id int, 
    foreign key (registroRol_id) references registroRol(id)
);



-- Ficha
CREATE TABLE Ficha (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_ficha int NOT NULL unique,
    jornada VARCHAR(10) NOT NULL,
    idPrograma INT,
    CHECK (numero_ficha REGEXP '^[0-9]{6}$'),
    CHECK (jornada IN ('Diurna','Nocturna','Mixta')),
    FOREIGN KEY (idPrograma) REFERENCES Programa(id)
);






create table programaFicha (
	id int auto_increment primary key,
    idprograma int not null,
    idFicha int not null,
    foreign key (idprograma) references programa(id),
    foreign key (idFicha) references Ficha(id)
);





-- Instructor (solo atributos específicos de instructores)
create table Instructor (
	id int auto_increment primary key ,
    especialidad varchar(100) not null,
    programaFicha_id int,
    foreign key (programaFicha_id) references programaFicha(id)
);





-- Asignatura
create table Asignatura (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    intensidad_horaria varchar(50) not null,
    Instructor_id int,
    foreign key (Instructor_id) references Instructor(id)
);





-- Relación N:M entre Instructor y Asignatura
create table InstructorAsignatura (
	id int auto_increment primary key,
    idInstructor int not null,
    idAsignatura int not null,
    foreign key (idInstructor) references Instructor(id),
    foreign key (idAsignatura) references Asignatura(id)
);





-- Clase (conecta Asignatura + Instructor + Ficha)
create table Clase (
    id int auto_increment primary key,
    idAsignatura int not null,
    idInstructor int not null,
    idFicha int not null,
    foreign key (idAsignatura) references Asignatura(id),
    foreign key (idInstructor) references Instructor(id),
    foreign key (idFicha) references Ficha(id)
);





-- Salón
create table Salon (
    id int auto_increment primary key,
    numero_salon varchar(20) not null,
    ubicacion varchar(50),
    capacidad int,
    clase_id int, 
    foreign key (clase_id) references clase(id)
    
);





-- Horario (cada clase se dicta en un salón)
create table Horario (
    id int auto_increment primary key,
    dia varchar(20),
    hora_inicio time,
    hora_fin time,
    idSalon int,
    foreign key (idSalon) references Salon(id)
);







