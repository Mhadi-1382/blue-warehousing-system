-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2025 at 04:07 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blue`
--

-- --------------------------------------------------------

--
-- Table structure for table `productsphrchase`
--

CREATE TABLE `productsphrchase` (
  `productId` int(11) NOT NULL,
  `productName` varchar(500) NOT NULL,
  `productNumber` varchar(300) NOT NULL,
  `productCategory` varchar(300) NOT NULL,
  `productPurchasePrice` varchar(300) NOT NULL,
  `productTotalPrice` varchar(300) NOT NULL,
  `productDiscount` varchar(300) NOT NULL,
  `productDescription` text NOT NULL,
  `productDate` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `productsphrchase`
--

INSERT INTO `productsphrchase` (`productId`, `productName`, `productNumber`, `productCategory`, `productPurchasePrice`, `productTotalPrice`, `productDiscount`, `productDescription`, `productDate`) VALUES
(1, 'نوشابه کوکالا-سیاه', '2', 'نوشیدنی', '250000', '500000', '0', 'در این صفحه می توانید محصول خرید شده خود را ویرایش کنید.', '1403/08/12 19:09'),
(2, 'لیموناد جدید', '8', 'نوشیدنی', '2500000', '31250000', '50', '', '1403/08/12 19:05'),
(3, 'دلستر انگور-هی دی', '35', 'نوشیدنی', '350000', '11270000', '8', '', '1403/06/28 19:51'),
(22, 'نوشابه کوکالا-نارنجی', '10', 'نوشیدنی', '250000', '2050000', '18', '', '1403/07/01 19:57'),
(23, 'دلستر هی دی گندم', '40', 'نوشیدنی', '300000', '21600000', '10', 'تسریع در آماده سازی 20 بسته از محصول برای آقای علی حسینی (افق کوروش).', '1403/08/12 19:03'),
(24, 'نوشابه پپ سی سیاه', '10', 'نوشیدنی', '1500000', '15000000', '0', 'نوشابه پپ سی سیاه', '1403/08/12 20:34');

-- --------------------------------------------------------

--
-- Table structure for table `productssale`
--

CREATE TABLE `productssale` (
  `productId` int(11) NOT NULL,
  `productSeries` varchar(100) NOT NULL,
  `productName` varchar(500) NOT NULL,
  `productNumber` varchar(300) NOT NULL,
  `productPrice` varchar(300) NOT NULL,
  `productTotalPrice` varchar(300) NOT NULL,
  `productDate` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `productssale`
--

INSERT INTO `productssale` (`productId`, `productSeries`, `productName`, `productNumber`, `productPrice`, `productTotalPrice`, `productDate`) VALUES
(26, '2', 'لیموناد جدید', '2', '2500000', '5000000', '1403/08/06 21:05'),
(27, '1', 'نوشابه کوکالا-سیاه', '1', '250000', '250000', '1403/08/12 13:13'),
(28, '2', 'لیموناد جدید', '2', '2500000', '5000000', '1403/08/12 13:14'),
(29, '23', 'دلستر هی دی گندم', '20', '300000', '6000000', '1403/08/12 19:15'),
(31, '23', 'دلستر هی دی گندم', '4', '300000', '1200000', '1403/08/12 19:27'),
(32, '2', 'لیموناد جدید', '10', '2500000', '25000000', '1403/08/12 19:28'),
(33, '23', 'دلستر هی دی گندم', '6', '300000', '1800000', '1403/08/12 20:30'),
(34, '23', 'دلستر هی دی گندم', '10', '300000', '3000000', '1403/08/12 20:31');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(300) NOT NULL,
  `email` varchar(300) NOT NULL,
  `tel` varchar(12) NOT NULL,
  `password` varchar(300) NOT NULL,
  `date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `tel`, `password`, `date`) VALUES
(1, 'محمدمهدی ربیعی', 'mrabiee175@gmail.com', '09031265448', '1234', '1403/06/20 10:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `productsphrchase`
--
ALTER TABLE `productsphrchase`
  ADD PRIMARY KEY (`productId`);

--
-- Indexes for table `productssale`
--
ALTER TABLE `productssale`
  ADD PRIMARY KEY (`productId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `productsphrchase`
--
ALTER TABLE `productsphrchase`
  MODIFY `productId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `productssale`
--
ALTER TABLE `productssale`
  MODIFY `productId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
