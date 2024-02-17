-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Feb 2024 pada 15.30
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
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
