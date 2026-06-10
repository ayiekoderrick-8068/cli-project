class BaseModel:
    # every model must implement to_dict
    def to_dict(self):
        raise NotImplementedError("to_dict() must be implemented by subclass")
