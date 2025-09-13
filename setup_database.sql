CREATE TYPE user_role AS ENUM ('admin', 'mentor');

CREATE TABLE employees (
    employee_id VARCHAR(100) PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    dob DATE,
    date_joined TIMESTAMPTZ DEFAULT NOW(),
    department VARCHAR(255),
    role user_role NOT NULL
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    enrollment_number VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(255) NOT NULL,
    mentor_id VARCHAR(100) REFERENCES employees(employee_id) ON DELETE SET NULL
);

CREATE TABLE sections (
    section_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_code VARCHAR(50) NOT NULL
);

CREATE TABLE mentor_section_assignments (
    mentor_id VARCHAR(100) REFERENCES employees(employee_id) ON DELETE CASCADE,
    section_id INT REFERENCES sections(section_id) ON DELETE CASCADE,
    PRIMARY KEY (mentor_id, section_id)
);

CREATE INDEX idx_employees_email ON employees(email);
