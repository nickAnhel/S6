USE `lab1`;

CREATE TABLE IF NOT EXISTS `lab1`.`suppliers` (
  `supplier_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(65) NOT NULL,
  `contact_info` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`supplier_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(65) NOT NULL,
  `last_name` VARCHAR(65) NOT NULL,
  `phone_number` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`parts` (
  `part_id` INT NOT NULL AUTO_INCREMENT,
  `part_name` VARCHAR(128) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `units_in_stock` INT NOT NULL,
  `retail_price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`part_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`delivery_requests` (
  `request_id` INT NOT NULL AUTO_INCREMENT,
  `supplier_id` INT NOT NULL,
  `request_date` DATE NOT NULL,
  `part_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`request_id`),
  INDEX `fk_delivery_requests_supplier_id_idx` (`supplier_id` ASC) VISIBLE,
  INDEX `fk_delivery_requests_part_id_idx` (`part_id` ASC) VISIBLE,
  CONSTRAINT `fk_delivery_requests_supplier_id`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `lab1`.`suppliers` (`supplier_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_delivery_requests_part_id`
    FOREIGN KEY (`part_id`)
    REFERENCES `lab1`.`parts` (`part_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`deliveries` (
  `delivery_id` INT NOT NULL AUTO_INCREMENT,
  `delivery_date` DATE NOT NULL,
  PRIMARY KEY (`delivery_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`delivery_details` (
  `delivery_id` INT NOT NULL,
  `request_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `selling_price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`delivery_id`, `request_id`),
  INDEX `fk_delivery_details_request_id_idx` (`request_id` ASC) VISIBLE,
  CONSTRAINT `fk_delivery_details_delivery_id`
    FOREIGN KEY (`delivery_id`)
    REFERENCES `lab1`.`deliveries` (`delivery_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_delivery_details_request_id`
    FOREIGN KEY (`request_id`)
    REFERENCES `lab1`.`delivery_requests` (`request_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`sales` (
  `sale_id` INT NOT NULL AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `sale_date` DATE NOT NULL,
  PRIMARY KEY (`sale_id`),
  CONSTRAINT `fk_sales_customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `lab1`.`customers` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lab1`.`sale_details` (
  `sale_id` INT NOT NULL,
  `part_id` INT NOT NULL,
  `retail_price` DECIMAL(10,2) NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`sale_id`, `part_id`),
  INDEX `fk_sale_details_part_id_idx` (`part_id` ASC) VISIBLE,
  CONSTRAINT `fk_sale_details_sale_id`
    FOREIGN KEY (`sale_id`)
    REFERENCES `lab1`.`sales` (`sale_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_sale_details_part_id`
    FOREIGN KEY (`part_id`)
    REFERENCES `lab1`.`parts` (`part_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;