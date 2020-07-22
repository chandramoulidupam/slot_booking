class ValidateAdmin:
    @property
    def interface(self):
        from userapp.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def user_is_admin(self, username: str):
        user_dto = self.interface.user_is_admin(username=username)
        return user_dto
