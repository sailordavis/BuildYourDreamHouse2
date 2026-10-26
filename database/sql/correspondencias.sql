-- PREGUNTA 2 (Ya almacenadas)
/*Tomara en cuenta la eficiencia, superficie y acabado */
/*1. Concreto / Cemento*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) 
VALUES
(2, 'Concreto / cemento', 'superficie', 'Concreto', 2.0),
(2, 'Concreto / cemento', 'eficiencia', 'Alta durabilidad exterior', 1.8),
(2, 'Concreto / cemento', 'acabado', 'Mate', 1.2);

/*2. Ladrillo expuesto*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) 
VALUES
(2, 'Ladrillo expuesto', 'superficie', 'Ladrillo', 2.0),
(2, 'Ladrillo expuesto', 'eficiencia', 'Transpirable / antisalitre', 1.7),
(2, 'Ladrillo expuesto', 'acabado', 'Satinado', 1.3);


/*3. Piedra natural*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(2, 'Piedra natural', 'superficie', 'Piedra', 2.0),
(2, 'Piedra natural', 'eficiencia', 'Resistente a la intemperie', 1.8),
(2, 'Piedra natural', 'acabado', 'Mate', 1.2);

/*4. Madera*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(2, 'Madera', 'superficie', 'Madera', 2.0),
(2, 'Madera', 'eficiencia', 'Proteccion contra humedad', 1.8),
(2, 'Madera', 'acabado', 'Brillante', 1.4);

/*5. Metal*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(2, 'Metal', 'superficie', 'Metal', 2.0),
(2, 'Metal', 'eficiencia', 'Anticorrosiva', 1.9),
(2, 'Metal', 'acabado', 'Brillante', 1.5);

/*6. Cerámica / Porcelanato*/
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(2, 'Ceramica / Porcelanato', 'superficie', 'Ceramica', 2.0),
(2, 'Ceramica / Porcelanato', 'eficiencia', 'Lavable / Resistente humedad', 1.8),
(2, 'Ceramica / Porcelanato', 'acabado', 'Satinado', 1.3);


-- PREGUNTA 3 (Ya alamcenadas)
/*Se tomara en cuenta la eficiencia y acabado*/
-- Sala
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Sala', 'eficiencia', 'Alta cobertura interior', 1.8),
(3, 'Sala', 'acabado', 'Satinado', 1.5);

-- Cocina
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Cocina', 'eficiencia', 'Lavable / Resistente a grasa y humedad', 2.0),
(3, 'Cocina', 'acabado', 'Semibrillante', 1.6);

-- Dormitorio
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Dormitorio', 'eficiencia', 'Alta opacidad / Bajo olor', 1.7),
(3, 'Dormitorio', 'acabado', 'Mate', 1.5);

-- Baño
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Baño', 'eficiencia', 'Resistente a humedad y moho', 2.0),
(3, 'Baño', 'acabado', 'Semibrillante', 1.6);

-- Oficina
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Oficina', 'eficiencia', 'Durabilidad / Limpieza facil', 1.8),
(3, 'Oficina', 'acabado', 'Satinado', 1.4);

-- Pasillo / Entrada
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso)
VALUES
(3, 'Pasillo / Entrada', 'eficiencia', 'Alta resistencia al roce', 1.9),
(3, 'Pasillo / Entrada', 'acabado', 'Semibrillante', 1.5);


-- 🔹 Bloque de correspondencia - Pregunta 20 (Emoción a transmitir) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Tranquilidad / Relajacion
(20, 'Tranquilidad / Relajacion', 'gama_color', 'Fríos', 0.8),
(20, 'Tranquilidad / Relajacion', 'gama_color', 'Neutros', 0.7),
(20, 'Tranquilidad / Relajacion', 'estilo_decorativo', 'Minimalista', 0.6),
(20, 'Tranquilidad / Relajacion', 'estilo_decorativo', 'Nórdico', 0.6),

