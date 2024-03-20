DROP TABLE IF EXISTS students;

CREATE TABLE students (
	student_id serial primary key,
	first_name text NOT NULL,
	last_name text NOT NULL,
	email text NOT NULL UNIQUE,
	enrollment_date date
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

select * from students;
