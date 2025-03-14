USE s6_db_l2;

ALTER TABLE delivery_requests ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE delivery_requests ADD FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE delivery_details ADD FOREIGN KEY (delivery_id) REFERENCES deliveries(delivery_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE delivery_details ADD FOREIGN KEY (request_id) REFERENCES delivery_requests(request_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE sales ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

ALTER TABLE sale_details ADD FOREIGN KEY (sale_id) REFERENCES sales(sale_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE sale_details ADD FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE ON UPDATE CASCADE;