-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`County`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`County` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `codeCounty` VARCHAR(10) NOT NULL,
  `county` VARCHAR(45) NOT NULL,
  `population` INT NOT NULL,
  `area` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `codeCounty_UNIQUE` (`codeCounty` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Election`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Election` (
  `idElection` INT NOT NULL AUTO_INCREMENT,
  `year` INT NOT NULL,
  `voteCount` INT NOT NULL,
  `politicalParty` VARCHAR(15) CHARACTER SET 'utf8' NOT NULL,
  `codeCounty` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idElection`),
  UNIQUE INDEX `idElection_UNIQUE` (`idElection` ASC) VISIBLE,
  INDEX `fk_election_codeCounty_idx` (`codeCounty` ASC) VISIBLE,
  CONSTRAINT `fk_election_codeCounty`
    FOREIGN KEY (`codeCounty`)
    REFERENCES `mydb`.`County` (`codeCounty`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Coordinator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Coordinator` (
  `idCoordinator` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `document` VARCHAR(10) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCoordinator`),
  UNIQUE INDEX `idCoordinator_UNIQUE` (`idCoordinator` ASC) VISIBLE,
  UNIQUE INDEX `document_UNIQUE` (`document` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
