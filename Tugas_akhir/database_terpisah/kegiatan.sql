-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Feb 2024 pada 15.29
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ukm`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `kegiatan`
--

CREATE TABLE `kegiatan` (
  `Id` int(10) NOT NULL,
  `No` varchar(10) NOT NULL,
  `UKM` varchar(20) NOT NULL,
  `Kegiatan` text NOT NULL,
  `Tgl` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `kegiatan`
--

INSERT INTO `kegiatan` (`Id`, `No`, `UKM`, `Kegiatan`, `Tgl`) VALUES
(1, '1', 'Himasantika', 'MOTIF\r\n', '2023-08-22'),
(2, '2', 'Himasantika', 'LKMMTD ', '2022-08-30'),
(3, '3', 'Himasantika', 'Seminar National IT Fest\r\n', '2023-08-23'),
(4, '4', 'Himaster', 'Rapat Kerja Himaster', '2020-02-06'),
(5, '5', 'Himaster', 'Upgrading Himaster', '2020-06-01'),
(6, '6', 'HMTI', 'Pengabdian Desa', '2022-04-13'),
(7, '7', 'HMTI', 'Industrial Simulation Dan Mabim', '2024-09-04'),
(8, '8', 'Computer Education', 'Webinar Nasional AI', '2023-11-19'),
(9, '9', 'Computer Education', 'Makrab & Upgrading Computer Education 2023', '2023-10-06'),
(10, '10', 'Akatsuki', 'Memburu para Jinchuriki', '2013-10-08');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `kegiatan`
--
ALTER TABLE `kegiatan`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `No` (`No`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `kegiatan`
--
ALTER TABLE `kegiatan`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
