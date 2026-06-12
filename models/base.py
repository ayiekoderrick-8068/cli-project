

class BaseModel:

    def to_dict(self):
        raise NotImplementedError("Every model needs its own to_dict method")
