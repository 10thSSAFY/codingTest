SELECT
    flavor
FROM
    first_half JOIN icecream_info USING (flavor)
WHERE
    total_order > 3000
    AND ingredient_type = 'fruit_based'
ORDER BY
    total_order DESC;