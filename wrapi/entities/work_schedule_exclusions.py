from __future__ import annotations

from datetime import date

from ..types_.entity import BaseEntity
from ..types_.enums import ExclusionType
from ..types_.scalar import WorkScheduleExclusionId


class WorkScheduleExclusion(BaseEntity):
    id: WorkScheduleExclusionId
    from_date: date
    to_date: date
    is_work_days: bool
    exclusion_type: ExclusionType
