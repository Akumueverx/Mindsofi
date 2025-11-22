-- TABLA REGISTRO --

insert into registro (username, contraseña, correo, telefono, nombre_completo) values
('chico_sena', '123456', 'sena.edu@gmail.com', '12384904', 'Mario Gonzalez'),
('ana_dev', 'abc123', 'ana.dev@sena.edu', '3001234567', 'Ana Martínez'),
('juan_prog', 'qwerty', 'juan.prog@sena.edu', '3109876543', 'Juan Pérez'),
('luis_soft', 'pass2025', 'luis.soft@sena.edu', '3154567890', 'Luis Ramírez'),
('caro_design', 'design23', 'caro.design@sena.edu', '3205551234', 'Carolina López'),
('maria_web', 'webdev', 'maria.web@sena.edu', '3016789123', 'María Rodríguez'),
('pedro_data', 'data2025', 'pedro.data@sena.edu', '3024567891', 'Pedro Sánchez'),
('sofia_uiux', 'uxui2025', 'sofia.uiux@sena.edu', '3112345678', 'Sofía Morales'),
('jose_mobile', 'mobile23', 'jose.mobile@sena.edu', '3002223344', 'José Herrera'),
('lucia_cloud', 'cloud2025', 'lucia.cloud@sena.edu', '3139876543', 'Lucía Fernández'),
('andres_admin', 'admin25', 'andres.admin@sena.edu', '3147894561', 'Andrés Torres'),
('valentina_log', 'logi2025', 'valentina.log@sena.edu', '3156547890', 'Valentina Gómez'),
('camilo_fin', 'fin2025', 'camilo.fin@sena.edu', '3171239876', 'Camilo Vargas'),
('diana_ind', 'ind2025', 'diana.ind@sena.edu', '3162224455', 'Diana Castillo'),
('sebastian_sis', 'sis2025', 'sebastian.sis@sena.edu', '3183335566', 'Sebastián Rojas'),
('paula_asist', 'asist25', 'paula.asist@sena.edu', '3194446677', 'Paula Mendoza');


------------------------------



-- TABLA ROL --

INSERT INTO Rol (nombre_rol, descripcion) VALUES
('Administrativo', 'Personal encargado de la gestión administrativa, manejo de fichas, registros y procesos institucionales'),
('Instructor', 'Docente responsable de impartir formación técnica y tecnológica a los aprendices'),
('Aprendiz', 'Estudiante inscrito en los programas de formación técnica y tecnológica');





-----------------------------

-- TABLE REGISTRO_ROL --


insert into registroRol (idregistro, idRol) values
(1, 1),
(2, 1), 
(3, 1), 
(4, 1), 
(5, 1), 
(6, 2), 
(7, 2), 
(8, 2), 
(9, 2), 
(10, 3);



--------------------------


-- TABLA especialidad --

INSERT INTO especialidad (nombre_especialidad) VALUES
('Análisis y Desarrollo de Software'),
('Programación de Software'),
('Animación 3D'),
('Desarrollo de Medios Gráficos Visuales'),
('Desarrollo Multimedia y Web'),
('Sistemas'),
('Programación de Aplicaciones Móviles'),
('Programación de Aplicaciones para la Nube'),
('Bases de Datos y Análisis de Sistemas'),
('Desarrollo Web Frontend');

