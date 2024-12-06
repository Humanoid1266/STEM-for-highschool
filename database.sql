drop table dangkituyensinh
CREATE TABLE dangkituyensinh (
    id INT IDENTITY(1,1) PRIMARY KEY, -- ID tự tăng
    parent_name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    phone NVARCHAR(15) NOT NULL,
    student_school NVARCHAR(255) NOT NULL,
    student_birth_year INT NOT NULL,
    city NVARCHAR(100) NOT NULL,
    submitted_at DATETIME DEFAULT GETDATE(), -- Thời gian gửi thông tin
    CONSTRAINT check_email_format CHECK (CHARINDEX('@', email) > 0), -- Kiểm tra email có chứa '@'
    CONSTRAINT check_phone_format CHECK (LEN(phone) IN (10, 11) AND phone NOT LIKE '%[^0-9]%') -- Kiểm tra số điện thoại hợp lệ
);

CREATE TABLE menu (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL, -- Tên mục menu
    link NVARCHAR(255) NOT NULL, -- Đường dẫn trang
    parent_id INT NULL, -- ID của mục cha
    order_index INT NOT NULL -- Thứ tự hiển thị
);

CREATE TABLE gioithieu (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL, -- Tiêu đề
    content TEXT NOT NULL, -- Nội dung
    image NVARCHAR(255), -- Hình ảnh
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE tintuc (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    image NVARCHAR(255),
    category NVARCHAR(100), -- Danh mục
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE truyenthong (
    id INT IDENTITY(1,1) PRIMARY KEY,
    media_type NVARCHAR(50) NOT NULL, -- ảnh, video 
    url NVARCHAR(255) NOT NULL, -- Đường dẫn media
    description NVARCHAR(255), -- Mô tả
    related_page NVARCHAR(100), -- Trang liên quan
    uploaded_at DATETIME DEFAULT GETDATE()
);

-- Bảng phản hồi
CREATE TABLE phanhoi (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL, -- Tên người gửi
    email NVARCHAR(100),
    message TEXT NOT NULL, -- Nội dung phản hồi
    received_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE sukien (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    event_date DATE NOT NULL, -- Ngày tổ chức
    location NVARCHAR(255), -- Địa điểm
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE solieunoibat (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(100) NOT NULL,
    value INT NOT NULL, -- Giá trị số liệu
    description NVARCHAR(255),
    created_at DATETIME DEFAULT GETDATE()
);
