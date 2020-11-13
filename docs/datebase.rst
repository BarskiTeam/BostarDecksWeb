DOCS
####

TABLES
******

User
=====

`<https://www.keycloak.org/>`_

Deck
=====

* **name**: string
* **description**: string
* **deckFlashCard**: FK 
* **tag**: string

DeckFlashCard
=============

* **deck**: FK
* **flashCard**: FK
* **level**: FK 
* **good_answers**: int
* **bad_answers**: int


FlashCard
==========

* **name**: string
* **reverse**: string
* **averse**: string
* **tip**: string
* **tag**: list<string>


Level
=====
* **name**: string
* **repeat_frequency**: int # time in seconds