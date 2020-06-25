create table zips
(
    country varchar(50) not null,
    city varchar(50) not null,
    street varchar(50) not null,
    number smallint not null,
    zip char(7) not null,
    primary key (country, city, street, number)
);

INSERT INTO group3.zips (country, city, street, number, zip) VALUES ('Israel', 'Ariel', 'Nikayon', 10, '1220035');
INSERT INTO group3.zips (country, city, street, number, zip) VALUES ('Israel', 'Beer-Sheva', 'Peretz', 40, '1220034');
INSERT INTO group3.zips (country, city, street, number, zip) VALUES ('Israel', 'Tel-Aviv', 'Arlozarov', 34, '400051');
INSERT INTO group3.zips (country, city, street, number, zip) VALUES ('Israel', 'Tel-Aviv', 'Namir', 225, '3657600');
INSERT INTO group3.zips (country, city, street, number, zip) VALUES ('United Kingdom', 'Bradford', 'The Queen', 2, '9300000');


create table category
(
    category_code tinyint not null primary key,
    category_name varchar(20) not null
);

INSERT INTO group3.category (category_code, category_name) VALUES (1, 'Joke');
INSERT INTO group3.category (category_code, category_name) VALUES (2, 'Spyware');
INSERT INTO group3.category (category_code, category_name) VALUES (3, 'Muggle Magic');
INSERT INTO group3.category (category_code, category_name) VALUES (4, 'Games');


create table customer
(
    email_address  varchar(50) not null primary key,
    user varchar(50) not null,
    password varchar(50) not null,
    first_name varchar(10) not null,
    last_name varchar(20) not null,
    country varchar(50) not null,
    city varchar(50) not null,
    street varchar(50) not null,
    number smallint not null,
    phone_number char(11) null,
    constraint customer_fk
        foreign key (country, city, street, number) references zips (country, city, street, number)
);

INSERT INTO group3.customer (email_address, user, password, first_name, last_name, country, city, street, number, phone_number) VALUES ('abc@gmail.com', 'abc', 'qwerty23', 'Eliezer', 'Ben-Yehuda', 'Israel', 'Tel-Aviv', 'Namir', 225, '054-2234859');
INSERT INTO group3.customer (email_address, user, password, first_name, last_name, country, city, street, number, phone_number) VALUES ('chani@gmail.com', 'chani1', 'brush!', 'chani', 'chaim', 'Israel', 'Ariel', 'Nikayon', 10, '050-3048922');
INSERT INTO group3.customer (email_address, user, password, first_name, last_name, country, city, street, number, phone_number) VALUES ('dadisa@gmail.com', 'shoelord', 'lacesUp', 'adi', 'das', 'Israel', 'Beer-Sheva', 'Peretz', 40, '054-5551010');
INSERT INTO group3.customer (email_address, user, password, first_name, last_name, country, city, street, number, phone_number) VALUES ('israeli@bezeqint.net', 'israeli', '12345678', 'Israel', 'Israeli', 'United Kingdom', 'Bradford', 'The Queen', 2, '076-8726546');
INSERT INTO group3.customer (email_address, user, password, first_name, last_name, country, city, street, number, phone_number) VALUES ('nlodoch@yahoo.com', 'natan', 'noparK', 'natan', 'lodoch', 'Israel', 'Tel-Aviv', 'Arlozarov', 34, '052-1061061');


create table credit
(
    credit_card_number 	char(16) not null primary key,
    expiration_date date not null,
    cvv char(3) not null,
    email_address varchar(50) not null,
    constraint credit_fk
        foreign key (email_address) references customer (email_address)
);

INSERT INTO group3.credit (credit_card_number, expiration_date, cvv, email_address) VALUES ('1001003789', '2024-08-01', '107', 'dadisa@gmail.com');
INSERT INTO group3.credit (credit_card_number, expiration_date, cvv, email_address) VALUES ('1766309298', '2025-01-01', '329', 'chani@gmail.com');
INSERT INTO group3.credit (credit_card_number, expiration_date, cvv, email_address) VALUES ('198459870123', '2023-11-01', '290', 'abc@gmail.com');
INSERT INTO group3.credit (credit_card_number, expiration_date, cvv, email_address) VALUES ('209168993567', '2021-05-01', '312', 'israeli@bezeqint.net');
INSERT INTO group3.credit (credit_card_number, expiration_date, cvv, email_address) VALUES ('9300872899', '2025-07-01', '222', 'nlodoch@yahoo.com');


create table form
(
    application_number 	int auto_increment primary key,
    application_date datetime  not null,
    subject varchar(50) not null,
    content text not null,
    status varchar(50) null,
    email_address varchar(50) not null,
    constraint form_fk
        foreign key (email_address) references customer (email_address)
);

