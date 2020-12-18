API
###

Get decks
*********
`</api/v1/deck>`_ 

GET:

Response:

.. code-block:: json

    {
        "deck": [
            {
                "name": "string",
                "description": "string",
                "tag": "string"
            }
        ],
        "auth_field": "string"
    }


Get flashcards
**************
`</api/v1/flashcard/deck/\<deck:id\>>`_ 

GET:

Response:

.. code-block:: json

    {
        "flashcard": [
            {
                "name": "string",
                "reverse": "string",
                "avers": "string",
                "tip": "string",
                "tag": "string",
                "level": "string",
                "deck_id": "int"
            }
        ],
        "auth_field": "string"
    }


Get flashcards from one deck
****************************
EXAMPLE:
`</api/v1/deck/1/flashcards/>`_

GET:

Response:

.. code-block:: json

    {
        {
            "id": 1,
            "name": "otázka",
            "reverse": "problem",
            "averse": "otázka",
            "tip": "taser sprawia duża problemów",
            "deck": [
                1
            ]
        }
    }
