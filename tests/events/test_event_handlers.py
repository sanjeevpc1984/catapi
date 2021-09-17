import pytest

from catapi import dto
from catapi.events.event_handlers import handle_cat_created, handle_ping


@pytest.mark.parametrize(
    "data",
    [{"event_id": "00000000-0000-4000-0000-000000000000"}],
)
def test_handle_ping(data: dto.JSON) -> None:
    handle_ping(data)


def test_handle_cat_created() -> None:
    data: dto.JSON = {
        "cat_id": "000000000000000000000101",
    }

    handle_cat_created(data)
