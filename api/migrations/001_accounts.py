steps = [
    [
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            username VARCHAR(150) NOT NULL,
            password VARCHAR(100) NOT NULL CHECK(LENGTH(password) >= 6)
        );
        """,
        """
        DROP TABLE accounts;
        """,
    ]
]
