steps = [
    [
        """
        CREATE TABLE geography_questions(
            id SERIAL PRIMARY KEY NOT NULL,
            question STR NOT NULL,
            answer STR NOT NULL,
            picture VARCHAR(300) NOT NULL,
        )
        """,
        """
        DROP TABLE geography_questions;
        """
    ]
]