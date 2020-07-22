from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from userapp.storages.storage_implementation import \
    LoginStorageImplementation
from userapp.presenters.presentation_implementation import UserLoginPresenterImplementation
from ...interactors.get_user_details_interactor import UserProfileInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']
    request_data = kwargs['request_data']
    storage = LoginStorageImplementation()
    presenter = UserLoginPresenterImplementation()
    interactor = UserProfileInteractor(
        storage=storage,
    )
    response = interactor.user_profile_wrapper(
        username=request_data['username'],
        presenter=presenter
    )

    return response