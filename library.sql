-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookcopies`
--

DROP TABLE IF EXISTS `bookcopies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookcopies` (
  `bookcopyid` int NOT NULL AUTO_INCREMENT,
  `bookid` int NOT NULL,
  `format` varchar(12) NOT NULL,
  PRIMARY KEY (`bookcopyid`),
  KEY `bookid_idx` (`bookid`),
  CONSTRAINT `bookid` FOREIGN KEY (`bookid`) REFERENCES `books` (`bookid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4790 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookcopies`
--

LOCK TABLES `bookcopies` WRITE;
/*!40000 ALTER TABLE `bookcopies` DISABLE KEYS */;
INSERT INTO `bookcopies` VALUES (3,56,'Hardcover'),(4,7455,'Paperback'),(7,34,'Paperback'),(11,56,'Paperback'),(19,56,'Paperback'),(25,7455,'Hardcover'),(34,7455,'Paperback'),(47,34,'Paperback'),(49,7455,'Paperback'),(56,56,'Paperback'),(81,56,'Audio Book'),(93,56,'Paperback'),(234,7455,'Paperback'),(4789,34,'Illustrated');
/*!40000 ALTER TABLE `bookcopies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `bookid` int NOT NULL AUTO_INCREMENT,
  `booktitle` varchar(45) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `category` varchar(15) DEFAULT NULL,
  `yearofpublication` int DEFAULT NULL,
  `description` longtext,
  `branchid` int DEFAULT NULL,
  PRIMARY KEY (`bookid`)
) ENGINE=InnoDB AUTO_INCREMENT=7456 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (34,'The Wind in the Willows','Kenneth Grahame ','Fiction',1908,'The Wind in the Willows is a children\'s novel by Kenneth Grahame, first published in England in 1908. The story focuses on four anthropomorphized animals in a pastoral version of Edwardian England. The novel is notable for its mixture of mysticism, adventure, morality and camaraderie, and celebrated for its evocation of the nature of the Thames Valley. It is a delightful and captivating tale that is sure to delight.',NULL),(56,'Harry Potter and the Order of the Phoenix','J. K. Rowling','Fiction',2011,'Dark times have come to Hogwarts. After the Dementors\' attack on his cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to find him. There are many who deny the Dark Lord\'s return, but Harry is not alone: a secret order gathers at Grimmauld Place to fight against the Dark forces. Harry must allow Professor Snape to teach him how to protect himself from Voldemort\'s savage assaults on his mind. But they are growing stronger by the day and Harry is running out of time ...',NULL),(7455,'Python Crash Course','Eric Matthes','Non-Fiction',2019,'A fast-paced, no-nonsense, updated guide to programming in Python.',NULL);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrowers`
--

DROP TABLE IF EXISTS `borrowers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowers` (
  `borrowerid` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) NOT NULL,
  `familyname` varchar(45) NOT NULL,
  `dateofbirth` date DEFAULT NULL,
  `housenumbername` varchar(15) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `town` varchar(25) DEFAULT NULL,
  `city` varchar(25) DEFAULT NULL,
  `postalcode` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`borrowerid`)
) ENGINE=InnoDB AUTO_INCREMENT=65237 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowers`
--

LOCK TABLES `borrowers` WRITE;
/*!40000 ALTER TABLE `borrowers` DISABLE KEYS */;
INSERT INTO `borrowers` VALUES (533,'Zhe','Wang','2001-03-16','Apartment 3','Prebblewood Drive','Prebbleton','Prebbleton','7601'),(659,'Di','Wang','2003-11-25','26','Kahu Rd','Lincoln','Lincoln','7609'),(7523,'Simon','Charles','1980-07-24','Elizabeth Lodge','Elmwood Drive','Lincoln','CHC','7608'),(65233,'Charlie','Venz','2013-11-05','3','Windsor Rd','Hoon Hay','Christchurch','8034'),(65234,'test1','test','2010-08-01','aa','bb','cc','dd','1234'),(65235,'aa','ss','2023-02-02','ss','ss','ss','ss','ss'),(65236,'Simon','C','2023-01-05','aa','bb','dd','chc','8053');
/*!40000 ALTER TABLE `borrowers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarybranch`
--

DROP TABLE IF EXISTS `librarybranch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarybranch` (
  `branchid` int NOT NULL AUTO_INCREMENT,
  `branchname` varchar(45) NOT NULL,
  PRIMARY KEY (`branchid`),
  UNIQUE KEY `branchid_UNIQUE` (`branchid`),
  UNIQUE KEY `branchname_UNIQUE` (`branchname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarybranch`
--

LOCK TABLES `librarybranch` WRITE;
/*!40000 ALTER TABLE `librarybranch` DISABLE KEYS */;
/*!40000 ALTER TABLE `librarybranch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loans` (
  `loanid` int NOT NULL AUTO_INCREMENT,
  `bookcopyid` int NOT NULL,
  `borrowerid` int NOT NULL,
  `loandate` date NOT NULL,
  `returned` tinyint DEFAULT NULL,
  PRIMARY KEY (`loanid`),
  KEY `borrowedbook_idx` (`bookcopyid`),
  KEY `borrower_idx` (`borrowerid`),
  CONSTRAINT `borrowedbook` FOREIGN KEY (`bookcopyid`) REFERENCES `bookcopies` (`bookcopyid`),
  CONSTRAINT `borrower` FOREIGN KEY (`borrowerid`) REFERENCES `borrowers` (`borrowerid`)
) ENGINE=InnoDB AUTO_INCREMENT=5468994 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
INSERT INTO `loans` VALUES (236,4789,7523,'2021-12-10',1),(54656,47,659,'2022-07-28',1),(2333546,93,7523,'2022-11-30',1),(2355546,4789,65233,'2022-10-10',1),(2395546,4789,533,'2022-01-01',1),(5468956,34,659,'2022-07-28',1),(5468987,11,533,'2023-02-06',1),(5468988,81,533,'2023-02-09',0),(5468989,4,659,'2023-02-09',0),(5468990,4789,7523,'2023-02-09',0),(5468991,11,65233,'2023-02-09',0),(5468992,3,659,'2023-02-09',0),(5468993,81,65234,'2023-02-09',0);
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-10 16:05:00
