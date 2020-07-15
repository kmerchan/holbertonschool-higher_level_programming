-- lists all shows of genre 'Comedy'
-- display as tv_shows.title
SELECT tv.title
       FROM tv_show_genres AS tvg
       INNER JOIN tv_shows AS tv
       ON tvg.show_id = tv.id
       INNER JOIN tv_genres AS g
       ON g.id = tvg.genre_id
       WHERE g.name = "Comedy"
       ORDER BY tv.title ASC;
