-- ists all genres from hbtn_0d_tvshows and displays number of shows
SELECT g.name genre, COUNT(g.id) number_of_shows FROM tv_genres g
	INNER JOIN tv_show_genres tg ON g.id = tg.genre_id
	GROUP BY (genre)
	ORDER BY number_of_shows DESC;
