-- lists all genres of the show Dexter
SELECT g.name FROM tv_shows s
	LEFT JOIN tv_show_genres tg ON s.id = tg.show_id
	LEFT JOIN tv_genres g ON g.id = tg.genre_id
	WHERE s.title = 'Dexter'
	ORDER BY g.name;
