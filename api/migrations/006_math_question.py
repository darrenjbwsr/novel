steps = [
    [
        """
        CREATE TABLE math_questions(
            id SERIAL PRIMARY KEY NOT NULL,
            question VARCHAR(1000) NOT NULL,
            answer VARCHAR(1000) NOT NULL
        )
        """,
        """
        DROP TABLE math_questions;
        """
    ]
]
