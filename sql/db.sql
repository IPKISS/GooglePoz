-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.27 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL version:             7.0.0.4053
-- Date/time:                    2013-05-31 22:42:18
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;

-- Dumping database structure for google
CREATE DATABASE IF NOT EXISTS `google` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `google`;


-- Dumping structure for table google.keywords
CREATE TABLE IF NOT EXISTS `keywords` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `page_id` int(10) NOT NULL,
  `keyword` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Keywords that will be checkd\r\n';

-- Data exporting was unselected.


-- Dumping structure for table google.pages
CREATE TABLE IF NOT EXISTS `pages` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `page` varchar(150) NOT NULL COMMENT 'Without "http, https" or "www"',
  PRIMARY KEY (`id`),
  UNIQUE KEY `page` (`page`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='List of page that will be checked';

-- Data exporting was unselected.


-- Dumping structure for table google.results
CREATE TABLE IF NOT EXISTS `results` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `page` int(10) DEFAULT '0',
  `position` int(10) DEFAULT '0',
  `page_id` int(10) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Table for main.py result for specific page.';

-- Data exporting was unselected.
/*!40014 SET FOREIGN_KEY_CHECKS=1 */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
