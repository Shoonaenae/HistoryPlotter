-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2022 at 03:30 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `historyplotter`
--

-- --------------------------------------------------------

--
-- Table structure for table `uploads`
--

CREATE TABLE `uploads` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `uploads`
--

INSERT INTO `uploads` (`id`, `file`) VALUES
(34, 'xampp-windows-x64-8.1.10-0-VS16-installer.exe'),
(35, 'xampp-windows-x64-8.1.10-0-VS16-installer.exe'),
(36, 'Output.pdf'),
(37, 'Output.pdf'),
(38, 'Test.docx'),
(39, 'brailledots.txt'),
(40, 'forbraille.psd'),
(41, 'text_to_braille.py'),
(42, 'text_to_braille.py'),
(43, 'results.png'),
(44, 'results.png'),
(45, 'Test.docx'),
(46, 'Test.docx'),
(47, 'Test_UBkS3nS.docx'),
(48, 'results.png'),
(49, 'results_sXvlnZO.png'),
(50, 'text_to_braille.py'),
(51, 'text_to_braille.py'),
(52, 'text_to_braille_OsAY5o2.py'),
(53, 'text_to_braille_zvNCbe5.py'),
(54, 'text_to_braille_HBbLT91.py'),
(55, 'idk.py'),
(56, 'results.png'),
(57, 'idk_uTcmiQz.py'),
(58, 'results_inYoAsT.png'),
(59, 'idk_j2rflhc.py'),
(60, 'results_vm4yLfl.png'),
(61, 'example.png'),
(62, 'med_scan.jpg'),
(63, 'test.pdf'),
(64, 'test_003pTQR.pdf'),
(65, 'idk_NYkFemk.py'),
(66, 'brailledots.txt'),
(67, 'idk_SFEt5KW.py');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `uploads`
--
ALTER TABLE `uploads`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `uploads`
--
ALTER TABLE `uploads`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
