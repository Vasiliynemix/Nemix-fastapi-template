from pydantic import BaseModel, ConfigDict


class TaskBaseSchema(BaseModel):
    pass


class TaskAddSchema(TaskBaseSchema):
    model_config = ConfigDict(from_attributes=True)
