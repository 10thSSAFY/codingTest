SELECT
    user_id,
    product_id
FROM
    online_sale
GROUP BY
    user_id, product_id
    having count(product_id) > 1
ORDER BY
    user_id, product_id desc;