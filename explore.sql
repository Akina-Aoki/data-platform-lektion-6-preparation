/* Explore the market_table 
*/

-- Scale
SELECT COUNT(*) FROM market_table;
-- 121,343

-- Look at ONE row, never expore JSON at scale first
SELECT jsonb_pretty(raw_market_data)
FROM market_table
LIMIT 1;
-- Result in market_table_structure.md

SELECT raw_market_data['occupation_field'][0]['label'] FROM public.market_table;