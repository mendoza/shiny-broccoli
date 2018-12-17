CREATE TABLE Employees (
	EmployeeID int(11) NOT NULL AUTO_INCREMENT,
	LastName varchar(20) NOT NULL,
	FirstName varchar(10) NOT NULL,
	Title varchar(30) NULL,
	TitleOfCourtesy varchar(25) NULL,
	BirthDate datetime NULL,
	HireDate datetime NULL, 
	Address varchar(60) NULL,
	City varchar(15) NULL,
	Region varchar(15) NULL,
	PostalCode varchar(10) NULL,
	Country varchar(15) NULL,
	HomePhone varchar(24) NULL,
	Extension varchar(4) NULL,
	Photo blob NULL,
	Notes text NULL,
	ReportsTo int NULL,
	PhotoPath varchar(255) NULL,
    PRIMARY KEY(EmployeeID)
);


CREATE TABLE Categories (
	CategoryID int(11)  NOT NULL auto_increment,
	CategoryName varchar(15) NOT NULL ,
	Description text NULL ,
	Picture blob NULL ,
    PRIMARY KEY(CategoryID)
);

CREATE TABLE Customers (
	CustomerID char (5) NOT NULL ,
	CompanyName varchar (40) NOT NULL ,
	ContactName varchar (30) NULL ,
	ContactTitle varchar (30) NULL ,
	CAddress varchar (60) NULL ,
	City varchar (15) NULL ,
	Region varchar (15) NULL ,
	PostalCode varchar (10) NULL ,
	Country varchar (15) NULL ,
	Phone varchar (24) NULL ,
	Fax varchar (24) NULL ,
    PRIMARY KEY(CustomerID)
);
 
CREATE TABLE Shippers (
    ShippersID int(11) NOT NULL auto_increment,
    CompanyName varchar(40) NOT NULL,
    Phone varchar(24) NULL,
    PRIMARY KEY (ShippersID)
);

CREATE TABLE Suppliers (
    SuppliersID int(11) NOT NULL auto_increment,
    CompanyName varchar(40) NOT NULL,
    ContactName varchar(30) NULL,
    ContactTitle varchar(30) NULL,
    Address varchar(60) NULL,
    City varchar(15) NULL,
    Region varchar(15) NULL,
    PostalCode varchar(15) NULL,
    Coountry varchar(10) NULL,
    Phone varchar(24) NULL,
    Fax varchar(24) NULL,
    HamePage varchar(500) NULL,
    PRIMARY KEY(SuppliersID)
);

CREATE TABLE Orders (
    OrderID int(11) NOT NULL auto_increment,
    CustomerID char(5) NULL,
    EmployeeID int(11) NULL,
    OrderDate datetime NULL,
    RequiredDate datetime NULL,
    ShippedDate datetime NULL,
    ShipVia int(11) NULL,
    Freight float(6) NULL,
	ShipName varchar (40) NULL ,
	ShipAddress varchar (60) NULL ,
	ShipCity varchar (15) NULL ,
	ShipRegion varchar (15) NULL ,
	ShipPostalCode varchar (10) NULL ,
	ShipCountry varchar (15) NULL ,
    PRIMARY KEY (OrderID)
);

CREATE TABLE Products (
    ProductID int(11)  NOT NULL AUTO_INCREMENT,
    ProductName varchar(40) NOT NULL,
    SupplierID int(11) NULL,
    CategoryID int(11) NULL,
    QuantityPerUnit varchar(20) NULL,
    UnitPrice float(11) NULL,
    UnitsInStock int(11) NULL,
	UnitsOnOrder int(11) NULL,
	ReorderLevel int(11) NULL,
	Discontinued bit NOT NULL,
    PRIMARY KEY(ProductID)
);

CREATE TABLE  `Order Details` (
    OrderID int(11) NOT NULL PRIMARY KEY, 
    ProductID int(11) NOT NULL,
    UnitPrice float(11) NOT NULL,
    Quantity int(11) NOT NULL,
	Discount float(11) NOT NULL
);

CREATE TABLE CustomerCustomerDemo(
    CustomerID char(5) NOT NULL,
	CustomerTypeID char (10) NOT NULL,
	PRIMARY KEY (CustomerID)
);

CREATE TABLE CustomerDemographics (
	CustomerTypeID char (10) NOT NULL ,
	CustomerDesc varchar(500) NULL ,
    PRIMARY KEY (CustomerTypeID)
); 		
	
CREATE TABLE Region ( 
	RegionID int(11) NOT NULL ,
	RegionDescription char (50) NOT NULL, 
    PRIMARY KEY(RegionID)
);


CREATE TABLE Territories (
	TerritoryID varchar (20) NOT NULL ,
	TerritoryDescription char (50) NOT NULL ,
    RegionID int(11) NOT NULL,
	PRIMARY KEY(TerritoryID)
);

CREATE TABLE EmployeeTerritories (
	EmployeeID int(11) NOT NULL,
	TerritoryID varchar (20) NOT NULL 
);