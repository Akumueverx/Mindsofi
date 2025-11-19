-- TABLA PROGRAMA --

-- TIC - Tecnólogos
INSERT INTO programa (nombre, nivel, duracion, etapa) VALUES
('Análisis y Desarrollo de Software', 'Tecnólogo', "24 meses", 'Lectiva'),
('Análisis y Desarrollo de Software', 'Tecnólogo', "24 meses", 'Productiva'),
('Animación 3D', 'Tecnólogo', "24 meses", 'Lectiva'),
('Animación 3D', 'Tecnólogo', "24 meses", 'Productiva'),
('Desarrollo de Medios Gráficos Visuales', 'Tecnólogo', "24 meses", 'Lectiva'),
('Desarrollo de Medios Gráficos Visuales', 'Tecnólogo', "24 meses", 'Productiva'),
('Desarrollo Multimedia y Web', 'Tecnólogo', "24 meses", 'Lectiva'),
('Desarrollo Multimedia y Web', 'Tecnólogo', "24 meses", 'Productiva');

-- TIC - Técnicos
INSERT INTO programa (nombre, nivel, duracion, etapa) VALUES
('Programación de Software', 'Técnico', "15 meses", 'Lectiva'),
('Programación de Software', 'Técnico', "15 meses", 'Productiva'),
('Sistemas', 'Técnico', "15 meses", 'Lectiva'),
('Sistemas', 'Técnico', "15 meses", 'Productiva'),
('Programación de Aplicaciones para Dispositivos Móviles', 'Técnico', "15 meses", 'Lectiva'),
('Programación de Aplicaciones para Dispositivos Móviles', 'Técnico', "15 meses", 'Productiva'),
('Programación de Aplicaciones y Servicios para la Nube', 'Técnico', "15 meses", 'Lectiva'),
('Programación de Aplicaciones y Servicios para la Nube', 'Técnico', "15 meses", 'Productiva');





----------------------------------------------------------------------


-- TABLA FICHA --

INSERT INTO Ficha (numero_ficha, jornada, idPrograma) VALUES
('100001', 'Diurna', 1),
('100002', 'Nocturna', 2),
('100003', 'Mixta', 3),
('100004', 'Diurna', 4),
('100005', 'Nocturna', 5),
('100006', 'Mixta', 6),
('100007', 'Diurna', 7),
('100008', 'Nocturna', 8),
('100009', 'Mixta', 9),
('100010', 'Diurna', 10);




---------------------------------

-- TABLA ROL --

INSERT INTO Rol (nombre_rol, descripcion) VALUES
('Administrativo', 'Personal encargado de la gestión administrativa, manejo de fichas, registros y procesos institucionales'),
('Instructor', 'Docente responsable de impartir formación técnica y tecnológica a los aprendices'),
('Aprendiz', 'Estudiante inscrito en los programas de formación técnica y tecnológica');


----------------------------------

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





