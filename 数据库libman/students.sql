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

 Date: 10/06/2018 16:19:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `sname` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sno` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `telnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `major` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('魏如意', '16020440115', '男', '15580335390', '软件工程', '1601');
INSERT INTO `students` VALUES ('叶祺斌', '16020440108', '男', '88888888', '软件工程', '1601');

SET FOREIGN_KEY_CHECKS = 1;
