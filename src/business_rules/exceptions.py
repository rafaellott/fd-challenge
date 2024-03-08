
class BaseFdChallengeException(Exception):

    def __init__(self, message=None):
        self.message = message


class UnauthorizedException(BaseFdChallengeException):
    pass


class ForbiddenException(BaseFdChallengeException):
    pass


class BadGatewayException(BaseFdChallengeException):
    pass
