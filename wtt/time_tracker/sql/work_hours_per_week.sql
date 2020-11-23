SELECT date_trunc('week', start_at::date) AS weekly, SUM(duration_in_minutes) / 60 AS hours           
FROM time_tracker_entry
GROUP BY weekly
ORDER BY weekly;