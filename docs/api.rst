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


Get flashCards
**************
EXAMPLE:
`</api/v1/flashCard/1/>`_

GET:

Response:

.. code-block:: json

    {
        "flashCard": [
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
