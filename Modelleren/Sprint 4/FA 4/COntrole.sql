select sum(aantal) aantal
from aankoop, transactie
where product = 1 and datum < '2020-01-01'and datum > '2019-11-30'