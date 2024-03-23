-- lists all cities
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities LEFT JOIN states ON state_id = states.id;
