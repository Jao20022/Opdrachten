select bonuskaartnummer, filiaal.filiaalnummer, filiaal.adres, filiaal.plaats, transactie.datum from filiaal, transactie
where bonuskaartnummer = 65472335;

select sum(distinct(product.prijs * aankoop.aantal)) as totaalprijs
from product, aankoop, bonuskaart
where bonuskaartnummer = 65472335 and product.productnummer = aankoop.product

select sum(aantal) aantal
from aankoop
where product = 1