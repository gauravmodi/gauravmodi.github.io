Title: One Query To Rule Them All
Date: 2018-06-19 22:57
Category: SQL
Tags: sql, window functions, datetime functions,
Slug: one-sql-query-to-all-them-all
Authors: Gaurav Modi
<p>
<p><b><h3>This is one query where I have put all frequently used SQL functions so to reference the syntax whenever required.</b></h3>
<p><i><b><font color='red'>NOTE: This query as whole is gibberish.</font></b></i></p>

``` mysql
WITH
    cte_table AS
    (
        SELECT *
          FROM table
    ),

    cte_derived AS
    (
        SELECT *
          FROM cte_table
    )

SELECT COUNT(DISTINCT artist),

       -- DATA TYPE CASTING
       CAST(sales AS DECIMAL(28, 3)) AS sale, -- sales with 3 decimal precisions
                                              -- and maximum 28 digits
       founded_at_clean::TIMESTAMP,

       -- CASE STATEMENT (IF-ELSE)
       CASE WHEN weight > 250 THEN 'over 250'
            ELSE '175 or under' END AS weight_group,
       SUM(CASE WHEN full_school_name < 'n' THEN 1 END) AS a_m,

       -- STRING MANIPULATION
       LEFT(date, 10) AS cleaned_date,
       SUBSTR(date, 4, 2) AS day, --substring from 4 places to 2 next positions
       TRIM(BOTH '()@$' FROM location), -- replaces all the characters inside
                                        -- the TRIM from 'BOTH' side left and right
       POSITION('A' IN descript) AS a_position, -- tells the position of 'A' in column value
       CONCAT(day_of_week, ', ', LEFT(date, 10)) AS day_and_date,
       UPPER(address) AS address_upper,
       LOWER(address) AS address_lower,

       -- DATETIME FUNCTIONS
       CURRENT_DATE AS date,
       CURRENT_TIME AS time,
       CURRENT_TIMESTAMP AS timestamp,
       CURRENT_TIME AT TIME ZONE 'PST' AS time_pst,
       LOCALTIME AS localtime,
       LOCALTIMESTAMP AS localtimestamp,
       NOW() AS time_now,

       -- DATE MANIPULATION FUNCTIONS
       founded_at_clean::TIMESTAMP + INTERVAL '1 week' AS plus_one_week,
       NOW() - founded_at_clean::TIMESTAMP AS founded_time_ago, -- current time - some_value

       -- TIME EXTRACTION FUNCTIONS
       EXTRACT('month' FROM transaction_date::TIMESTAMP) AS week,
       DATE_TRUNC('week', transaction_date::DATE) AS week,

       -- WINDOW FUNCTIONS: AVG, COUNT, RANK, DENSE_RANK, ROW_NUMBER, LAG, LEAD
       LAG(sales, 2) OVER () AS sales_last_week, --2nd lag value of
       RANK() OVER (PARTITION BY locationID ORDER BY quantity DESC) AS Rank,
       SUM(sales) OVER (ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS total_sales_moving_avg_7_days,
       SUM(sales) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_sales,
       SUM(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time) AS running_total,
       SUM(sales) OVER (ORDER BY week) AS running_total_V2 --make sure to have order by,
       NTILE(4) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS quartile
  FROM lag_sales AS w
  LEFT JOIN tutorial.crunchbase_acquisitions acquisitions
    ON companies.permalink = acquisitions.company_permalink
   AND companies.name = investments.company_name
   AND investments.funded_year > companies.founded_year + 5
 WHERE "group" LIKE 'Snoop%'
   AND artist ILIKE 'dr_ke' -- underscore is to match with any character
                            -- and ILIKE is CASE INsensitive
   AND artist NOT IN ('Taylor Swift', 'Usher', 'Ludacris')
   AND year_rank BETWEEN 5 AND 10 -- both extreme values included
    OR artist IS NULL
 GROUP BY 1  -- Group by first column in SELECT statement
 ORDER BY 1 DESC
OFFSET 1     -- Exclude the first row
 LIMIT 1;
```
