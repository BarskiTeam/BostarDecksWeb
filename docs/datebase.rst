DOCS
####

TABLES
******

User
=====

Deck
=====

* **name**: string
* **description**: string
* **deckFlashcard**: FK
* **owner**: FK
* **public**: boolean
* **tag**: string

DeckFlashcard
=============

* **deck**: FK
* **flashcard**: FK
* **level**: FK
* **good_answers**: int
* **bad_answers**: int


Flashcard
==========

* **name**: string
* **averse**: string
* **reverse**: string
* **tip**: string
* **owner**: FK
.. this is useable for Kusofc - if i wont able to remember word i can activate show a tips for a word

* **tag**: list<string>


Level
=====
* **name**: string
* **repeat_frequency**: int # time in seconds
.. int # time in seconds --> destination should be day
  #Warning we shouldn't used "-" in name of attributes of models - It isn't accept by django models

