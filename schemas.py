from pydantic import BaseModel
from typing import Optional


class LoadOut(BaseModel):
    cpu_load: float  # percents
    ram_load: float  # percents
    gpu_load: Optional[float]  # percents
