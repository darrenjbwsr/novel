steps = [
    [
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL CHECK(LENGTH(password) >= 8),
            is_landlord BOOLEAN DEFAULT false
        );
        """,
        """
        DROP TABLE accounts;
        """,
    ]
]
