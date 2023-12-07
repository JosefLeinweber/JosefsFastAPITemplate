import datetime
import typing

import pydantic

from src.utility.formatters.date_time import datetime_2_isoformat
from src.utility.formatters.name_case import snake_2_camel


class BaseModel(pydantic.BaseModel):
    model_config: pydantic.ConfigDict = pydantic.ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        validate_assignment=True,
        json_encoders={datetime.datetime: datetime_2_isoformat},
        alias_generator=snake_2_camel,
    )
