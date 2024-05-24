from enum import Enum
from typing import Any

from .base import Base


class Reference(Enum):
    marks = "marks"
    lengths = "lengths"
    periods = "periods"
    accesses = "accesses"
    downloads = "downloads"
    durations = "durations"
    work_forms = "work-forms"
    sort_orders = "sort-orders"
    work_states = "work-states"
    series_orders = "series-orders"
    series_states = "series-states"
    rating_periods = "rating-periods"
    promo_fragments = "promo-fragments"


class Catalog(Base):
    URL = 'https://api.author.today/v1/catalog'

    def get_reference(self, field: Reference) -> Any:

        return self.get(f"{self.URL}/{field.value}").json()

    def search(self, **params) -> Any:

        return self.get(f"{self.URL}/search", params=params).json()
