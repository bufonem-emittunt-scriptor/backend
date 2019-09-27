

class EmailOrMobileAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            if username.isdigit():
                try:
                    user = get_user_model().objects.get(mobile=username)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None
            else:
                return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except User.DoesNotExist:
            return None