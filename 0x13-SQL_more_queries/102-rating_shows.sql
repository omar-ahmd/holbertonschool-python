-- List shows sorted by their rating from hbtn_0d_tvshows_rate 
   SELECT title,
          SUM(rate) AS rating
     FROM tv_shows
LEFT JOIN tv_show_ratings
       ON tv_shows.id = tv_show_ratings.show_id
 GROUP BY title
 ORDER BY rating DESC;