-- Energia / Vitalidad
(20, 'Energia / Vitalidad', 'gama_color', 'Cálidos', 0.8),
(20, 'Energia / Vitalidad', 'gama_color', 'Tierra', 0.6),
(20, 'Energia / Vitalidad', 'estilo_decorativo', 'Moderno', 0.6),
(20, 'Energia / Vitalidad', 'estilo_decorativo', 'Industrial', 0.5),

-- Calidez / Confort
(20, 'Calidez / Confort', 'gama_color', 'Tierra', 0.8),
(20, 'Calidez / Confort', 'gama_color', 'Cálidos', 0.7),
(20, 'Calidez / Confort', 'estilo_decorativo', 'Rústico', 0.6),
(20, 'Calidez / Confort', 'estilo_decorativo', 'Clásico', 0.5),

-- Creatividad / Inspiracion
(20, 'Creatividad / Inspiracion', 'gama_color', 'Vibrantes', 0.8),
(20, 'Creatividad / Inspiracion', 'gama_color', 'Pasteles', 0.6),
(20, 'Creatividad / Inspiracion', 'estilo_decorativo', 'Ecléctico', 0.7),
(20, 'Creatividad / Inspiracion', 'estilo_decorativo', 'Bohemio', 0.6),

-- Elegancia / Sofisticacion
(20, 'Elegancia / Sofisticacion', 'gama_color', 'Neutros', 0.8),
(20, 'Elegancia / Sofisticacion', 'gama_color', 'Oscuros', 0.7),
(20, 'Elegancia / Sofisticacion', 'estilo_decorativo', 'Clásico', 0.7),
(20, 'Elegancia / Sofisticacion', 'estilo_decorativo', 'Contemporáneo', 0.6),

-- Frescura / Ligereza
(20, 'Frescura / Ligereza', 'gama_color', 'Fríos', 0.8),
(20, 'Frescura / Ligereza', 'gama_color', 'Pasteles', 0.7),
(20, 'Frescura / Ligereza', 'estilo_decorativo', 'Mediterráneo', 0.6),
(20, 'Frescura / Ligereza', 'estilo_decorativo', 'Nórdico', 0.5),

-- Alegria / Optimismo
(20, 'Alegria / Optimismo', 'gama_color', 'Vibrantes', 0.8),
(20, 'Alegria / Optimismo', 'gama_color', 'Cálidos', 0.7),
(20, 'Alegria / Optimismo', 'estilo_decorativo', 'Bohemio', 0.6),
(20, 'Alegria / Optimismo', 'estilo_decorativo', 'Ecléctico', 0.5);


-- 🔹 Bloque de correspondencia - Pregunta 23 (Tipo de estación deseada) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Otoño
(23, 'Otono', 'gama_color', 'Tierra', 0.8),
(23, 'Otono', 'gama_color', 'Cálidos', 0.7),
(23, 'Otono', 'estilo_decorativo', 'Rústico', 0.6),
(23, 'Otono', 'estilo_decorativo', 'Clásico', 0.5),

-- Primavera
(23, 'Primavera', 'gama_color', 'Pasteles', 0.8),
(23, 'Primavera', 'gama_color', 'Vibrantes', 0.7),
(23, 'Primavera', 'estilo_decorativo', 'Bohemio', 0.6),
(23, 'Primavera', 'estilo_decorativo', 'Ecléctico', 0.5),

-- Verano
(23, 'Verano', 'gama_color', 'Cálidos', 0.8),
(23, 'Verano', 'gama_color', 'Fríos', 0.6),
(23, 'Verano', 'estilo_decorativo', 'Mediterráneo', 0.6),
(23, 'Verano', 'estilo_decorativo', 'Moderno', 0.5),

-- Invierno
(23, 'Invierno', 'gama_color', 'Neutros', 0.8),
(23, 'Invierno', 'gama_color', 'Oscuros', 0.7),
(23, 'Invierno', 'estilo_decorativo', 'Minimalista', 0.6),
(23, 'Invierno', 'estilo_decorativo', 'Contemporáneo', 0.5);


