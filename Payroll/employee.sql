-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2025 at 01:49 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee_payroll`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_code` varchar(20) NOT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `hr_location` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `doj` date DEFAULT NULL,
  `proof_id` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  `month` varchar(20) DEFAULT NULL,
  `year` varchar(10) DEFAULT NULL,
  `salary` float DEFAULT NULL,
  `total_days` int(11) DEFAULT NULL,
  `absent_days` int(11) DEFAULT NULL,
  `medical` float DEFAULT NULL,
  `pf` float DEFAULT NULL,
  `convience` float DEFAULT NULL,
  `net_salary` float DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_code`, `designation`, `name`, `age`, `gender`, `email`, `hr_location`, `dob`, `doj`, `proof_id`, `contact`, `status`, `experience`, `month`, `year`, `salary`, `total_days`, `absent_days`, `medical`, `pf`, `convience`, `net_salary`, `address`) VALUES
('E001', 'Software Engineer', 'John Doe', 28, 'Male', 'john.doe@example.com', 'Hyderabad', '1996-05-12', '2021-07-01', 'A123456789', '9876543210', 'Active', '2 years', 'May', '2025', 60000, 31, 1, 2000, 1800, 1500, 58700, 'H.No 4-5, Tech Lane, Hyderabad');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
