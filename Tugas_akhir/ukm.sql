-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Feb 2024 pada 10.13
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

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `email`, `nama`, `password`, `level`) VALUES
(1, 'uchihambatoyib@umc.ac.id', 'Uchiha Sakura', '$2y$10$BzqqNPejAUyOraPKKKCK2.xbrToZgOq9GnlmBtAMThvtB2zCTg4O.', 'mahasiswa'),
(2, 'uchihabangtoyib@gmail.com', 'Uchiha Sasuke', '$2y$10$NgiUETWu9BYXGKOTil.aOO5NobC1Nq5kREKYxG9cdnl4rhUZ/Tpci', 'dosen'),
(3, 'zahrarizky@rheinsullivan.my.id', 'Zahra Rahayu Ratna Dewi', '$2y$10$i.GRsHyXlF0DUlIyGF96Zul5PFkm3Rq7C/1WOxd19WmKQercK5J8i', 'admin'),
(4, 'rizkyzahra@rheinsullivan.my.id', 'Moh. Rifki Ramadhan, S.SI', '$2y$10$2vl40E6j9RS7dhhl2Jo6Y..afee1P6gaaXGq28B1DTfT7CNiT85zW', 'admin');

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
-- Indeks untuk tabel `kegiatan`
--
ALTER TABLE `kegiatan`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `No` (`No`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `anggota`
--
ALTER TABLE `anggota`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `kegiatan`
--
ALTER TABLE `kegiatan`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
