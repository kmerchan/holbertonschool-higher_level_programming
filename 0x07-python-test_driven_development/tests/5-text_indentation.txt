============================
doctest for 5-text_indentation.py
============================
``text_indentation()`` prints text with two newlines after '.' '?' or ':'

TEST CONDITIONS
===============

testing printing string with various '.' '?' and ':'
::
>>> text_indentation = __import__('5-text_indentation').text_indentation
>>> text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
... Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
... Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
... Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
... Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
... rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
... stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
... cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
... beatiorem! Iam ruinas videres""")
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
<BLANKLINE>
Quonam modo?
<BLANKLINE>
Utrum igitur tibi litteram videor an totas paginas commovere?
<BLANKLINE>
Non autem hoc:
<BLANKLINE>
igitur ne illud quidem.
<BLANKLINE>
Fortasse id optimum, sed ubi illud:
<BLANKLINE>
Plus semper voluptatis?
<BLANKLINE>
Teneo, inquit, finem illi videri nihil dolere.
<BLANKLINE>
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
<BLANKLINE>
Si id dicis, vicimus.
<BLANKLINE>
Inde sermone vario sex illa a Dipylo stadia confecimus.
<BLANKLINE>
Sin aliud quid voles, postea.
<BLANKLINE>
Quae animi affectio suum cuique tribuens atque hanc, quam dico.
<BLANKLINE>
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

testing printing text with '.' '?' and ':', some without trailing whitespace
::
>>> text_indentation("""This is a test string with : in the middle of wo:rd. \
... Isn't it crazy? What if we have a ? in the middle of this wo?rd? Wild!""")
This is a test string with :
<BLANKLINE>
in the middle of wo:
<BLANKLINE>
rd.
<BLANKLINE>
Isn't it crazy?
<BLANKLINE>
What if we have a ?
<BLANKLINE>
in the middle of this wo?
<BLANKLINE>
rd?
<BLANKLINE>
Wild!

testing printing text with '.' '?' and ':', some with multiple trailing spaces
::
>>> text_indentation("""This is a test string with :                          \
... in the middle of wo:rd.                                          \
... Isn't it crazy?                        \
... What if we have a ?                                  \
... in the middle of this wo?                rd?                       Wild!""")
This is a test string with :
<BLANKLINE>
in the middle of wo:
<BLANKLINE>
rd.
<BLANKLINE>
Isn't it crazy?
<BLANKLINE>
What if we have a ?
<BLANKLINE>
in the middle of this wo?
<BLANKLINE>
rd?
<BLANKLINE>
Wild!

testing printing text with leading whitespace
::
>>> text_indentation("""     This is a test string with : in the middle \
... of wo:rd. \
... Isn't it crazy? What if we have a ? in the middle of this wo?rd? Wild!""")
This is a test string with :
<BLANKLINE>
in the middle of wo:
<BLANKLINE>
rd.
<BLANKLINE>
Isn't it crazy?
<BLANKLINE>
What if we have a ?
<BLANKLINE>
in the middle of this wo?
<BLANKLINE>
rd?
<BLANKLINE>
Wild!

testing string without the specific characters
::
>>> text_indentation("This string has no special indentation characters!")
This string has no special indentation characters!

testing string with the specific characters back-to-back
::
>>> text_indentation("This string has all the characters .?:!")
This string has all the characters .
<BLANKLINE>
?
<BLANKLINE>
:
<BLANKLINE>
!

testing empty string argument
::
>>> text_indentation("")


testing None argument
::
>>> text_indentation(None)
Traceback (most recent call last):
TypeError: text must be a string

testing boolean argument
::
>>> text_indentation(True)
Traceback (most recent call last):
TypeError: text must be a string

testing argument of incorrect type (list of strings)
::
>>> text_indentation(["This", "list", "has", ".", "?", "and", ":"])
Traceback (most recent call last):
TypeError: text must be a string

testing argument of incorrect type (tuple)
::
>>> text_indentation((1, 2.2, 3))
Traceback (most recent call last):
TypeError: text must be a string

testing argument of incorrect type (float)
::
>>> text_indentation(1.234)
Traceback (most recent call last):
TypeError: text must be a string
