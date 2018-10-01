import pytest

from app.journal.models import Entry


@pytest.fixture
def entry(user):
    return Entry.objects.create(
        user=user,
        text="It was the best of times, it was the blurst of times.",
        published=True,
    )
