-- lists all shows and all genres linked that show
SELECT s.title title, g.name name FROM tv_shows s
	LEFT JOIN tv_show_genres tg ON s.id = tg.show_id 
	LEFT JOIN tv_genres g ON tg.genre_id = g.id
	ORDER BY title, name