INSERT INTO group3.form (application_number, application_date, subject, content, status, email_address) VALUES (1, '2020-04-01 12:00:00', 'My order didnt ARRIVE!!!', 'Where is my order?', 'done', 'israeli@bezeqint.net');
INSERT INTO group3.form (application_number, application_date, subject, content, status, email_address) VALUES (2, '2020-04-01 12:28:00', 'Sorry!', 'My order just arrived. sorry', 'waiting', 'israeli@bezeqint.net');
INSERT INTO group3.form (application_number, application_date, subject, content, status, email_address) VALUES (3, '2020-05-05 09:00:00', 'Help!', 'This magic is too scary!', 'waiting', 'chani@gmail.com');
INSERT INTO group3.form (application_number, application_date, subject, content, status, email_address) VALUES (4, '2020-06-09 09:00:00', 'Magic not working!', 'Tried to use product. Doesnt work!', 'waiting', 'dadisa@gmail.com');
INSERT INTO group3.form (application_number, application_date, subject, content, status, email_address) VALUES (5, '2020-06-12 09:00:00', 'Your magic ruined my computer!', 'Since buying your product, Ive been getting spam!', 'waiting', 'nlodoch@yahoo.com');


create table `order`
(
    number int not null primary key,
    date_of_order datetime not null,
    email_address varchar(50) not null,
    constraint order_fk
        foreign key (email_address) references customer (email_address)
);

INSERT INTO group3.`order` (number, date_of_order, email_address) VALUES (2, '2020-03-01 10:19:03', 'israeli@bezeqint.net');
INSERT INTO group3.`order` (number, date_of_order, email_address) VALUES (100, '2009-12-11 12:25:00', 'chani@gmail.com');
INSERT INTO group3.`order` (number, date_of_order, email_address) VALUES (32324, '2010-03-02 18:10:30', 'chani@gmail.com');
INSERT INTO group3.`order` (number, date_of_order, email_address) VALUES (1128492, '2001-09-11 11:15:00', 'dadisa@gmail.com');
INSERT INTO group3.`order` (number, date_of_order, email_address) VALUES (1983022, '2020-02-20 20:20:20', 'nlodoch@yahoo.com');


create table product
(
    id int not null primary key,
    name varchar(50) not null,
    price double not null,
    prev_price double,
    description varchar(300) not null,
    img varchar(50) null,
    category_code tinyint not null,
    constraint product_fk
        foreign key (category_code) references category (category_code)
);

INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (100000001, 'Extendable Ears', 14.99, 24.90, 'A piece of string for eavesdropping', 'extendable_ear.jpg', 2);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (190225832, 'No Poo Bottle', 25, 'Name says it all', 'product5.jpg', 1);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (399200019, 'Peruvian Instant Darkness Powder', 35, 'Creates darkness when used, allowing the user to escape', 'Peruvian_Instant_Darkness_Powder.jpg', 1);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (499990012, 'Sticky Trainers', 60.00, 80.00, 'Yellow trainers with suction cups attached to the soles', 'product3.jpg', 1);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (602456888, 'Fever and Reusable Hangman', 10, 'A magical toy version of the traditionally pen-and-paper game hangman', 'product1.jpg', 3);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (100025460, 'Special Girl', 19.90, 29.90, 'Description of the girls product', 'product6.jpg', 3);
INSERT INTO group3.product (id, name, price, prev_price, description, img, category_code) VALUES (222222222, 'Smelly Candle', 2.90, 7.90, 'Description of the Smelly Cansdle', 'product4.jpg', 2);



create table review
(
    review_number tinyint not null primary key,
    date datetime not null,
    `rank` tinyint not null,categorycategory
    `content`  varchar(300) not null,
    email_address varchar(50) not null,
    sku int not null,
    constraint review_fk
        foreign key (email_address) references customer (email_address),
    constraint review_fk2
        foreign key (sku) references product (id)
);

INSERT INTO group3.review (review_number, date, `rank`, `content`, email_address, sku) VALUES (1, '2011-09-11 11:15:00', 5, 'My son was happy to get this product, the quality of it is more than expected :)', 'dadisa@gmail.com', 602456888);
INSERT INTO group3.review (review_number, date, `rank`, `content`, email_address, sku) VALUES (2, '2009-12-11 12:25:00', 5, 'HAHA thank you! it was just as i imagined!', 'chani@gmail.com', 399200019);
INSERT INTO group3.review (review_number, date, `rank`, `content`, email_address, sku) VALUES (7, '2001-09-11 10:19:00', 5, 'great product!', 'chani@gmail.com', 602456888);
INSERT INTO group3.review (review_number, date, `rank`, `content`, email_address, sku) VALUES (21, '2010-03-02 18:10:00', 4, 'the size is a bit smaller than we thought', 'abc@gmail.com', 499990012);
INSERT INTO group3.review (review_number, date, `rank`, `content`, email_address, sku) VALUES (102, '2019-03-01 16:15:40', 5, 'Good product, I got the delivery very fast!', 'nlodoch@yahoo.com', 100000001);


create table include
(
    quantity tinyint not null,
    number int not null,
    sku int not null,
    primary key (sku, number),
    constraint include_fk
        foreign key (number) references `order` (number),
    constraint include_fk2
        foreign key (sku) references product (id)
);

INSERT INTO group3.include (quantity, number, sku) VALUES (1, 1983022, 100000001);
INSERT INTO group3.include (quantity, number, sku) VALUES (1, 100, 399200019);
INSERT INTO group3.include (quantity, number, sku) VALUES (1, 2, 499990012);
INSERT INTO group3.include (quantity, number, sku) VALUES (2, 32324, 602456888);
INSERT INTO group3.include (quantity, number, sku) VALUES (1, 1128492, 602456888);

