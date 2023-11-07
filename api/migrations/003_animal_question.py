steps = [
    [
        """
        CREATE TABLE animal_questions(
            id SERIAL PRIMARY KEY NOT NULL,
            question STR NOT NULL,
            answer STR NOT NULL,
            picture VARCHAR(300) NOT NULL,
        )
        """,
        """
        DROP TABLE animal_questions;
        """
    ]
]
