-- lists all the cities in current database, sorted by cities.id in ascending order
-- displayed as [cities.id]-[cities.name]-[state.name]
SELECT c.`id`, c.`name`, s.`name` FROM `cities` c FULL OUTER JOIN `states` s ON c.`state_id` = s.`id` ORDERED BY c.`id` ASC;
