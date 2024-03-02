SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS date_of_birth
FROM member_profile
WHERE MONTH(date_of_birth) = 3
  AND gender = 'W'
  AND TLNO IS NOT NULL;