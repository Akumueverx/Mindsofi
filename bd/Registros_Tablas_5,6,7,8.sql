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



-- TABLE REGISTRO_FICHA


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


-- TABLA especialidad --

INSERT INTO especialidad (programaFicha_id, especialidad) VALUES
(1, 'Análisis y Desarrollo de Software'),
(2, 'Programación de Software'),
(3, 'Animación 3D'),
(4, 'Desarrollo de Medios Gráficos Visuales'),
(5, 'Desarrollo Multimedia y Web'),
(6, 'Sistemas'),
(7, 'Programación de Aplicaciones Móviles'),
(8, 'Programación de Aplicaciones para la Nube'),
(9, 'Bases de Datos y Análisis de Sistemas'),
(10, 'Desarrollo Web Frontend');


------------------------------


-- TABLE ASIGNATURA --

insert into Asignatura (nombre, intensidad_horaria) values
('Matemáticas', '4 horas'),                                -- Para Análisis y Desarrollo de Software
('Modelado 3D', '4 horas '),                               -- Para Animación 3D
('Diseño Gráfico Digital', '4 horas '),                    -- Para Desarrollo de Medios Gráficos Visuales
('Desarrollo Web Frontend', '4 horas '),                   -- Para Desarrollo Multimedia y Web
('Lógica de Programación', '4 horas '),                    -- Para Programación de Software
('Fundamentos de Sistemas Operativos', '4 horas '),        -- Para Sistemas
('Programación de Aplicaciones Móviles', '4 horas '),      -- Para Programación de Aplicaciones Móviles
('Computación en la Nube', '4 horas '),                    -- Para Programación en la Nube
('Fundamentos de Gestión Empresarial', '4 horas '),        -- Para Gestión Empresarial
('Logística de Abastecimiento', '4 horas ');               -- Para Gestión Logística

