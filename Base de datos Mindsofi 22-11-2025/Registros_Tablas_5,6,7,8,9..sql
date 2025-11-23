-- TABLA PROGRAMA --

-- TIC - Tecnólogos
INSERT INTO programa (nombre, nivel, duracion, etapa, idespecialidad) VALUES
('Análisis y Desarrollo de Software', 'Tecnólogo', "24 meses", 'Lectiva', 1),
('Análisis y Desarrollo de Software', 'Tecnólogo', "24 meses", 'Productiva', 2),
('Animación 3D', 'Tecnólogo', "24 meses", 'Lectiva', 3),
('Animación 3D', 'Tecnólogo', "24 meses", 'Productiva', 4),
('Desarrollo de Medios Gráficos Visuales', 'Tecnólogo', "24 meses", 'Lectiva', 5),
('Desarrollo de Medios Gráficos Visuales', 'Tecnólogo', "24 meses", 'Productiva', 6),
('Desarrollo Multimedia y Web', 'Tecnólogo', "24 meses", 'Lectiva', 7),
('Desarrollo Multimedia y Web', 'Tecnólogo', "24 meses", 'Productiva', 8);

-- TIC - Técnicos
INSERT INTO programa (nombre, nivel, duracion, etapa, idespecialidad) VALUES
('Programación de Software', 'Técnico', "15 meses", 'Lectiva', 1),
('Programación de Software', 'Técnico', "15 meses", 'Productiva', 2),
('Sistemas', 'Técnico', "15 meses", 'Lectiva', 3),
('Sistemas', 'Técnico', "15 meses", 'Productiva', 4),
('Programación de Aplicaciones para Dispositivos Móviles', 'Técnico', "15 meses", 'Lectiva', 5),
('Programación de Aplicaciones para Dispositivos Móviles', 'Técnico', "15 meses", 'Productiva', 6),
('Programación de Aplicaciones y Servicios para la Nube', 'Técnico', "15 meses", 'Lectiva', 10),
('Programación de Aplicaciones y Servicios para la Nube', 'Técnico', "15 meses", 'Productiva', 9);



-------------------------------




-- TABLA FICHA --

INSERT INTO Ficha (numero_ficha, jornada) VALUES
('100001', 'Diurna'),
('100002', 'Nocturna'),
('100003', 'Mixta'),
('100004', 'Diurna'),
('100005', 'Nocturna'),
('100006', 'Mixta'),
('100007', 'Diurna'),
('100008', 'Nocturna'),
('100009', 'Mixta'),
('100010', 'Diurna');



------------------------------



-- TABLE programa_Ficha


INSERT INTO programaFicha (idFicha, idprograma) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


---------------------------




INSERT INTO instructor_especialidad (idregistroRol, idespecialidad) VALUES
(1, 1),  
(2, 1),  
(2, 3),  
(3, 2),  
(4, 4), 
(5, 5),  
(6, 6), 
(7, 7),  
(8, 8),  
(1, 3);  


------------------------------------




-- TABLE ASIGNATURA --

insert into Asignatura (nombre, intensidad_horaria) values
('Matemáticas', '4 horas'),                                
('Modelado 3D', '4 horas '),                               
('Diseño Gráfico Digital', '4 horas '),                   
('Desarrollo Web Frontend', '4 horas '),                   
('Lógica de Programación', '4 horas '),                    
('Fundamentos de Sistemas Operativos', '4 horas '),       
('Programación de Aplicaciones Móviles', '4 horas '),      
('Computación en la Nube', '4 horas '),                   
('Fundamentos de Gestión Empresarial', '4 horas '),       
('Logística de Abastecimiento', '4 horas ');

