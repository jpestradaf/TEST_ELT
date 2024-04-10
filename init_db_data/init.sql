create table client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(30),
    address VARCHAR(50),
    invoi_client INTEGER
    --PRIMARY KEY (id),
   -- KEY invoi_client_fk (invoi_client),
   -- CONSTRAINT invoi_client_fk FOREIGN KEY (invoi_client) REFERENCES invoice (id)
);

insert into client (
    name, email, phone, address, invoi_client
) values ('wade lewis', 'wade88@gmail.com', '7609947483', '3803 millbridge dr.', 1),
('dave smith', 'dave05@yahoo.com', '8015295125', '11227 vienna trails ln', 1),
('seth mcallister', 'sethmc99@hotmail.com','2035006370', '3939 synott rd', 1),
('ivan stokes', 'stokesvan78@gmail.com', '6154817037', '1039 street br', 1),
('riley sheeran', 'sheeranley88@hotmail.com', '7608440455', '2000 holly hall st', 1),
('gilbert dunston', 'gilbertd06@gmail.com', '9563254178', '3814 gardenia bend dr', 1),
('frankie moore', 'mooref81@yahoo.com', '3569854712', '10004 timbercreek ct', 1),
('dan griffin', 'dangriffin00@gmail.com', '9785641230', '10226 washington trace rd', 1),
('brian huff', 'brianh2005@hotmail.com', '5035698410', '10541 garibaldi dr', 1),
('robert seewald', 'robert1999@gmail.com', '6056423189', '10632 aspen ave.', 1);