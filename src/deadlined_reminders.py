from abc import ABCMeta, ABC, abstractmethod
from collections.abc import Iterable
from datetime import datetime

from dateutil.parser import parse


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date, dayfirst=True):
        self.text = text
        self.date = parse(date, dayfirst)

    def is_due(self):
        return self.date <= datetime.now

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

