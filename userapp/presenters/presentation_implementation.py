import json

from django.http import HttpResponse, response

from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound
from userapp.interactors.user_login_interactor import \
    LoginInteractor
from userapp.interactors.\
    presenters.presenter_interface import PresenterInterface
from userapp.constants.custom_exceptions import \
    InvalidPassword, InvalidUsername
INVALIDUSERNAME = ("Invalid username", "INVALIDUSERNAME")
INVALIDPASSWORD = ("Invalid password", "INVALIDPASSWORD")
USERNAME_ALREADY_EXISTS = ("Username already exists", "USERNAME_ALREADY_EXISTS")

class UserLoginPresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_password(self):
        # raise NotFound(*INVALIDPASSWORD)

        response_object = response.HttpResponse(json.dumps(
            {
                "response":INVALIDPASSWORD[0],
                "http_status_code":INVALIDPASSWORD[1],
                "res_status": 403
            }
        ), status=403)
        return response_object


    def raise_exception_for_invalid_username(self):
        # raise NotFound(*INVALIDUSERNAME)
        response_object = response.HttpResponse(json.dumps(
            {
                "response": INVALIDUSERNAME[0],
                "http_status_code": INVALIDUSERNAME[1],
                "res_status": 403
            }
        ), status=403)
        return response_object

    def user_login_response(self, token_dto, user_is_admin):
        # print("\n"*10,UserAuthTokensDTO)
        print("**********","\n",token_dto)
        login_response = {
         "access_token": token_dto.access_token,
         "is_admin":user_is_admin
        }
        return response.HttpResponse(json.dumps(login_response), status=200)

    def user_signup_response(self, token_dto, user_is_admin):
        signup_response = {
            "access_token": token_dto.access_token,
            "is_admin":user_is_admin}
        return response.HttpResponse(json.dumps(signup_response), status=200)

    def raise_exception_for_username_already_exists(self):

        response_object = response.HttpResponse(json.dumps(
            {
                "response": USERNAME_ALREADY_EXISTS[0],
                "http_status_code": USERNAME_ALREADY_EXISTS[1],
                "res_status": 403
            }
        ), status=403)
        return response_object
    def user_profile_details(self, user_profile_dto):
        user_profile_response = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "is_admin": user_profile_dto.is_admin
        }
        return response.HttpResponse(json.dumps(user_profile_response), status=201)