-- 🔹 Bloque de correspondencia - Pregunta 24 (Tipo de entorno deseado) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Natural / Orgánico
(24, 'Natural / Organico', 'gama_color', 'Tierra', 0.8),
(24, 'Natural / Organico', 'gama_color', 'Verdes', 0.7),
(24, 'Natural / Organico', 'estilo_decorativo', 'Ecológico', 0.8),
(24, 'Natural / Organico', 'estilo_decorativo', 'Bohemio', 0.6),

-- Moderno / Minimalista
(24, 'Moderno / Minimalista', 'gama_color', 'Neutros', 0.8),
(24, 'Moderno / Minimalista', 'gama_color', 'Fríos', 0.7),
(24, 'Moderno / Minimalista', 'estilo_decorativo', 'Minimalista', 0.9),
(24, 'Moderno / Minimalista', 'estilo_decorativo', 'Contemporáneo', 0.7),

-- Cálido / Acogedor
(24, 'Calido / Acogedor', 'gama_color', 'Cálidos', 0.8),
(24, 'Calido / Acogedor', 'gama_color', 'Tierra', 0.7),
(24, 'Calido / Acogedor', 'estilo_decorativo', 'Clásico', 0.6),
(24, 'Calido / Acogedor', 'estilo_decorativo', 'Rústico', 0.8),

-- Rústico / Tradicional
(24, 'Rustico / Tradicional', 'gama_color', 'Tierra', 0.9),
(24, 'Rustico / Tradicional', 'gama_color', 'Neutros', 0.6),
(24, 'Rustico / Tradicional', 'estilo_decorativo', 'Rústico', 0.9),
(24, 'Rustico / Tradicional', 'estilo_decorativo', 'Clásico', 0.7),

-- Nórdico / Escandinavo
(24, 'Nordico / Escandinavo', 'gama_color', 'Neutros', 0.9),
(24, 'Nordico / Escandinavo', 'gama_color', 'Fríos', 0.7),
(24, 'Nordico / Escandinavo', 'estilo_decorativo', 'Escandinavo', 0.9),
(24, 'Nordico / Escandinavo', 'estilo_decorativo', 'Minimalista', 0.7),

-- Industrial / Urbano
(24, 'Industrial / Urbano', 'gama_color', 'Oscuros', 0.8),
(24, 'Industrial / Urbano', 'gama_color', 'Neutros', 0.6),
(24, 'Industrial / Urbano', 'estilo_decorativo', 'Industrial', 0.9),
(24, 'Industrial / Urbano', 'estilo_decorativo', 'Urbano', 0.8);



-- 🔹 Bloque de correspondencia - Pregunta 25 (Estilo decorativo interior) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Clásico
(25, 'Clasico', 'estilo_decorativo', 'Clásico', 0.9),
(25, 'Clasico', 'gama_color', 'Neutros', 0.7),
(25, 'Clasico', 'gama_color', 'Tierra', 0.6),

-- Vintage
(25, 'Vintage', 'estilo_decorativo', 'Vintage', 0.9),
(25, 'Vintage', 'gama_color', 'Pasteles', 0.8),
(25, 'Vintage', 'gama_color', 'Cálidos', 0.6),

-- Bohemio
(25, 'Bohemio', 'estilo_decorativo', 'Bohemio', 0.9),
(25, 'Bohemio', 'gama_color', 'Vibrantes', 0.8),
(25, 'Bohemio', 'gama_color', 'Tierra', 0.6),

-- Contemporáneo
(25, 'Contemporaneo', 'estilo_decorativo', 'Contemporáneo', 0.9),
(25, 'Contemporaneo', 'gama_color', 'Neutros', 0.8),
(25, 'Contemporaneo', 'gama_color', 'Fríos', 0.6),

