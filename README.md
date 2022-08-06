# Python-Handler-Guide
A guide for the usage of Python Handlers. Include the use of collections and example code of handlers.
This will contain and provide analogies that connect with the uses of Python Handlers and it will also contain examples for having as a guide.

## Handlers

In short words: Handlers are functions that 'handle' certain events that they are designated for / registered for.

Handlers are often used to replace polling. Polling is a technique where the program is checking the state of something frequently to react when the state has changed. Staying with the keyboard example. Imagine you are steering a player in a game through a 2D world with your arrow keys. How does the program know which direction you want to go? It needs to check which (if any) of the arrow keys are pressed. For that, it could get the state of the keyboard, check if e.g. the right arrow key is currently pressed and then move the player a bit to the right if that is the case. But the program will only know about this change once it has checked the keyboard. So to be responsive for the player it has to check the state of the keyboard quite often (a couple of times per second) which wastes CPU cycles as most of the time the state has indeed not changed.

Now turning the model around, the game could ask the keyboard: Hey, when a key is pressed, call this function and tell it which keys are pressed. The function can then accordingly update the players position - but is only called when the state of the keyboard has changed. Polling is like calling the pizza guy every five minutes: "Is my order ready for pickup?" as opposed to calling him once and telling him "Call me back when my order is ready." In the latter case you 'registered a handler for pizza-ready events' and saved both of you a lot of time.