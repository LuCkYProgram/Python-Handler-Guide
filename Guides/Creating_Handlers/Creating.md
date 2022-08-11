# Creating A Handler

Every handler is essentially a class that does something. Simple as that.

All handlers MUST inherit ‘BaseHandler’! If you attempt to load an object that does not inherit ‘BaseHandler’, then an exception will be raised!

This is the one and only restriction to handlers. The reason why this is the case is because cursepy must guarantee that a ‘handel()’ method is present on the object to load (You will find out why this is later). It is also important for the HandlerCollection(HC), as it will assign some values in the object, and cursepy does not want weird errors to occur.