-- Mediterráneo
(25, 'Mediterraneo', 'estilo_decorativo', 'Mediterráneo', 0.9),
(25, 'Mediterraneo', 'gama_color', 'Azules', 0.8),
(25, 'Mediterraneo', 'gama_color', 'Blancos', 0.7),

-- Ecléctico
(25, 'Eclectico', 'estilo_decorativo', 'Ecléctico', 0.9),
(25, 'Eclectico', 'gama_color', 'Vibrantes', 0.7),
(25, 'Eclectico', 'gama_color', 'Neutros', 0.6);


-- 🔹 Bloque de correspondencia - Pregunta 21 (Profesión en el espacio de trabajo) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Ejecutivo
(21, 'Ejecutivo', 'estilo_decorativo', 'Moderno', 0.9),
(21, 'Ejecutivo', 'gama_color', 'Neutros', 0.8),

-- Diseñador / artista
(21, 'Disenador / artista', 'estilo_decorativo', 'Bohemio', 0.8),
(21, 'Disenador / artista', 'estilo_decorativo', 'Contemporáneo', 0.7),
(21, 'Disenador / artista', 'gama_color', 'Vibrantes', 0.9),

-- Ingeniero / técnico
(21, 'Ingeniero / tecnico', 'estilo_decorativo', 'Minimalista', 0.9),
(21, 'Ingeniero / tecnico', 'gama_color', 'Fríos', 0.8),

-- Maestro / educativo
(21, 'Maestro / educativo', 'estilo_decorativo', 'Clásico', 0.8),
(21, 'Maestro / educativo', 'gama_color', 'Cálidos', 0.7),

-- Programador / desarrollador / IT
(21, 'Programador / desarrollador / IT', 'estilo_decorativo', 'Contemporáneo', 0.9),
(21, 'Programador / desarrollador / IT', 'gama_color', 'Fríos', 0.8),

-- Salud / médico / terapeuta
(21, 'Salud / medico / terapeuta', 'estilo_decorativo', 'Minimalista', 0.9),
(21, 'Salud / medico / terapeuta', 'gama_color', 'Blancos', 0.9),
(21, 'Salud / medico / terapeuta', 'gama_color', 'Verdes suaves', 0.7),

-- Emprendedor / start-up / coworking
(21, 'Emprendedor / start-up / coworking', 'estilo_decorativo', 'Industrial', 0.8),
(21, 'Emprendedor / start-up / coworking', 'estilo_decorativo', 'Contemporáneo', 0.7),
(21, 'Emprendedor / start-up / coworking', 'gama_color', 'Vibrantes', 0.8),

-- Escritorio personal
(21, 'Escritorio personal', 'estilo_decorativo', 'Ecléctico', 0.9),
(21, 'Escritorio personal', 'gama_color', 'Personalizada', 0.7),

-- Científico
(21, 'Cientifico', 'estilo_decorativo', 'Minimalista', 0.9),
(21, 'Cientifico', 'gama_color', 'Fríos', 0.8),

-- Arquitecto
(21, 'Arquitecto', 'estilo_decorativo', 'Contemporáneo', 0.9),
(21, 'Arquitecto', 'gama_color', 'Neutros', 0.8),

-- Músico
(21, 'Musico', 'estilo_decorativo', 'Bohemio', 0.8),
(21, 'Musico', 'estilo_decorativo', 'Vintage', 0.7),
(21, 'Musico', 'gama_color', 'Cálidos', 0.8);


-- 🔹 Bloque de correspondencia - Pregunta 22 (Hobbies y gustos personales) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Cine
(22, 'Cine', 'estilo_decorativo', 'Vintage', 0.8),
(22, 'Cine', 'gama_color', 'Oscuros', 0.7),

-- Fotografía
(22, 'Fotografia', 'estilo_decorativo', 'Contemporáneo', 0.8),
(22, 'Fotografia', 'gama_color', 'Neutros', 0.7),

