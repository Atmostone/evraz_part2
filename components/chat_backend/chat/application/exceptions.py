from classic.app.errors import AppError


class NotAllowed(AppError):
    msg_template = "You are not allowed to do this action"
    code = 'not_allowed'


class DoesNotExists(AppError):
    msg_template = "This object does not exists"
    code = 'not_exists'


class AuthFailed(AppError):
    msg_template = "Authorization failed"
    code = 'auth_fail'
