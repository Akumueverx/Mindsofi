-- TABLE especialidad_ASIGNATURA --

insert into especialidadAsignatura (idespecialidad, idAsignatura) values
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

------------------------------------


-- TABLE CLASE --

INSERT INTO Clase (idAsignatura, idinstructor_especialidad, idFicha, idSalon) VALUES
(1, 1, 1, 1),   
(2, 2, 1, 4),   
(3, 1, 2, 2),  
(1, 3, 2, 1),   
(4, 3, 3, 3),   
(2, 2, 3, 4),   
(5, 4, 4, 2), 
(3, 1, 4, 2),   
(1, 5, 1, 3), 
(4, 3, 4, 1); 



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

