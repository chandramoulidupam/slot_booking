from typing import List
from slot_booking.interactors.storages.dtos import UserDto


class AuthService:

    @property
    def interface(self):
        from userapp.interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, username: str):
        user_dto = self.interface.get_user_dtos(username=username)

        user_details_dtos = UserDto(
                name=user_dto.name,
                user_id=user_dto.user_id,
                is_admin=user_dto.is_admin
            )

        return user_details_dtos