-- Viajes / aventura
(22, 'Viajes / aventura', 'estilo_decorativo', 'Bohemio', 0.8),
(22, 'Viajes / aventura', 'gama_color', 'Vibrantes', 0.7),

-- Deporte / fitness
(22, 'Deporte / fitness', 'estilo_decorativo', 'Moderno', 0.8),
(22, 'Deporte / fitness', 'gama_color', 'Cálidos', 0.7),

-- Naturaleza / jardinería
(22, 'Naturaleza / jardineria', 'estilo_decorativo', 'Natural / Orgánico', 0.9),
(22, 'Naturaleza / jardineria', 'gama_color', 'Verdes / Tierra', 0.9),

-- Tecnología / gaming
(22, 'Tecnologia / gaming', 'estilo_decorativo', 'Industrial', 0.8),
(22, 'Tecnologia / gaming', 'gama_color', 'Fríos / Neón', 0.8),

-- Moda / diseño
(22, 'Moda / diseno', 'estilo_decorativo', 'Contemporáneo', 0.8),
(22, 'Moda / diseno', 'gama_color', 'Vibrantes', 0.7),

-- Animales / mascotas
(22, 'Animales / mascotas', 'estilo_decorativo', 'Acogedor', 0.8),
(22, 'Animales / mascotas', 'gama_color', 'Cálidos', 0.7),

-- Meditación / bienestar
(22, 'Meditacion / bienestar', 'estilo_decorativo', 'Zen / Asiático', 0.9),
(22, 'Meditacion / bienestar', 'gama_color', 'Suaves / Neutros', 0.9),

-- Coleccionismo / nostalgia
(22, 'Coleccionismo / nostalgia', 'estilo_decorativo', 'Vintage', 0.9),
(22, 'Coleccionismo / nostalgia', 'gama_color', 'Oscuros / Cálidos', 0.8),

-- Automóviles / mecánica
(22, 'Automoviles / mecanica', 'estilo_decorativo', 'Industrial', 0.9),
(22, 'Automoviles / mecanica', 'gama_color', 'Metálicos / Neutros', 0.8);


-- 🔹 Bloque de correspondencia - Pregunta 30 (Armonía con el entorno natural) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Rústico natural
(30, 'Rustico natural', 'estilo_decorativo', 'Rustico / Tradicional', 0.9),
(30, 'Rustico natural', 'gama_color', 'Tierra / Naturales', 0.8),

-- Mediterráneo
(30, 'Mediterraneo', 'estilo_decorativo', 'Mediterraneo', 0.9),
(30, 'Mediterraneo', 'gama_color', 'Cálidos / Neutros', 0.8),

-- Tropical
(30, 'Tropical', 'estilo_decorativo', 'Tropical / Bohemio', 0.9),
(30, 'Tropical', 'gama_color', 'Vibrantes / Cálidos', 0.8),

-- Zen / Asiático
(30, 'Zen / Asiatico', 'estilo_decorativo', 'Zen / Asiático', 0.9),
(30, 'Zen / Asiatico', 'gama_color', 'Suaves / Neutros', 0.8),

-- Bohemio natural
(30, 'Bohemio natural', 'estilo_decorativo', 'Bohemio', 0.9),
(30, 'Bohemio natural', 'gama_color', 'Vibrantes / Naturales', 0.8),

-- Ecológico
(30, 'Ecologico', 'estilo_decorativo', 'Natural / Orgánico', 0.9),
(30, 'Ecologico', 'gama_color', 'Verdes / Tierra', 0.9);


-- 🔹 Bloque de correspondencia - Pregunta 31 (Estilo arquitectónico) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Moderno
(31, 'Moderno', 'estilo_decorativo', 'Moderno / Minimalista', 0.9),
(31, 'Moderno', 'gama_color', 'Neutros / Fríos', 0.8),

