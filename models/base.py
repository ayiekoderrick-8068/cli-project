# This is the base class that all my models inherit from.
# It makes sure every model has a to_dict method.

class BaseModel:

    def to_dict(self):
        raise NotImplementedError("Every model needs its own to_dict method")
