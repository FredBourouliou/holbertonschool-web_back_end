-- Task: Create a trigger that decreases item quantity after adding a new order
-- Trigger fires after INSERT on orders table
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
