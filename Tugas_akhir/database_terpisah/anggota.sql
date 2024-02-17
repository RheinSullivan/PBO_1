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
-- Struktur dari tabel `anggota`
--

CREATE TABLE `anggota` (
  `Id` int(10) NOT NULL,
  `Nim` int(20) NOT NULL,
  `Nama` varchar(20) NOT NULL,
  `UKM` enum('Himasantika','Himaster','HMTI','Computer Education') NOT NULL,
  `Angkatan` varchar(10) NOT NULL,
  `Jabatan` varchar(50) NOT NULL,
  `Kegiatan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `anggota`
--

INSERT INTO `anggota` (`Id`, `Nim`, `Nama`, `UKM`, `Angkatan`, `Jabatan`, `Kegiatan`) VALUES
(3, 210511021, 'Zahra Rahayu Ratna D', 'Computer Education', '21', 'Wakil Ketua', 'Webinar Nasional AI'),
(4, 210511020, 'Moh. Rifki Ramadhan', 'Computer Education', '21', 'Ketua', 'Webinar Nasional AI'),
(5, 220802010, 'Sodiq Abdullah', 'Himasantika', '22', 'Member Akatsuki', 'MENGENAL ORGANISASI TEKNIK INFORMATIKA ( MOTIF )\r\n'),
(6, 235590101, 'No Pain No Bocor Boc', 'Himaster', '23', 'Ketua Akatsuki', 'Upgrading Himaster'),
(7, 19202122, 'Roxy-Chwan', 'HMTI', '19', 'Istri MC Mushoku Tensei', 'Pengabdian Desa');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Nim` (`Nim`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `anggota`
--
ALTER TABLE `anggota`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
