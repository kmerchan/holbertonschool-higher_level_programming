-- lists all shows in current database, where there is no linked genre id
-- display as tv_shows.title-NULL
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id` WHERE g.`show_id` IS NULL ORDER BY s.`title` ASC;
