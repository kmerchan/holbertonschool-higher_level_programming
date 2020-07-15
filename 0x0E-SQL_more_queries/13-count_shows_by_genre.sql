-- lists all genres and count of number of shows linked to that genre
-- display as tv_genres.name-count of tv shows linked to that genre
SELECT g.name AS genre, COUNT(t.show_id) AS number_of_shows
       FROM tv_genres AS g
       LEFT JOIN tv_show_genres AS t
       ON g.id = t.genre_id
       GROUP BY g.id
       ORDER BY number_of_shows DESC;
