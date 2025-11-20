-- ============================================
-- 1️⃣ Create Tables
-- ============================================

-- ------------------------------
-- Table: Students
-- ------------------------------
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    registration_date DATE DEFAULT CURRENT_DATE
);

-- ------------------------------
-- Table: Courses
-- ------------------------------
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE
);

-- ------------------------------
-- Table: Enrollments
-- ------------------------------
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    UNIQUE(student_id, course_id)
);

-- ============================================
-- 2️⃣ Insert Sample Data
-- ============================================

-- Insert students
INSERT INTO Students (first_name, last_name, email) VALUES
('Alice', 'Johnson', 'alice@example.com'),
('Bob', 'Smith', 'bob@example.com'),
('Charlie', 'Brown', 'charlie@example.com');

-- Insert courses
INSERT INTO Courses (course_name, description, start_date, end_date) VALUES
('Python Programming', 'Learn Python from scratch', '2025-12-01', '2026-01-15'),
('Data Science', 'Introduction to Data Science', '2025-12-05', '2026-02-01');

-- Insert enrollments
INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1),  -- Alice in Python Programming
(2, 1),  -- Bob in Python Programming
(3, 2);  -- Charlie in Data Science

-- ============================================
-- 3️⃣ Enroll a Student in a Course
-- ============================================

-- Example: Enroll Alice (student_id=1) in Data Science (course_id=2)
INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 2);

-- ============================================
-- 4️⃣ Queries
-- ============================================

-- a) List students in a specific course (Python Programming, course_id=1)
SELECT s.student_id, s.first_name, s.last_name, s.email
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 1;

-- b) Count total enrollments per course
SELECT c.course_id, c.course_name, COUNT(e.student_id) AS total_enrollments
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- c) List all courses a student is enrolled in (Alice, student_id=1)
SELECT c.course_id, c.course_name, c.start_date, c.end_date
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
WHERE e.student_id = 1;

-- ============================================
-- 5️⃣ Test Cases
-- ============================================

-- Check students in Python Programming
SELECT s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 1;

-- Check students in Data Science
SELECT s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 2;

-- Count enrollments per course
SELECT c.course_name, COUNT(e.student_id) AS total_enrollments
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;
