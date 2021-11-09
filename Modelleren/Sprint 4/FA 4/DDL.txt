create database AH; 

create table bonuskaart (
 bonuskaartnummer integer,
 naam varchar(255) NULL,
 adres varchar(255) NULL,
 woonplaats varchar(255) NULL,
 primary key(bonuskaartnummer));

 create table filiaal (
 filiaalnummer integer,
 plaats varchar(255),
 adres varchar(255),
 primary key(filiaalnummer));

 create table product (
 	productnummer integer,
 	omschrijving varchar(255),
 	prijs decimal(6,2),
 	primary key(productnummer));

 create table transactie (
 	transactienummer integer,
 	datum date,
 	tijd time,
 	bonuskaartnummer integer,
 	filiaalnummer integer,
 	primary key(transactienummer),
 	foreign key (bonuskaartnummer) references bonuskaart(bonuskaartnummer),
 	foreign key (filiaalnummer) references filiaal(filiaalnummer));

 create table aankoop(
 	transactienummer integer,
 	product integer,
 	aantal integer,
 	foreign key (transactienummer) references transactie(transactienummer),
 	foreign key (product) references product(productnummer),
	primary key (transactienummer, product));


INSERT INTO bonuskaart (bonuskaartnummer)
Values (65472335);

INSERT INTO bonuskaart (bonuskaartnummer, naam, adres, woonplaats)
Values (12345678, 'Annette', 'Vredenburg 12', 'Utrecht');

INSERT INTO filiaal (filiaalnummer, plaats, adres)
Values (35, 'Utrecht', 'Stationsplein');

INSERT INTO filiaal (filiaalnummer, plaats, adres)
Values (48, 'Utrecht', 'Roelantdreef 41');


INSERT INTO product (productnummer, omschrijving, prijs)
Values (1, 'AH halfvolle melk', 0.99);

INSERT INTO product (productnummer, omschrijving, prijs)
Values (2, 'AH pindakaas', 2.39);


INSERT INTO product (productnummer, omschrijving, prijs)
Values (3, 'tandelborstel', 1.35);


INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
Values (1, '2019-12-01', '17:35', 65472335, 35);

INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
Values (2, '2019-12-03', '12:25', 65472335, 48);

INSERT INTO transactie (transactienummer, datum, tijd, bonuskaartnummer, filiaalnummer)
Values (3, '2019-12-1', '08:30', 12345678, 35);

insert into aankoop (transactienummer, product, aantal)
values (1, 1, 2);

insert into aankoop (transactienummer, product, aantal)
values (1, 2, 1);

insert into aankoop (transactienummer, product, aantal)
values (1, 3, 1);


insert into aankoop (transactienummer, product, aantal)
values (2, 1, 1);


insert into aankoop (transactienummer, product, aantal)
values (3, 1, 2);
