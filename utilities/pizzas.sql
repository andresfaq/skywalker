
INSERT INTO tenant.baseapp_pizzabase (id, name, description, image) VALUES (1, 'Pepperoni', 'pepperoni...', 'upload/pepperoni.png');
INSERT INTO tenant.baseapp_pizzabase (id, name, description, image) VALUES (2, 'Hawaina', 'Hawaina', 'upload/pepperoni.png');
INSERT INTO tenant.baseapp_pizzabase (id, name, description, image) VALUES (3, 'Pollo y Champiñones', 'Pollo y Champiñones', 'upload/pepperoni.png');
INSERT INTO tenant.baseapp_pizzabase (id, name, description, image) VALUES (4, 'Colombiana ', 'Colombiana...', 'upload/pepperoni.png');
INSERT INTO tenant.baseapp_pizzabase (id, name, description, image) VALUES (5, 'Mexicana', 'Mexicana', 'upload/pepperoni.png');

INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (1, 16500, 'SM', 1);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (2, 22600, 'ME', 1);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (3, 28600, 'LG', 1);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (4, 32600, 'XL', 1);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (5, 16500, 'SM', 2);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (6, 22600, 'ME', 2);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (7, 28600, 'LG', 2);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (8, 32600, 'XL', 2);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (9, 16500, 'SM', 3);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (10, 22600, 'ME', 3);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (11, 28600, 'LG', 3);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (12, 32600, 'XL', 3);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (13, 16500, 'SM', 4);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (14, 22600, 'ME', 4);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (15, 28600, 'LG', 4);
INSERT INTO tenant.baseapp_pizza (id, price, size, pizza_base_id) VALUES (16, 32600, 'XL', 4);

INSERT INTO tenant.baseapp_pizzabase_aditions (id, pizzabase_id, ingredient_id) VALUES (1, 1, 1);

