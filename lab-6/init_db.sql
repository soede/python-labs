-- Удаляем таблицы, если они уже существуют (для повторного запуска)
DROP TABLE IF EXISTS ProgramPlatform;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Platforms;
DROP TABLE IF EXISTS Developers;

-- Таблица разработчиков
CREATE TABLE Developers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            country TEXT
);

-- Таблица платформ
CREATE TABLE Platforms (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           os_name TEXT NOT NULL
);

-- Таблица программ
CREATE TABLE Programs (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          version TEXT NOT NULL,
                          license_type TEXT NOT NULL,
                          developer_id INTEGER,
                          FOREIGN KEY (developer_id) REFERENCES Developers(id)
);

-- Таблица связи программ с платформами (многие ко многим)
CREATE TABLE ProgramPlatform (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 program_id INTEGER NOT NULL,
                                 platform_id INTEGER NOT NULL,
                                 FOREIGN KEY (program_id) REFERENCES Programs(id),
                                 FOREIGN KEY (platform_id) REFERENCES Platforms(id)
);

-- Заполнение таблицы Developers
INSERT INTO Developers (name, country) VALUES
                                           ('JetBrains', 'Russia'),
                                           ('Microsoft', 'USA'),
                                           ('Mozilla Foundation', 'USA');

-- Заполнение таблицы Platforms
INSERT INTO Platforms (os_name) VALUES
                                    ('Windows'),
                                    ('Linux'),
                                    ('macOS');

-- Заполнение таблицы Programs
INSERT INTO Programs (name, version, license_type, developer_id) VALUES
                                                                     ('PyCharm', '2023.1', 'Proprietary', 1),
                                                                     ('Visual Studio Code', '1.78', 'Freeware', 2),
                                                                     ('Firefox', '124.0', 'Open Source', 3);

-- Заполнение таблицы ProgramPlatform
INSERT INTO ProgramPlatform (program_id, platform_id) VALUES
                                                          (1, 1), -- PyCharm на Windows
                                                          (1, 2), -- PyCharm на Linux
                                                          (1, 3), -- PyCharm на macOS
                                                          (2, 1), -- VS Code на Windows
                                                          (2, 2), -- VS Code на Linux
                                                          (2, 3), -- VS Code на macOS
                                                          (3, 1), -- Firefox на Windows
                                                          (3, 2), -- Firefox на Linux
                                                          (3, 3); -- Firefox на macOS
