CREATE DATABASE  IF NOT EXISTS `django_hr` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `django_hr`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: django_hr
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add auth_user',5,'add_user'),(18,'Can change auth_user',5,'change_user'),(19,'Can delete auth_user',5,'delete_user'),(20,'Can view auth_user',5,'view_user'),(21,'Can add Token',6,'add_token'),(22,'Can change Token',6,'change_token'),(23,'Can delete Token',6,'delete_token'),(24,'Can view Token',6,'view_token'),(25,'Can add token',7,'add_tokenproxy'),(26,'Can change token',7,'change_tokenproxy'),(27,'Can delete token',7,'delete_tokenproxy'),(28,'Can view token',7,'view_tokenproxy'),(29,'Can add employee',8,'add_employee'),(30,'Can change employee',8,'change_employee'),(31,'Can delete employee',8,'delete_employee'),(32,'Can view employee',8,'view_employee'),(33,'Can add auth_user to employee',9,'add_usertoemployee'),(34,'Can change auth_user to employee',9,'change_usertoemployee'),(35,'Can delete auth_user to employee',9,'delete_usertoemployee'),(36,'Can view auth_user to employee',9,'view_usertoemployee'),(37,'Can add auth_user employee mapping',10,'add_useremployeemapping'),(38,'Can change auth_user employee mapping',10,'change_useremployeemapping'),(39,'Can delete auth_user employee mapping',10,'delete_useremployeemapping'),(40,'Can view auth_user employee mapping',10,'view_useremployeemapping'),(41,'Can add org department',11,'add_orgdepartment'),(42,'Can change org department',11,'change_orgdepartment'),(43,'Can delete org department',11,'delete_orgdepartment'),(44,'Can view org department',11,'view_orgdepartment'),(45,'Can add position',12,'add_position'),(46,'Can change position',12,'change_position'),(47,'Can delete position',12,'delete_position'),(48,'Can view position',12,'view_position'),(49,'Can add org unit',13,'add_orgunit'),(50,'Can change org unit',13,'change_orgunit'),(51,'Can delete org unit',13,'delete_orgunit'),(52,'Can view org unit',13,'view_orgunit'),(53,'Can add job information',14,'add_jobinformation'),(54,'Can change job information',14,'change_jobinformation'),(55,'Can delete job information',14,'delete_jobinformation'),(56,'Can view job information',14,'view_jobinformation'),(57,'Can add punch record',15,'add_punchrecord'),(58,'Can change punch record',15,'change_punchrecord'),(59,'Can delete punch record',15,'delete_punchrecord'),(60,'Can view punch record',15,'view_punchrecord');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (15,'attend','punchrecord'),(2,'auth','group'),(1,'auth','permission'),(5,'auths','auth_user'),(6,'authtoken','token'),(7,'authtoken','tokenproxy'),(3,'contenttypes','contenttype'),(8,'employee','employee'),(14,'employee','jobinformation'),(11,'employee','orgdepartment'),(13,'employee','orgunit'),(12,'employee','position'),(10,'employee','useremployeemapping'),(9,'employee','usertoemployee'),(4,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-12 00:43:13.896397'),(2,'contenttypes','0002_remove_content_type_name','2020-10-12 00:43:14.062779'),(3,'auth','0001_initial','2020-10-12 00:43:14.197661'),(4,'auth','0002_alter_permission_name_max_length','2020-10-12 00:43:14.650232'),(5,'auth','0003_alter_user_email_max_length','2020-10-12 00:43:14.659208'),(6,'auth','0004_alter_user_username_opts','2020-10-12 00:43:14.666189'),(7,'auth','0005_alter_user_last_login_null','2020-10-12 00:43:14.675204'),(8,'auth','0006_require_contenttypes_0002','2020-10-12 00:43:14.681149'),(9,'auth','0007_alter_validators_add_error_messages','2020-10-12 00:43:14.690162'),(10,'auth','0008_alter_user_username_max_length','2020-10-12 00:43:14.698140'),(11,'auth','0009_alter_user_last_name_max_length','2020-10-12 00:43:14.707080'),(12,'auth','0010_alter_group_name_max_length','2020-10-12 00:43:14.727027'),(13,'auth','0011_update_proxy_permissions','2020-10-12 00:43:14.736039'),(14,'auth','0012_alter_user_first_name_max_length','2020-10-12 00:43:14.744978'),(15,'auths','0001_initial','2020-10-12 00:43:14.810075'),(16,'sessions','0001_initial','2020-10-12 00:43:14.852936'),(17,'auths','0002_auto_20201012_0845','2020-10-12 00:45:07.698638'),(18,'authtoken','0001_initial','2020-10-12 14:19:47.284181'),(19,'authtoken','0002_auto_20160226_1747','2020-10-12 14:19:47.723193'),(20,'authtoken','0003_tokenproxy','2020-10-12 14:19:47.733170'),(21,'employee','0001_initial','2020-10-12 14:19:47.945640'),(22,'employee','0002_auto_20201012_2220','2020-10-12 14:21:01.742451'),(23,'employee','0003_auto_20201012_2240','2020-10-12 14:40:59.941158'),(24,'employee','0004_delete_usertoemployee','2020-10-12 14:58:12.396340'),(25,'employee','0005_auto_20201012_2323','2020-10-12 15:23:31.752561'),(26,'employee','0006_auto_20201013_0509','2020-10-12 21:09:45.625530'),(27,'employee','0007_useremployeemapping','2020-10-12 21:16:13.638871'),(28,'employee','0008_auto_20201013_0812','2020-10-13 00:12:40.695967'),(29,'employee','0009_auto_20201013_0833','2020-10-13 00:33:39.156218'),(30,'employee','0010_auto_20201013_1427','2020-10-13 06:27:53.611252'),(31,'employee','0011_auto_20201013_1512','2020-10-13 07:12:29.981993'),(32,'employee','0012_auto_20201013_1515','2020-10-13 07:15:07.277276'),(33,'employee','0013_auto_20201013_1529','2020-10-13 07:29:31.509889'),(34,'employee','0014_orgunit_is_root','2020-10-13 08:07:20.348693'),(35,'employee','0015_auto_20201013_1622','2020-10-13 08:22:59.725402'),(36,'employee','0016_auto_20201013_1632','2020-10-13 08:32:05.905982'),(37,'employee','0017_auto_20201013_1748','2020-10-13 09:48:42.169223'),(38,'employee','0018_auto_20201014_2317','2020-10-14 15:17:17.978254'),(39,'employee','0019_auto_20201016_0554','2020-10-15 21:54:46.564078'),(40,'attend','0001_initial','2020-10-16 00:57:16.999111'),(41,'attend','0002_auto_20201018_1520','2020-10-18 07:20:55.803934');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('2020-10-13 00:37:39.856768','','2020-10-15 21:59:23.051997','',0,NULL,'','KMwEmeiuJ4kjR7BjBenm6Q',22,0,'441424199406030522','15626102267','kHRQfBZeRm6pxSmPVAQQ3K',0,NULL,'yachne','000002',1),('2020-10-12 15:24:12.639417','','2020-10-12 20:36:38.337501','',0,NULL,'','WpJbcL5XaHDTk2eAAarobJ',24,1,'441323199208260798','15768158635','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'petrel','000001',0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `jobinformation`
--

LOCK TABLES `jobinformation` WRITE;
/*!40000 ALTER TABLE `jobinformation` DISABLE KEYS */;
INSERT INTO `jobinformation` VALUES ('2020-10-15 21:59:23.054476','aCXUpoR4eACAz3BLeyL3ba','2020-10-15 21:59:23.054476','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','9Tf4SLJJJrxgbsNzWR83VK','2020-10-14','2199-12-31',0,0,'fTgHWHgE6U997qVpN6MPvf','KMwEmeiuJ4kjR7BjBenm6Q','38M5NhRtoJzHS9HCUB4XR8','LjdD5LacchGYpKxfnRzqHz'),('2020-10-14 20:05:42.332840','aCXUpoR4eACAz3BLeyL3ba','2020-10-14 20:05:42.333836','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','knbmxaUzB8dx2M5GWUhrbA','2020-10-14','2199-12-31',0,0,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ','38M5NhRtoJzHS9HCUB4XR8','LjdD5LacchGYpKxfnRzqHz');
/*!40000 ALTER TABLE `jobinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `org_department`
--

LOCK TABLES `org_department` WRITE;
/*!40000 ALTER TABLE `org_department` DISABLE KEYS */;
INSERT INTO `org_department` VALUES ('2020-10-13 15:46:05.967601','','2020-10-13 22:56:20.662511','aCXUpoR4eACAz3BLeyL3ba',1,'2020-10-14 06:56:20.661546','aCXUpoR4eACAz3BLeyL3ba','9ziecaEBj5sDHtaGV4YSMt','2020-10-14','2199-12-31',NULL,'LjdD5LacchGYpKxfnRzqHz','浪潮董事会','000003'),('2020-10-14 15:32:35.054208','aCXUpoR4eACAz3BLeyL3ba','2020-10-14 15:32:35.054208','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','fTgHWHgE6U997qVpN6MPvf','2020-10-14','2199-12-31',NULL,'LjdD5LacchGYpKxfnRzqHz','浪潮董事会','000001');
/*!40000 ALTER TABLE `org_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `org_unit`
--

LOCK TABLES `org_unit` WRITE;
/*!40000 ALTER TABLE `org_unit` DISABLE KEYS */;
INSERT INTO `org_unit` VALUES ('2020-10-13 08:32:10.172658','','2020-10-13 08:32:10.172658','',0,NULL,'','LjdD5LacchGYpKxfnRzqHz','2020-10-13','2199-12-31',NULL,'浪潮云服务技术有限公司','000001',1),('2020-10-13 09:20:53.123275','','2020-10-13 09:20:53.123275','',0,NULL,'','VUJvjvQQtBXFEbtvTh3QPG','2020-10-13','2199-12-31','LjdD5LacchGYpKxfnRzqHz','浪潮云服务子公司1','000002',0);
/*!40000 ALTER TABLE `org_unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES ('2020-10-14 15:34:07.419026','aCXUpoR4eACAz3BLeyL3ba','2020-10-14 15:34:07.419026','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','38M5NhRtoJzHS9HCUB4XR8','2020-10-14','2199-12-31','fTgHWHgE6U997qVpN6MPvf','大董事长','000001');
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `punch_record`
--

LOCK TABLES `punch_record` WRITE;
/*!40000 ALTER TABLE `punch_record` DISABLE KEYS */;
INSERT INTO `punch_record` VALUES ('2020-10-18 08:34:34.664924','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:34:34.664924','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','2HRzyN8nFB7ZK9sg6MKUhe','2020-10-18 08:28:34.656514',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 08:33:16.992394','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:33:16.992394','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','6XXQb3HKpQAX4WzSvkt5a8','2020-10-18 08:27:16.862819',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 08:34:36.498182','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:34:36.498182','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','Adjt5GJteCDpjffhfZKkaf','2020-10-18 08:28:36.489745',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 08:34:32.892647','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:34:32.892647','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','Eomo6MgjwM6VJQJcPLMS2G','2020-10-18 08:28:32.884179',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 08:30:57.122009','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:30:57.122009','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','gMnwzqkGxhHgudNbPe2gfv','2020-10-18 07:10:23.000000',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 07:57:40.454099','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 07:57:40.454099','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','ijBZRZvL7ptSGqNSixvLew','2020-10-18 07:10:23.000000',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ'),('2020-10-18 08:34:05.634265','aCXUpoR4eACAz3BLeyL3ba','2020-10-18 08:34:05.634265','aCXUpoR4eACAz3BLeyL3ba',0,NULL,'','jrctf8SHWUNTZ7koMgmdGs','2020-10-18 08:28:05.625870',NULL,NULL,'fTgHWHgE6U997qVpN6MPvf','WpJbcL5XaHDTk2eAAarobJ');
/*!40000 ALTER TABLE `punch_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('pbkdf2_sha256$216000$S7Y6hG0yka7B$9/hLS7ceqFCuaKeW/4IFtVT+uk9VoDtkklqGPlTnTec=',NULL,'2020-10-12 00:45:19.775399','','2020-10-12 00:45:19.775399','',0,NULL,'','aCXUpoR4eACAz3BLeyL3ba','petrel',1),('gHoSJBHD',NULL,'2020-10-15 21:59:23.049517','','2020-10-15 21:59:23.049517','',0,NULL,'','kHRQfBZeRm6pxSmPVAQQ3K','15626102267',0);
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-18 19:15:26