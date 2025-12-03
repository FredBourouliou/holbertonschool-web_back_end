-- Task: Create a function SafeDiv that safely divides two numbers
-- Returns a / b or 0 if b is 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END //
DELIMITER ;
