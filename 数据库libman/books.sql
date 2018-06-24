/*
 Navicat MariaDB Data Transfer

 Source Server         : test
 Source Server Type    : MariaDB
 Source Server Version : 100214
 Source Host           : localhost:3306
 Source Schema         : libman

 Target Server Type    : MariaDB
 Target Server Version : 100214
 File Encoding         : 65001

 Date: 10/06/2018 16:18:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books`  (
  `bname` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `author` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `bnum` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `bprices` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `had` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of books
-- ----------------------------
INSERT INTO `books` VALUES ('《战争与和平》', '列夫托尔斯泰', 'zz2316789', '23.5元', '4本');
INSERT INTO `books` VALUES ('《三体》', '刘慈欣', 'st3689563', '36.99元', '3本');
INSERT INTO `books` VALUES ('《sql从入门到放弃》', '未知', 'sq3265984', '36元', '2本');
INSERT INTO `books` VALUES ('《java从入门到放弃》', '张大力', 'ja6598723', '65.3元', '3本');
INSERT INTO `books` VALUES ('《Python大法好》', '魏小意', 'py239865', '59.86元', '5本');
INSERT INTO `books` VALUES ('《如何让自己充满吸引力》', '傻子', 'rh236598', '12元', '3本');
INSERT INTO `books` VALUES ('《如何优雅的装逼》', '叶晓冰', 'zb2368946', '102.8元', '6本');
INSERT INTO `books` VALUES ('《swift从入门到放弃》', 'Jobs', 'sw1234567', '23.5元', '6本');
INSERT INTO `books` VALUES ('《adel》', 'adel', '12345678', '23.5元', '0本');

SET FOREIGN_KEY_CHECKS = 1;
