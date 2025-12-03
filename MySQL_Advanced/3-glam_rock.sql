-- Task: List all Glam rock bands ranked by their longevity
-- Lifespan computed using formed and split attributes (until 2024 if not split)
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
