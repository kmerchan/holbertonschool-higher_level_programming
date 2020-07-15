-- lists all shows in current database, including those missing linked genre id
-- display as tv_shows.title-tv_shows_genres.genre_id or NULL
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id` ORDER BY s.`title`, g.`genre_id` ASC;
