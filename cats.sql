
/*file: cats.sql
 purpose: Cat Database
 author: Annelise Rasmussen
 version: 1.0
 date: 2024/04/15
*/

CREATE DATABASE IF NOT EXISTS `catsrus` ;

USE catsrus;

CREATE TABLE IF NOT EXISTS `colorTable` (
     `id` int(11) NOT NULL AUTO_INCREMENT,
     `colordesc` VARCHAR(20) DEFAULT NULL,
     PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `nameTable` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `colorid` int(11) DEFAULT NULL,
        `name` VARCHAR(20) DEFAULT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`colorid`) REFERENCES `colorTable`(`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE

) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `contactsTable` (
     `id` int(11) NOT NULL AUTO_INCREMENT,
     `name` VARCHAR(40) DEFAULT NULL,
     `email` VARCHAR(256) DEFAULT NULL,
     `password_hash` VARCHAR(256) DEFAULT NULL, 
     `role` VARCHAR(50) DEFAULT NULL, 
    PRIMARY KEY (`id`)
     
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `movieTable` (
     `id` int(11) NOT NULL AUTO_INCREMENT,
     `name` VARCHAR(50) DEFAULT NULL,
     PRIMARY KEY (`id`)
) ENGINE=InnoDB;




INSERT INTO contactsTable (name, email) values('Mochi', 'mochitreats@catsrus.com');
INSERT INTO contactsTable (name, email) values('Toothless', 'toothless@catsrus.com');
INSERT INTO contactsTable (name, email) values('Luna', 'luna@catsrus.com');
INSERT INTO contactsTable (name, email) values('Lupin', 'lupin@catsrus.com');



INSERT INTO movieTable (name) values('Bolt');
INSERT INTO movieTable (name) values('The Secret Life of Pets');
INSERT INTO movieTable (name) values('Aristocats');
INSERT INTO movieTable (name) values('Olive&Company');
INSERT INTO movieTable (name) values('Lady and the Tramp');
INSERT INTO movieTable (name) values('Puss in Boots');
INSERT INTO movieTable (name) values('Homeward Bound');
INSERT INTO movieTable (name) values('That Darn Cat');
INSERT INTO movieTable (name) values('Nine Lives');
INSERT INTO movieTable (name) values('Garfield: The Movie');
INSERT INTO movieTable (name) values('Cats & Dogs');
INSERT INTO movieTable (name) values('Cats');
INSERT INTO movieTable (name) values('An American Tail');
INSERT INTO movieTable (name) values('The Cat in the Hat');
INSERT INTO movieTable (name) values('Big Hero 6');
INSERT INTO movieTable (name) values('Tom and Jerry');

INSERT INTO colorTable (id, colordesc) values(1, 'White');
INSERT INTO colorTable (id, colordesc) values(2, 'Orange');
INSERT INTO colorTable (id, colordesc) values(3, 'Black');
INSERT INTO colorTable (id, colordesc) values(4, 'Gray');
INSERT INTO colorTable (id, colordesc) values(5, 'Brown');





INSERT INTO `nameTable` (colorid, name) values(1, 'Snowball');

INSERT INTO `nameTable` (colorid, name) values(1, 'Frosty');

INSERT INTO `nameTable` (colorid, name) values(1, 'Ivory');

INSERT INTO `nameTable` (colorid, name) values(1, 'Pearl');

INSERT INTO `nameTable` (colorid, name) values(1, 'Cotton');

INSERT INTO `nameTable` (colorid, name) values(3, 'Midnight');

INSERT INTO `nameTable` (colorid, name) values(3, 'Panther');

INSERT INTO `nameTable` (colorid, name) values(3, 'Onyx');

INSERT INTO `nameTable` (colorid, name) values(3, 'Jet');

INSERT INTO `nameTable` (colorid, name) values(3, 'Shadow');

INSERT INTO `nameTable` (colorid, name) values(4, 'Smokey');

INSERT INTO `nameTable` (colorid, name) values(4, 'Mist');

INSERT INTO `nameTable` (colorid, name) values(4, 'Ash');

INSERT INTO `nameTable` (colorid, name) values(4, 'Silver');

INSERT INTO `nameTable` (colorid, name) values(4, 'Nimbus');

INSERT INTO `nameTable` (colorid, name) values(2, 'Sunshine');

INSERT INTO `nameTable` (colorid, name) values(2, 'Ginger');

INSERT INTO `nameTable` (colorid, name) values(2, 'Rusty');

INSERT INTO `nameTable` (colorid, name) values(2, 'Amber');

INSERT INTO `nameTable` (colorid, name) values(2, 'Tangerine');

INSERT INTO `nameTable` (colorid, name) values(5, 'Cocoa');

INSERT INTO `nameTable` (colorid, name) values(5, 'Chestnut');

INSERT INTO `nameTable` (colorid, name) values(5, 'Hazel');

INSERT INTO `nameTable` (colorid, name) values(5, 'Mocha');

INSERT INTO `nameTable` (colorid, name) values(5, 'Caramel');














