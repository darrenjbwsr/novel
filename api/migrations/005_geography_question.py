steps = [
    [
        """
        CREATE TABLE geography_questions(
            id SERIAL PRIMARY KEY NOT NULL,
            question VARCHAR(1000) NOT NULL,
            answer VARCHAR(1000) NOT NULL,
            picture VARCHAR(300) NOT NULL
        )
        """,
        """
        DROP TABLE geography_questions;
        """
    ]
]
