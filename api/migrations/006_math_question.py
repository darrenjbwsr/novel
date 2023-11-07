steps = [
    [
        """
        CREATE TABLE math_questions(
            id SERIAL PRIMARY KEY NOT NULL,
            question STR NOT NULL,
            answer STR NOT NULL,
        )
        """,
        """
        DROP TABLE math_questions;
        """
    ]
]
