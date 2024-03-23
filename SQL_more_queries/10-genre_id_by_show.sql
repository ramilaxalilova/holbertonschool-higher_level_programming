-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres 
	LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
