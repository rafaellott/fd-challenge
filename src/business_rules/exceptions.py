
class BaseFdChallengeException(Exception):

    def __init__(self, reason=""):
        self.reason = reason


class UnauthorizedException(BaseFdChallengeException):
    pass


class ForbiddenException(BaseFdChallengeException):
    pass


class ResourceNotFoundException(BaseFdChallengeException):
    pass
