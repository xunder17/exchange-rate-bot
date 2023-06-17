"""Кастомные классы обработки исключений."""


class APIException(Exception):
    """Ошибки в работе API."""

    ...


class ServiceException(Exception):
    """Ошибки в работе сервиса курса валют."""

    ...
