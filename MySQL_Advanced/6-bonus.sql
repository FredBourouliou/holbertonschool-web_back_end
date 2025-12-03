-- Task: Create a stored procedure AddBonus to add a correction for a student
-- Creates project if it doesn't exist, then adds the correction
DELIMITER //
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check if project exists, if not create it
    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Get the project id
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
