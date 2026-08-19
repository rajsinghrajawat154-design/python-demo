-- STUDENT Table
CREATE TABLE STUDENT (
    Roll_No     INT PRIMARY KEY,
    Name        VARCHAR(50) NOT NULL,
    Branch      VARCHAR(30),
    Year        INT,
    Section     VARCHAR(5),
    Hostel      VARCHAR(30),
    F_Name      VARCHAR(50),
    Address     VARCHAR(100)
);

-- BOOK Table
CREATE TABLE BOOK (
    Book_Id     INT PRIMARY KEY,
    Title       VARCHAR(100) NOT NULL,
    Author      VARCHAR(50),
    Publisher   VARCHAR(50),
    Cost        DECIMAL(10,2),
    Copies      INT CHECK (Copies >= 0)
);

-- TRANSACTION Table
CREATE TABLE TRANSACTION (
    Roll_No     INT,
    Book_Id     INT,
    Date_Issue  DATE,
    Date_Return DATE,
    Fine        DECIMAL(10,2),
    PRIMARY KEY (Roll_No, Book_Id, Date_Issue),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (Book_Id) REFER-- STUDENT Table
CREATE TABLE STUDENT (
    Roll_No     INT PRIMARY KEY,
    Name        VARCHAR(50) NOT NULL,
    Branch      VARCHAR(30),
    Year        INT,
    Section     VARCHAR(5),
    Hostel      VARCHAR(30),
    F_Name      VARCHAR(50),
    Address     VARCHAR(100)
);

-- BOOK Table
CREATE TABLE BOOK (
    Book_Id     INT PRIMARY KEY,
    Title       VARCHAR(100) NOT NULL,
    Author      VARCHAR(50),
    Publisher   VARCHAR(50),
    Cost        DECIMAL(10,2),
    Copies      INT CHECK (Copies >= 0)
);

-- TRANSACTION Table
CREATE TABLE TRANSACTION (
    Roll_No     INT,
    Book_Id     INT,
    Date_Issue  DATE,
    Date_Return DATE,
    Fine        DECIMAL(10,2),
    PRIMARY KEY (Roll_No, Book_Id, Date_Issue),
    FOREIGN KEY (Roll_No) REFERENCES STUDENT(Roll_No),
    FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id)
);