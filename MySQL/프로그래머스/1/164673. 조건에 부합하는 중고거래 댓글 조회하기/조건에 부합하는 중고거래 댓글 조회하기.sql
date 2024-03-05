SELECT
    TITLE,
    board.board_id,
    reply_id,
    reply.writer_id,
    reply.contents,
    DATE_FORMAT(reply.created_date, "%Y-%m-%d") AS created_date
FROM
    used_goods_board AS board,
    used_goods_reply AS reply
WHERE
    board.board_id = reply.board_id
    AND board.created_date LIKE "2022-10%"
ORDER BY
    reply.created_date ASC,
    title ASC;