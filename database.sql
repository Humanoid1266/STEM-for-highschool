--Tài liệu công khai
CREATE TABLE public_resources (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL, -- Tiêu đề tài liệu
    description NVARCHAR(MAX), -- Mô tả tài liệu
    link NVARCHAR(255) NOT NULL, -- Đường dẫn tài liệu
    created_at DATETIME DEFAULT GETDATE() -- Ngày thêm tài liệu
);

--Sự kiện
CREATE TABLE events (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL, -- Tên sự kiện
    description NVARCHAR(MAX), -- Mô tả sự kiện
    event_date DATE NOT NULL, -- Ngày tổ chức
    location NVARCHAR(255), -- Địa điểm
    created_at DATETIME DEFAULT GETDATE() -- Ngày tạo
);

--đăng kí nhận thông tin
CREATE TABLE subscriptions (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(100) NOT NULL UNIQUE, -- Email người đăng ký
    registered_at DATETIME DEFAULT GETDATE() -- Ngày đăng ký
);

--Học sinh
CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL, 
    email NVARCHAR(100) NOT NULL UNIQUE, 
    password NVARCHAR(255) NOT NULL, 
    created_at DATETIME DEFAULT GETDATE() -- Ngày tạo tài khoản
);

--Giáo viên
CREATE TABLE teachers (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT GETDATE() -- Ngày tạo tài khoản
);

--Môn học
CREATE TABLE courses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL, -- Tên môn học
    description NVARCHAR(MAX), -- Mô tả môn học
    created_by INT NOT NULL, -- ID của giáo viên tạo
    created_at DATETIME DEFAULT GETDATE(), -- Ngày tạo
    CONSTRAINT fk_teacher_course FOREIGN KEY (created_by) REFERENCES teachers(id)
);

--Đăng kí môn học
CREATE TABLE student_courses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT NOT NULL, -- ID của học sinh
    course_id INT NOT NULL, -- ID của môn học
    enrolled_at DATETIME DEFAULT GETDATE(), -- Ngày đăng ký
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(id)
);

--Bài tập
CREATE TABLE assignments (
    id INT IDENTITY(1,1) PRIMARY KEY,
    course_id INT NOT NULL, -- ID môn học
    title NVARCHAR(255) NOT NULL, -- Tiêu đề bài tập
    description NVARCHAR(MAX), -- Mô tả bài tập
    due_date DATE, -- Ngày hết hạn
    created_at DATETIME DEFAULT GETDATE(), -- Ngày tạo
    CONSTRAINT fk_course_assignment FOREIGN KEY (course_id) REFERENCES courses(id)
);

--Nộp bài tập
CREATE TABLE submissions (
    id INT IDENTITY(1,1) PRIMARY KEY,
    assignment_id INT NOT NULL, -- ID bài tập
    student_id INT NOT NULL, -- ID học sinh
    submission_link NVARCHAR(255), -- Đường dẫn bài nộp
    submitted_at DATETIME DEFAULT GETDATE(), -- Thời gian nộp
    feedback NVARCHAR(MAX), -- Phản hồi từ giáo viên
    score FLOAT, -- Điểm số
    CONSTRAINT fk_assignment FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    CONSTRAINT fk_student_submission FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE admins (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL, -- Tên quản trị viên
    email NVARCHAR(100) NOT NULL UNIQUE, -- Email
    password NVARCHAR(255) NOT NULL, -- Mật khẩu
    created_at DATETIME DEFAULT GETDATE() -- Ngày tạo tài khoản
);
