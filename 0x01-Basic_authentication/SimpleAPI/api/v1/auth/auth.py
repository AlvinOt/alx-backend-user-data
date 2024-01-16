#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """class to manage API auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

        for i in excluded_paths:
            if i[len(i) - 1] != '*':
                return False
            else:
                if i[:-1] == path[:len(i) - 1]:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be Flask request object"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """returns none"""
        return None