-- Contemporáneo
(31, 'Contemporaneo', 'estilo_decorativo', 'Contemporaneo', 0.9),
(31, 'Contemporaneo', 'gama_color', 'Neutros / Cálidos', 0.8),

-- Minimalista
(31, 'Minimalista', 'estilo_decorativo', 'Minimalista', 0.9),
(31, 'Minimalista', 'gama_color', 'Blancos / Grises', 0.9),

-- Industrial
(31, 'Industrial', 'estilo_decorativo', 'Industrial / Urbano', 0.9),
(31, 'Industrial', 'gama_color', 'Grises / Oscuros', 0.8),

-- Clásico
(31, 'Clasico', 'estilo_decorativo', 'Clasico', 0.9),
(31, 'Clasico', 'gama_color', 'Cálidos / Neutros', 0.8),

-- Colonial
(31, 'Colonial', 'estilo_decorativo', 'Colonial', 0.9),
(31, 'Colonial', 'gama_color', 'Madera / Tierra', 0.8),

-- Urbano / Ciudad
(31, 'Urbano / Ciudad', 'estilo_decorativo', 'Urbano / Contemporaneo', 0.9),
(31, 'Urbano / Ciudad', 'gama_color', 'Grises / Neutros', 0.8),

-- Vintage / Retro
(31, 'Vintage / Retro', 'estilo_decorativo', 'Vintage / Retro', 0.9),
(31, 'Vintage / Retro', 'gama_color', 'Cálidos / Pasteles', 0.8),

-- Ecléctico
(31, 'Eclectico', 'estilo_decorativo', 'Eclectico', 0.9),
(31, 'Eclectico', 'gama_color', 'Combinados / Vibrantes', 0.8);

-- 🔹 Bloque de correspondencia - Pregunta 32 (Estilo estacional) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Primavera
(32, 'Primavera', 'gama_color', 'Colores claros / Pasteles', 0.9),
(32, 'Primavera', 'estilo_decorativo', 'Fresco / Ligero', 0.8),

-- Verano
(32, 'Verano', 'gama_color', 'Colores vivos / Brillantes', 0.9),
(32, 'Verano', 'estilo_decorativo', 'Vibrante / Alegre', 0.8),

-- Otoño
(32, 'Otono', 'gama_color', 'Tonos cálidos / Tierra', 0.9),
(32, 'Otono', 'estilo_decorativo', 'Acogedor / Confortable', 0.8),

-- Invierno
(32, 'Invierno', 'gama_color', 'Colores fríos / Neutros', 0.9),
(32, 'Invierno', 'estilo_decorativo', 'Elegante / Sobrio', 0.8);


-- 🔹 Bloque de correspondencia - Pregunta 33 (Espacio exterior) (Ya almacenadas)
INSERT INTO Correspondencias (pregunta_id, opcion_value, atributo_objetivo, valor_relacionado, peso) VALUES
-- Colores vivos / llamativos
(33, 'Colores vivos / llamativos', 'gama_color', 'Colores brillantes / Vivos', 0.9),
(33, 'Colores vivos / llamativos', 'estilo_decorativo', 'Vibrante / Llamativo', 0.8),

-- Contrastes marcados
(33, 'Contrastes marcados', 'gama_color', 'Combinaciones contrastantes', 0.9),
(33, 'Contrastes marcados', 'estilo_decorativo', 'Moderno / Impactante', 0.8),

-- Tonos elegantes / sobrios
(33, 'Tonos elegantes / sobrios', 'gama_color', 'Neutros / Oscuros', 0.9),
(33, 'Tonos elegantes / sobrios', 'estilo_decorativo', 'Elegante / Sofisticado', 0.8),

-- Detalles decorativos destacados
(33, 'Detalles decorativos destacados', 'gama_color', 'Colores destacados / Complementarios', 0.9),
(33, 'Detalles decorativos destacados', 'estilo_decorativo', 'Decorativo / Ornamental', 0.8);