# Import the BaseHandler:

from cursepy.handlers.base import BaseHandler

# Create a simple handler:

class DummyHand(BaseHandler):

    def __init__(self):

        # Set our name:

        super().__init__(name='DummyHand')

    def start(self):

        # Start this handler, somehow:

        print("Handler is started!")

    def stop(self):

        # Stop this handler, somehow:

        print("Handler is stopped!")