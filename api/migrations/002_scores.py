steps = [
    [
        """
        CREATE TABLE scores(
            id SERIAL PRIMARY KEY NOT NULL,
            user_id INT REFERENCES accounts(id) ON DELETE CASCADE,
            value INT NOT NULL,
            created_on DATE NOT NULL
        )
        """,
        """
        DROP TABLE scores;
        """
    ]
]
