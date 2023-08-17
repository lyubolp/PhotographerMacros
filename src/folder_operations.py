"""
Module containing the folder related operations

Operations:
- Move
- Copy
- Delete

Criteria:
- File name matches pattern
- Date is in range
- Rating is equal to
"""

import os
import re
import time
import shutil

from abc import ABC, abstractmethod
from typing import List, Optional


class BaseOperation(ABC):
    """Base class for the operations"""

    def __init__(self, operation_name: str):
        self.__operation_name = operation_name

    # The fact that this method accepts a destination_path break the Interface Segregation Principle
    @abstractmethod
    def execute(self, source_path: str, destination_path: str = ''):
        """Execute the operation"""
        raise NotImplementedError

    @property
    def operation_name(self) -> str:
        """Get the operation name"""
        return self.__operation_name

class MoveOperation(BaseOperation):
    """Move operation"""

    def __init__(self):
        super().__init__('move')

    def execute(self, source_path: str, destination_path: str = ''):
        """Execute the move operation"""
        if not os.path.exists(source_path):
            raise FileNotFoundError(f'File {source_path} does not exist')
        if not os.path.exists(destination_path):
            raise FileNotFoundError(f'Destination folder {destination_path} does not exist')
        os.rename(source_path, destination_path)


class CopyOperation(BaseOperation):
    """Copy operation"""

    def __init__(self):
        super().__init__('copy')

    def execute(self, source_path: str, destination_path: str = ''):
        """Execute the copy operation"""
        if not os.path.exists(source_path):
            raise FileNotFoundError(f'File {source_path} does not exist')
        if not os.path.exists(destination_path):
            raise FileNotFoundError(f'Destination folder {destination_path} does not exist')
        shutil.copy2(source_path, destination_path)  # copy2 preserves metadata


class DeleteOperation(BaseOperation):
    """Delete operation"""

    def __init__(self):
        super().__init__('delete')

    def execute(self, source_path: str, destination_path: str = ''):
        """Execute the delete operation"""
        if not os.path.exists(source_path):
            raise FileNotFoundError(f'File {source_path} does not exist')
        os.remove(source_path)


class BaseCriteria(ABC):
    def __init__(self, criteria_name: str):
        self.__criteria_name = criteria_name

    @abstractmethod
    def filter(self, directory: str) -> List[str]:
        """Filter the files in the directory"""
        raise NotImplementedError


class FileNameCriteria(BaseCriteria):
    """File name criteria"""

    def __init__(self, pattern: str):
        super().__init__('File name criteria')
        self.__regex = re.compile(pattern)

    def filter(self, directory: str) -> List[str]:
        """Filter the files in the directory"""
        return [filename for filename in os.listdir(directory) if self.__regex.match(filename)]


class DateCriteria(BaseCriteria):
    """Date criteria"""
    def __init__(self,
                 start_date_epoch: Optional[int] = None, 
                 end_date_epoch: Optional[int] = None):
        super().__init__('Date criteria')
        self.__start_date_epoch = start_date_epoch if start_date_epoch is not None else 0
        self.__end_date_epoch = end_date_epoch if end_date_epoch is not None else time.time()

    def filter(self, directory: str) -> List[str]:
        """Filter the files in the directory"""
        return [filename for filename in os.listdir(directory) if self.__filter_by_date(filename)]

    def __filter_by_date(self, filepath: str) -> bool:
        creation_time = os.path.getctime(filepath)
        return self.__start_date_epoch <= creation_time <= self.__end_date_epoch
