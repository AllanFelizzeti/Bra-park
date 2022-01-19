-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema testbra_park
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema testbra_park
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testbra_park` DEFAULT CHARACTER SET utf8 ;
USE `testbra_park` ;

-- -----------------------------------------------------
-- Table `testbra_park`.`vagas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbra_park`.`vagas` (
  `N_Vagas` INT(11) NOT NULL,
  `Hora_entrada` TIME NULL DEFAULT NULL,
  `Hora_saida` TIME NULL DEFAULT NULL,
  PRIMARY KEY (`N_Vagas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `testbra_park`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testbra_park`.`carro` (
  `Cpf` VARCHAR(15) NOT NULL,
  `Placa` VARCHAR(10) NULL DEFAULT NULL,
  `Cel` VARCHAR(15) NULL DEFAULT NULL,
  `vagas_N_Vagas` INT(11) NOT NULL,
  PRIMARY KEY (`Cpf`),
  INDEX `fk_carro_vagas_idx` (`vagas_N_Vagas` ASC) ,
  CONSTRAINT `fk_carro_vagas`
    FOREIGN KEY (`vagas_N_Vagas`)
    REFERENCES `testbra_park`.`vagas` (`N_Vagas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
