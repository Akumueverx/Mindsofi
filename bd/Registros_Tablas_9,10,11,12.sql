-- TABLE especialidad_ASIGNATURA --

insert into especialidadAsignatura (idespecialidad, idAsignatura) values
(1, 1), -- Instructor 1 dicta Matemáticas
(2, 2), -- Instructor 2 dicta Modelado 3D
(3, 3), -- Instructor 3 dicta Diseño Gráfico Digital
(4, 4), -- Instructor 4 dicta Desarrollo Web Frontend
(5, 5), -- Instructor 5 dicta Lógica de Programación
(6, 6), -- Instructor 6 dicta Fundamentos de Sistemas Operativos
(7, 7), -- Instructor 7 dicta Programación de Aplicaciones Móviles
(8, 8), -- Instructor 8 dicta Computación en la Nube
(9, 9), -- Instructor 9 dicta Fundamentos de Gestión Empresarial
(10, 10); -- Instructor 10 dicta Logística de Abastecimiento



--------------------------------



-- TABLE CLASE --

insert into Clase (idAsignatura, idespecialidad, idFicha) values
(1, 1, 1), -- Matemáticas con Instructor 1 para ficha 12345
(2, 2, 2), -- Modelado 3D con Instructor 2 para ficha 12345
(3, 3, 3), -- Diseño Gráfico Digital con Instructor 3 para ficha 23456
(4, 4, 4), -- Desarrollo Web Frontend con Instructor 4 para ficha 23456
(5, 5, 5), -- Lógica de Programación con Instructor 5 para ficha 34567
(6, 6, 6), -- Sistemas Operativos con Instructor 6 para ficha 34567
(7, 7, 7), -- Apps Móviles con Instructor 7 para ficha 12345
(8, 8, 8), -- Computación en la Nube con Instructor 8 para ficha 23456
(9, 9, 9), -- Gestión Empresarial con Instructor 9 para ficha 34567
(10, 10, 10); -- Logística de Abastecimiento con Instructor 10 para ficha 12345


--------------------------------


-- TABLE SALON --

insert into Salon (numero_salon, ubicacion, capacidad) values
('101', 'Edificio A - Piso 1', 30),
('102', 'Edificio A - Piso 1', 35),
('201', 'Edificio A - Piso 2', 40),
('202', 'Edificio A - Piso 2', 25),
('301', 'Edificio B - Piso 3', 20),
('302', 'Edificio B - Piso 3', 45),
('304', 'Edificio C - Piso 4', 33),
('307', 'Edificio C - Piso 4', 30),
('204', 'Edificio D - Piso 5', 20),
('103', 'Edificio D - Piso 5', 25);


------------------------------


-- TABLE HORARIO --

INSERT INTO Horario (dia, hora_inicio, hora_fin, idclase, idsalon) VALUES
('Lunes', '06:00:00', '10:00:00', 1, 1),        
('Lunes', '10:00:00', '14:00:00', 2, 2),        
('Martes', '06:00:00', '10:00:00', 3, 3),      
('Martes', '14:00:00', '18:00:00', 4, 4),       
('Miércoles', '08:00:00', '12:00:00', 5, 5),    
('Miércoles', '14:00:00', '18:00:00', 6, 6),    
('Jueves', '08:00:00', '12:00:00', 7, 7),       
('Jueves', '14:00:00', '18:00:00', 8, 8),       
('Viernes', '08:00:00', '12:00:00', 9, 9),      
('Viernes', '14:00:00', '18:00:00', 10, 10);    

