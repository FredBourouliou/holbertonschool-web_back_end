-- Task: Create an index on the first letter of the name column
-- Index idx_name_first on table names for first letter of name
CREATE INDEX idx_name_first ON names (name(1));
