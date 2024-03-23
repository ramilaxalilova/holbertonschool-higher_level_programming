-- lists all comedy shows
SELECT s.title title FROM tv_genres g
	LEFT JOIN tv_show_genres tg ON g.id = tg.genre_id
	LEFT JOIN tv_shows s ON tg.show_id = s.id
	WHERE g.name = 'Comedy'
	ORDER BY s.title;
