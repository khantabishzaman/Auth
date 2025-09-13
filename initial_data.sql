INSERT INTO employees (employee_id, full_name, email, hashed_password, dob, department, role) VALUES
('ADMIN001', 'Dr. Anjali Sharma', 'anjali.sharma@example.com', '$2b$12$Ea.8z2JzV/y5.0a3hQ9a.O0gQ9u.K.6cZ8lJd2n.2sB/8p2b3b7eC', '1975-05-20', 'Administration', 'admin'),
('MENTOR001', 'Prof. Vikram Singh', 'vikram.singh@example.com', '$2b$12$aB.Cd4E.fG6hH.iJ9kL0l.uM.nO7pQ8rS.tU6vW5xY4zZ2a1b3c4d', '1982-11-15', 'Computer Science', 'mentor'),
('MENTOR002', 'Dr. Priya Mehta', 'priya.mehta@example.com', '$2b$12$xY.z1A2b3C.d4E5f6G.h7i.jK8lM9nO0pQ.rS.tU.vW.xY.z1A2b3', '1985-02-10', 'Mechanical Engineering', 'mentor');

INSERT INTO students (enrollment_number, full_name, mentor_id) VALUES
('E23CS001', 'Rohan Kumar', 'MENTOR001'),
('E23CS002', 'Sneha Gupta', 'MENTOR001'),
('E23CS003', 'Amit Patel', 'MENTOR001'),
('E23ME001', 'Aditi Rao', 'MENTOR002'),
('E23ME002', 'Karan Verma', 'MENTOR002');

INSERT INTO sections (course_name, course_code) VALUES
('Data Structures', 'CS201'),
('Thermodynamics', 'ME201'),
('Algorithms', 'CS301');

INSERT INTO mentor_section_assignments (mentor_id, section_id) VALUES
('MENTOR001', 1),
('MENTOR001', 3),
('MENTOR002', 2);
