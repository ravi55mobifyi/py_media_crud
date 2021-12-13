from rest_framework.response import Response
from rest_framework import status


class ResponseHelper:

    def get_status_500(self, msg="internal server error"):
        error_message = {"message": msg}
        return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_status_400(self, msg="invalid data"):
        error_message = {"message": msg}
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def get_status_201(self, msg="success"):
        message = {"message": msg}
        return Response(message, status=status.HTTP_201_CREATED)

    def get_status_200(self, msg="success", data=None):
        ok_response = {"message": msg}
        if data is None:
            return Response(ok_response, status=status.HTTP_200_OK)
        else:
            ok_response["data"] = data
            return Response(ok_response, status=status.HTTP_200_OK)

    def get_status_404(self, msg="No data found"):
        not_found_response = {"message": msg}
        return Response(not_found_response, status=status.HTTP_404_NOT_FOUND)