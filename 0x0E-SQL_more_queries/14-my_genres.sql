-- lists all genres of tv show 'Dexter'
-- display as tv_genres.name
SELECT g.`name` FROM `tv_genres` AS g INNER JOIN `tv_shows_genre` AS tvg ON g.`id` = tvg.`genre_id` INNER JOIN `tv_shows` AS tv ON tvg.`show_id` = tv.`id` ORDER BY g.`name` ASC;
