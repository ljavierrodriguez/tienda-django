-- SQLite
-- SELECT * FROM table_name (WHERE condition); (WHERE = optional)
SELECT id, name, description, is_active, created_at, updated_at
FROM categories;

SELECT id, name FROM categories WHERE is_active=1;

SELECT * FROM auth_user WHERE username='lrodriguez';

-- INSERT INTO table_name (field1, field2, ....) VALUES (value1, value2, ...) ;

INSERT INTO categories (name, description, is_active, created_at, updated_at) 
VALUES ('Deportes', 'Categoria para los productos deportivos', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- UPDATE table_name SET field1=value1, field2=value2, ... WHERE condition;

UPDATE auth_user SET first_name='Luis J.', last_name='Rodriguez' WHERE id=1;

-- DELETE FROM table_name WHERE condition; 
DELETE FROM categories WHERE id > 3;