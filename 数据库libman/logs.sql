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

 Date: 10/06/2018 16:18:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for logs
-- ----------------------------
DROP TABLE IF EXISTS `logs`;
CREATE TABLE `logs`  (
  `bname` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bsno` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `btime` date NOT NULL,
  `howlong` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `outline` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of logs
-- ----------------------------
INSERT INTO `logs` VALUES ('《战争与和平》\r\n', '16020440115', '2018-05-11', '30', '1天');

SET FOREIGN_KEY_CHECKS = 1;
