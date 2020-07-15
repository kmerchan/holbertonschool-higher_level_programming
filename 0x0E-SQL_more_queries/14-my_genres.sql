-- lists all genres of tv show 'Dexter'
-- display as tv_genres.name
SELECT g.name
       FROM tv_show_genres AS tvg
       INNER JOIN tv_shows AS tv
       ON tvg.show_id = tv.id
       INNER JOIN tv_genres AS g
       ON g.id = tvg.genre_id
       WHERE tv.title = "Dexter"
       ORDER BY g.name ASC;
