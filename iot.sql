-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 10 déc. 2023 à 14:18
-- Version du serveur : 5.7.36-log
-- Version de PHP : 7.4.28

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de données : `iot`
--

-- --------------------------------------------------------

--
-- Structure de la table `data_object`
--

DROP TABLE IF EXISTS `data_object`;
CREATE TABLE IF NOT EXISTS `data_object` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `message` text,
  `topic` varchar(255) NOT NULL,
  `object` varchar(255) DEFAULT NULL,
  `accuracy` float DEFAULT NULL,
  `qos` int(11) DEFAULT NULL,
  `detected_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `data_object`
--

INSERT INTO `data_object` (`id`, `message`, `topic`, `object`, `accuracy`, `qos`, `detected_at`, `created_at`, `updated_at`) VALUES
(1, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": 1700604559.895393}', 'iot', 'person', 0.793768, 0, '2023-11-21 22:25:35', '2023-11-21 22:25:35', '2023-11-21 22:25:35'),
(100, NULL, 'iot', NULL, NULL, NULL, NULL, NULL, NULL),
(101, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": 1700604559}', 'iot', NULL, NULL, NULL, NULL, NULL, NULL),
(102, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": 1700604559}', 'iot', 'person', 0.793768, 0, NULL, NULL, NULL),
(103, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7114630937576294, \"detected_at\": 1700606817.909938}', 'iot', 'person', 0.711463, 0, NULL, NULL, NULL),
(104, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": 1700606817.909938}', 'iot', 'person', 0.793768, 0, NULL, NULL, NULL),
(105, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7114630937576294, \"detected_at\": 1700607021.52603}', 'iot', 'person', 0.711463, 0, NULL, '2023-11-21 22:50:21', NULL),
(106, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": 1700607021.52802}', 'iot', 'person', 0.793768, 0, NULL, '2023-11-21 22:50:21', NULL),
(107, NULL, '', NULL, NULL, NULL, '2023-11-14 22:50:57', '2023-11-17 22:50:57', '2023-11-21 22:50:57'),
(108, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7114630937576294, \"detected_at\": \"1700608888\"}', 'iot', 'person', 0.711463, 0, NULL, '2023-11-21 23:21:28', '2023-11-21 23:21:28'),
(109, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": \"1700608888\"}', 'iot', 'person', 0.793768, 0, NULL, '2023-11-21 23:21:28', '2023-11-21 23:21:28'),
(110, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7114630937576294, \"detected_at\": \"1700608908\"}', 'iot', 'person', 0.711463, 0, NULL, '2023-11-21 23:21:48', '2023-11-21 23:21:48'),
(111, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": \"1700608908\"}', 'iot', 'person', 0.793768, 0, NULL, '2023-11-21 23:21:48', '2023-11-21 23:21:48'),
(112, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7114630937576294, \"detected_at\": \"1700687275\"}', 'iot', 'person', 0.711463, 0, NULL, '2023-11-22 21:07:55', '2023-11-22 21:07:55'),
(113, '{\"image_name\": \"174908774-la-voiture-passe-par-l-entr\\u00e9e-avec-une-barri\\u00e8re-sur-le-parking-souterrain.jpg\", \"prediction\": \"person\", \"confidence\": 0.7937675714492798, \"detected_at\": \"1700687275\"}', 'iot', 'person', 0.793768, 0, NULL, '2023-11-22 21:07:55', '2023-11-22 21:07:55');
SET FOREIGN_KEY_CHECKS=1;
COMMIT;
