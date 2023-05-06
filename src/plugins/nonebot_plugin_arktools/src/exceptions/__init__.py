"""异常基类"""
from typing import Union


class ArkBaseException(Exception):
    """基础异常类"""
    def __init__(self, msg: str = "出现了错误，但是未说明具体原因。", details: Union[str, int] = ""):
        super().__init__(msg)
        self.msg = f"{msg} - {details}"

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.msg


class NamedCharacterNotExistException(ArkBaseException):
    """这个名字的干员不存在"""
    def __init__(self, msg: str = "干员不存在！", details: str = ""):
        super().__init__(msg, details)


class NamedPoolNotExistException(ArkBaseException):
    """这个名字的池子不存在"""
    def __init__(self, msg: str = "卡池不存在！", details: str = ""):
        super().__init__(msg, details)


class MAAFailedResponseException(ArkBaseException):
    """响应错误"""
    def __init__(self, msg: str = "作业站响应错误！", details: str = ""):
        super().__init__(msg, details)


class MAANoResultException(ArkBaseException):
    """没有作业"""
    def __init__(self, msg: str = "没有查询到结果！", details: str = ""):
        super().__init__(msg, details)


class NoHandbookInfoException(ArkBaseException):
    """没有档案"""
    def __init__(self, msg: str = "干员没有档案！", details: str = ""):
        super().__init__(msg, details)


__all__ = [
    "NamedCharacterNotExistException",
    "NamedPoolNotExistException",
    "NoHandbookInfoException",

    "MAAFailedResponseException",
    "MAANoResultException"
]
