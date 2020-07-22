from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from userapp.interactors.user_login_interactor import \
    LoginInteractor
from userapp.storages.storage_implementation import \
    LoginStorageImplementation
from userapp.presenters.presentation_implementation import \
    UserLoginPresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    request_data = kwargs['request_data']
    storage = LoginStorageImplementation()
    oauth_storage = OAuth2SQLStorage()
    presenter = UserLoginPresenterImplementation()
    interactor = LoginInteractor(
        storage=storage,
        oauth_storage=oauth_storage
    )
    response = interactor.user_login_wrapper(
        username=request_data['username'],
        password=request_data['password'],
        presenter=presenter
    )

    return response
