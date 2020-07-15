-- lists all shows in current database that have at least one genre linked
-- display as tv_shows.title-tv_shows_genres.genre_id
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s INNER JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id` ORDER BY s.`title`, g.`genre_id` ASC;
