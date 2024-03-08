create database Ecommerce;

use Ecommerce;

create table customer(
	customer_id int auto_increment primary key,
    name varchar(255),
    email varchar(255) unique,
    password varchar(255)
);

create table products(
	product_id int auto_increment primary key,
    name varchar(255),
    price decimal(8,2),
    description text,
    stockQuantity int
);

create table cart(
	cart_id int auto_increment primary key,
    customer_id int,
    product_id int,
    quantity int,
    foreign key (customer_id) references customer(customer_id) on delete cascade,
    foreign key (product_id) references products(product_id) on delete cascade
);

create table orders(
	order_id int auto_increment primary key,
    customer_id int,
    order_date date,
    total_price decimal(15,2),
    street varchar(25),
    city varchar(25),
    state varchar(25),
    pincode varchar(25),
    foreign key (customer_id) references customer(customer_id) on delete cascade
);

create table order_items(
	order_item_id int auto_increment primary key,
    order_id int,
    product_id int,
    quantity int,
    foreign key (order_id) references orders(order_id) on delete cascade,
    foreign key (product_id) references products(product_id) on delete cascade
);
