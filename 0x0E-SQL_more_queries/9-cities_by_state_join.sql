-- lists all the cities in current database, sorted by cities.id in ascending order
-- displayed as [cities.id]-[cities.name]-[state.name]
SELECT c.`id`, c.`name`, s.`name` FROM `cities` AS c INNER JOIN `states` AS s ON c.`state_id` = s.`id` ORDER BY c.`id` ASC;
