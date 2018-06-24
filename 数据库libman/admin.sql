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

 Date: 10/06/2018 16:18:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `account` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sno` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1612002884@qq.com', '123456', 'admin', 'admin');
INSERT INTO `admin` VALUES ('adeljck@gmail.com', 'weiruyi123', 'admin', 'admin');
INSERT INTO `admin` VALUES ('adeljck', '123456', 'student', '16020440115');

SET FOREIGN_KEY_CHECKS = 1;
