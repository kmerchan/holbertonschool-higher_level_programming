-- lists all TV show titles and linked genre names
-- display as tv_shows.title - tv_genres.name
SELECT tv.title, g.name
       FROM tv_show_genres AS tvg
       LEFT JOIN tv_shows AS tv
       ON tvg.show_id = tv.id
       LEFT JOIN tv_genres AS g
       ON g.id = tvg.genre_id
       ORDER BY tv.title, g.name ASC;
