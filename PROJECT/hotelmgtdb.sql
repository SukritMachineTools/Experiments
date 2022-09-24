-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2022 at 01:10 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmgtdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `usertype`) VALUES
('tushar', '123', 'Admin'),
('pratham', '456', 'Employee'),
('gurmeher', '789', 'Employee');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `contact` varchar(200) NOT NULL,
  `checkin` varchar(200) NOT NULL,
  `checkout` varchar(200) NOT NULL,
  `roomtype` varchar(20) NOT NULL,
  `numberofdays` varchar(20) NOT NULL,
  `paidtax` varchar(200) NOT NULL,
  `totalbill` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`contact`, `checkin`, `checkout`, `roomtype`, `numberofdays`, `paidtax`, `totalbill`) VALUES
('8888888889', '01/09/2022', '07/09/2022', 'Double Bed Room', '6', '275', '3275'),
('9877872240', '01/09/2022', '05/09/2022', 'Single Bed Room', '4', '125', '2125'),
('9888813118', '01/09/2022', '06/09/2022', 'Luxury Bed Room', '5', '1875', '9375');

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `customername` varchar(20) NOT NULL,
  `customerphone` varchar(12) NOT NULL,
  `customeremail` varchar(20) NOT NULL,
  `roomnumber` varchar(10) NOT NULL,
  `idproof` varchar(20) NOT NULL,
  `idnumber` varchar(30) NOT NULL,
  `nationality` varchar(20) NOT NULL,
  `customeraddress` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`customername`, `customerphone`, `customeremail`, `roomnumber`, `idproof`, `idnumber`, `nationality`, `customeraddress`) VALUES
('tushra', '8888888888', 'tushar@gmail.com', '202', 'Adhaar Card', '12345678900987654321', 'indian', 'delhi\n\n\n');

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `floor` varchar(20) NOT NULL,
  `roomnumber` varchar(20) NOT NULL,
  `roomtype` varchar(20) NOT NULL,
  `roomstatus` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`floor`, `roomnumber`, `roomtype`, `roomstatus`) VALUES
('1', '101', 'Single Bedroom', 'Occupied'),
('1', '102', 'Single Bedroom', 'Available'),
('1', '103', 'Double Bedroom', 'Available'),
('1', '104', 'Double Bedroom', 'Available'),
('2', '201', 'Single Bedroom', 'Available'),
('2', '202', 'Single Bedroom', 'Occupied'),
('2', '203', 'Double Bedroom', 'Available'),
('2', '204', 'Double Bedroom', 'Available'),
('3', '301', 'Single Bedroom', 'Available'),
('3', '302', 'Single Bedroom', 'Available'),
('3', '303', 'Double Bedroom', 'Available'),
('3', '304', 'Double Bedroom', 'Available'),
('3', '305', 'Deluxe Bedroom', 'Available'),
('4', '401', 'Single Bedroom', 'Available'),
('4', '402', 'Double Bedroom', 'Available'),
('4', '403', 'Deluxe Bedroom', 'Available'),
('4', '404', 'Deluxe Bedroom', 'Available'),
('5', '501', 'Single Bedroom', 'Available'),
('5', '502', 'Double Bedroom', 'Available'),
('5', '503', 'Deluxe Bedroom', 'Available'),
('5', '504', 'Deluxe Bedroom', 'Available');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`contact`);

--
-- Indexes for table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`customerphone`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`roomnumber`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
