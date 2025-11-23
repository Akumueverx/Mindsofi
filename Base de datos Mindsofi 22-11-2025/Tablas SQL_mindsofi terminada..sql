create database mindsofi;
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




--------------------------------

-- Roles
create table Rol (
    id int auto_increment primary key,
    nombre_rol varchar(50) not null,
    descripcion varchar(200)
);




-----------------------------------------------------

create table registroRol (
	id int auto_increment primary key,
    idregistro int not null,
    idRol int not null ,
    foreign key (idregistro) references registro(id),
    foreign key (idRol) references Rol(id)
);





---------------------------------



CREATE TABLE especialidad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_especialidad VARCHAR(100) NOT NULL UNIQUE
    );
    
    
----------------------------------


-- Programa
CREATE TABLE Programa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    duracion varchar(20) NOT NULL,
    etapa VARCHAR(20) NOT NULL,
    idespecialidad INT NOT NULL,  
    FOREIGN KEY (idespecialidad) REFERENCES especialidad(id)
);



   
---------------------------------



-- Ficha
CREATE TABLE Ficha (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_ficha int NOT NULL unique,
    jornada VARCHAR(10) NOT NULL,
    CHECK (numero_ficha REGEXP '^[0-9]{6}$'),
    CHECK (jornada IN ('Diurna','Nocturna','Mixta'))

);







---------------------------------


create table programaFicha (
	id int auto_increment primary key,
    idprograma int not null,
    idFicha int not null,
    foreign key (idprograma) references programa(id),
    foreign key (idFicha) references Ficha(id)
);


-----------------------------------
    
    


-- Especialidad del instructor--

CREATE TABLE instructor_especialidad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idregistroRol INT NOT NULL,  
    idespecialidad INT NOT NULL,
    FOREIGN KEY (idregistroRol) REFERENCES registroRol(id),
    FOREIGN KEY (idespecialidad) REFERENCES especialidad(id)
);





---------------------------------


-- Asignatura --

create table Asignatura (
    id int auto_increment primary key,
    nombre varchar(100) not null,
    intensidad_horaria varchar(50) not null

);




---------------------------------


-- Relación N:M entre especialidad y Asignatura

create table especialidadAsignatura (
	id int auto_increment primary key,
    idespecialidad int not null,
    idAsignatura int not null,
    foreign key (idespecialidad) references instructor_especialidad(id),
    foreign key (idAsignatura) references Asignatura(id)
);






---------------------------------


-- Salón
create table Salon (
    id int auto_increment primary key,
    numero_salon varchar(20) not null unique,
    ubicacion varchar(50),
    capacidad int
);



---------------------------------------


-- Clase con relacion al Salón

CREATE TABLE Clase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idAsignatura INT NOT NULL,
    idinstructor_especialidad INT NOT NULL,
    idFicha INT NOT NULL,
    idSalon INT, 
    FOREIGN KEY (idAsignatura) REFERENCES Asignatura(id),
    FOREIGN KEY (idinstructor_especialidad) REFERENCES instructor_especialidad(id),
    FOREIGN KEY (idFicha) REFERENCES Ficha(id),
    FOREIGN KEY (idSalon) REFERENCES Salon(id)
);


---------------------------------

-- Horario (cada clase se dicta en un salón)

CREATE TABLE Horario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dia VARCHAR(20) NOT NULL, 
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    idclase INT NOT NULL,
    idSalon INT NOT NULL,
    CHECK (dia IN ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')),
    FOREIGN KEY (idclase) REFERENCES Clase(id),
    FOREIGN KEY (idSalon) REFERENCES Salon(id)
);