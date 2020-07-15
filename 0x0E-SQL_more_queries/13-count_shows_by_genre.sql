-- lists all genres and count of number of shows linked to that genre
-- display as tv_genres.name-count of tv shows linked to that genre
SELECT g.`name`, COUNT(*) AS number FROM `tv_shows` AS s INNER JOIN `tv_show_genres` AS sg ON g.`id` = sg.`genre_id` GROUP BY WHERE g.`show_id` IS NULL ORDER BY s.`title` ASC;
