"""Sanity tests for package initialization."""

from houndarr import __version__


def test_version_is_string() -> None:
    """Version should be a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_version_format() -> None:
    """Version should follow MAJOR.MINOR.PATCH format."""
    parts = __version__.split(".")
    assert len(parts) == 3, f"Expected 3 version parts, got: {__version__!r}"
    assert all(p.isdigit() for p in parts), f"Non-numeric version parts: {__version__!r}"
