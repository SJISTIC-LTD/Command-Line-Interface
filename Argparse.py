import click
import requests

__author__ = "Oyetoke Toby"

@click.group()
def main():
    """
    Simple CLI for querying books on Google Books by Oyetoke Toby
    """
    pass

@main.command()
@click.argument('query')
def search(query):
    """This search and return results corresponding to the given query from Google Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes'
    query = "+".join(query.split())

    query_params = {
        'q': query
    }

    response = requests.get(url_format, params=query_params)

    click.echo(response.json()['items']) 

@main.command()
@click.argument('id')
def get(id):
    """This return a particular book from the given id on Google Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    click.echo(id)

    response = requests.get(url_format.format(id))

    click.echo(response.json())


if __name__ == "__main__":
    main()
    """HELLO CLI
Usage:
    hello.py
    hello.py <name>
    hello.py -h|--help
    hello.py -v|--version
Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -v --version  Show version.
"""

from docopt import docopt

def say_hello(name):
    return("Hello {}!".format(name))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')
    if arguments['<name>']:
        print(say_hello(arguments['<name>']))
    else:
        print(arguments)
        from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
     }
]
answers = prompt(questions)
pprint(answers)
from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [
            Separator('= The Meats ='),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= The Cheeses ='),
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            Separator('= The usual ='),
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
pprint(answers)
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


print('Hi, welcome to Python Pizza')

questions = [
    {
        'type': 'confirm',
        'name': 'toBeDelivered',
        'message': 'Is this for delivery?',
        'default': False
    },
    {
        'type': 'input',
        'name': 'phone',
        'message': 'What\'s your phone number?',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'list',
        'name': 'size',
        'message': 'What size do you need?',
        'choices': ['Large', 'Medium', 'Small'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'quantity',
        'message': 'How many do you need?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'expand',
        'name': 'toppings',
        'message': 'What about the toppings?',
        'choices': [
            {
                'key': 'p',
                'name': 'Pepperoni and cheese',
                'value': 'PepperoniCheese'
            },
            {
                'key': 'a',
                'name': 'All dressed',
                'value': 'alldressed'
            },
            {
                'key': 'w',
                'name': 'Hawaiian',
                'value': 'hawaiian'
            }
        ]
    },
    {
        'type': 'rawlist',
        'name': 'beverage',
        'message': 'You also get a free 2L beverage',
        'choices': ['Pepsi', '7up', 'Coke']
    },
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your purchase experience?',
        'default': 'Nope, all good!'
    },
    {
        'type': 'list',
        'name': 'prize',
        'message': 'For leaving a comment, you get a freebie',
        'choices': ['cake', 'fries'],
        'when': lambda answers: answers['comments'] != 'Nope, all good!'
    }
]

answers = prompt(questions, style=style)
print('Order receipt:')
pprint(answers)
