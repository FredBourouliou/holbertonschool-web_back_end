-- Task: Create a trigger that resets valid_email only when email has changed
-- Trigger fires before UPDATE on users table
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //
DELIMITER ;
