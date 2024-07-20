from rest_framework import viewsets, permissions, views
from .serializers import RegisterSerializer, KycSerializer
from userApp.models import CustomUser, Kyc
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from django.conf import settings
from firebase_admin import auth
from .firebase_init import initialize_firebase


common_status = settings.COMMON_STATUS


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("id")
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class KycViewSet(viewsets.ModelViewSet):
    queryset = Kyc.objects.all().order_by("id")
    serializer_class = KycSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


def jwt_token(user):
    user_id = user.custom_user
    access_token = AccessToken.for_user(user_id)
    refresh_token = RefreshToken.for_user(user_id)
    payload = {
        "access_token": str(access_token),
        "refresh_token": str(refresh_token),
        "user_id": user.id,
    }
    return Response(payload, common_status["success"]["code"])


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        a = initialize_firebase()
        print(a)
        data = request.data
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        firebase_id_token = data.get("firebase_id_token")
        is_social_login = data.get("is_social_login")

        if is_social_login is True:
            try:
                # Initialize Firebase app with your configuration file
                # cred = credentials.Certificate("../../paymorz/firebase-config.json")
                # print(cred)
                # firebase_admin.initialize_app(cred)
                decoded_token = auth.verify_id_token(firebase_id_token)
                firebase_user_uid = decoded_token["uid"]
                firebase_user_email = decoded_token.get("email")
                firebase_user_name = decoded_token.get("name")
            except:
                return Response(
                    {"message": "Invalid user"},
                    status=common_status["bad_request"]["code"],
                )

            try:
                if firebase_user_email:
                    try:
                        user = CustomUser.objects.get(email=firebase_user_email)
                    except:
                        user = None
                    if user:
                        social_login_uid = user.social_login_uid
                        if social_login_uid == firebase_user_uid:
                            user.first_name = firebase_user_name
                            user.middle_name = None
                            user.last_name = None
                            user.is_social_login = True
                            user.save(
                                update_fields=[
                                    "is_social_login",
                                    "first_name",
                                    "middle_name",
                                    "last_name",
                                ]
                            )
                            return jwt_token(user)
                        else:
                            user.social_login_uid = firebase_user_uid
                            user.first_name = firebase_user_name
                            user.middle_name = None
                            user.last_name = None
                            user.is_social_login = True
                            user.save(
                                update_fields=[
                                    "is_social_login",
                                    "social_login_uid",
                                    "first_name",
                                    "middle_name",
                                    "last_name",
                                ]
                            )
                            return jwt_token(user)
                    else:
                        new_user = CustomUser.objects.create(
                            email=firebase_user_email,
                            first_name = firebase_user_name,
                            password="Test@!Test123",
                            is_social_login=True,
                            social_login_uid=firebase_user_uid,
                        )
                        return jwt_token(new_user)
            except:
                return Response(
                    {"message": common_status["bad_request"]["message"]},
                    status=common_status["bad_request"]["code"],
                )
        elif email and password and not phone and is_social_login is False:
            try:
                user = CustomUser.objects.get(email=email)
                if user:
                    user_password = user.password
                    if user_password == password:
                        user.is_social_login = False
                        user.save(update_fields=["is_social_login"])
                        return jwt_token(user)
                    else:
                        return Response(
                            {"message": "Incorrect Password"},
                            status=common_status["bad_request"]["code"],
                        )
                else:
                    return Response(
                        {"message": "User does not exist"},
                        status=common_status["not_found"]["code"],
                    )
            except:
                return Response(
                    {"message": "Incorrect email or password, please check"},
                    status=common_status["bad_request"]["code"],
                )

        elif phone and not email and not password and is_social_login is False:
            try:
                user = CustomUser.objects.get(phone=phone)
                if user:
                    otp = 12345678
                    user.otp = otp
                    user.is_social_login = False
                    user.save(update_fields=["otp", "is_social_login"])
                    return Response(
                        {
                            "otp": otp,
                            "message": f"We have sent a 8-numbers OTP code to {phone}",
                        },
                        status=common_status["success"]["code"],
                    )
                else:
                    return Response(
                        {"message": "User does not exist"},
                        status=common_status["not_found"]["code"],
                    )
            except:
                return Response(
                    {"message": "Incorrect phone number, please check"},
                    status=common_status["bad_request"]["code"],
                )

        else:
            return Response(
                {"message": common_status["bad_request"]["message"]},
                status=common_status["bad_request"]["code"],
            )


class VerifyOTPView(views.APIView):
    def post(self, request):
        phone = request.data.get("phone")
        otp = request.data.get("otp")

        try:
            if phone and otp:
                try:
                    user = CustomUser.objects.get(phone=phone)
                    if user.otp == int(otp):
                        user.otp = None
                        user.save(update_fields=["otp"])
                        return jwt_token(user)
                    else:
                        return Response(
                            {"message": "Incorrect otp"},
                            status=common_status["bad_request"]["code"],
                        )
                except:
                    return Response(
                        {"message": "User does not exist"},
                        status=common_status["not_found"]["code"],
                    )
            else:
                return Response(
                    {"message": "Incorrect phone number or otp, please check"},
                    status=common_status["bad_request"]["code"],
                )

        except:
            return Response(
                {"message": common_status["bad_request"]["message"]},
                status=common_status["bad_request"]["code"],
            )
