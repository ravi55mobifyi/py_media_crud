import traceback

from rest_framework.views import APIView
from .response_helper import ResponseHelper
from .operation_helper import OperationHelper

ResponseHelper = ResponseHelper()
OperationHelper = OperationHelper()


class Episode(APIView):

    def post(self, request):
        """
        API to add episode details in database
        """
        try:
            data = request.data
            if not data:
               return ResponseHelper.get_status_400("request payload is empty")

            mandatory_keys = {"title", "description", "image", "audio", "showId"}
            missing_keys = []
            for _key in mandatory_keys:
                if _key not in data or not data[_key]:
                    missing_keys.append(_key)
            if missing_keys:
                msg = ",".join(missing_keys) + " keys are missing/blank in request payload"
                return ResponseHelper.get_status_400()

            response = OperationHelper.store_episode(data)
            return response
        except:
            traceback.print_exc()
            return ResponseHelper.get_status_500()

    def get(self, request):
        """
        GET API to get episode list or single episode
        """
        try:
            episode_id = request.GET.get("episodeId", "")

            response = OperationHelper.get_episode_data(episode_id)
            return response
        except:
            traceback.print_exc()
            return ResponseHelper.get_status_500()


class Show(APIView):

    def post(self, request):
        """
        API to add show details in database
        """
        try:
            data = request.data
            if not data:
               return ResponseHelper.get_status_400("request payload is empty")

            mandatory_keys = {"title", "description", "image"}
            missing_keys = []
            for _key in mandatory_keys:
                if _key not in data or not data[_key]:
                    missing_keys.append(_key)
            if missing_keys:
                msg = ",".join(missing_keys) + " keys are missing/blank in request payload"
                return ResponseHelper.get_status_400()

            response = OperationHelper.store_show(data)
            return response
        except:
            traceback.print_exc()
            return ResponseHelper.get_status_500()

    def get(self, request):
        """
        GET API to get show list or single episode
        """
        try:
            show_id = request.GET.get("showId", "")

            response = OperationHelper.get_show_data(show_id)
            return response
        except:
            traceback.print_exc()
            return ResponseHelper.get_status_500()