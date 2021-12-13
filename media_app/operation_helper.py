from bson import ObjectId

from py_media_crud.settings import db
from .response_helper import ResponseHelper
ResponseHelper = ResponseHelper()


class OperationHelper:

    def store_episode(self, data):
        """
        this method processes episode post api
        """
        mandatory_keys = {"title", "description", "image", "audio", "showId"}
        save_json = {
            "title": data["title"],
            "description": data["description"],
            "image": data["image"],
            "audio": data["audio"],
            "showId": data["showId"]
        }
        try:
            result = db.episodes.insert_one(save_json)
        except:
            return ResponseHelper.get_status_500("error in storing episode details")

        return ResponseHelper.get_status_201("episode save successfully")

    def store_show(self, data):
        """
        this method processes show post api
        """
        mandatory_keys = {"title", "description", "image"}
        save_json = {
            "title": data["title"],
            "description": data["description"],
            "image": data["image"]
        }
        try:
            result = db.shows.insert_one(save_json)
        except:
            return ResponseHelper.get_status_500("error in storing episode details")

        return ResponseHelper.get_status_201("show save successfully")

    def get_episode_data(self, episode_id):
        """
        this method gets episode list or episode details
        """
        query = {}
        if episode_id:
            try:
                query["_id"] = ObjectId(episode_id)
            except:
                return ResponseHelper.get_status_400("invalid episodeId")

        result = db.episodes.find(query)

        final_response = []
        for _data in result:
            _data["_id"] = str(_data["_id"])
            final_response.append(_data)

        if not final_response:
            return ResponseHelper.get_status_404("episode details not found")

        return ResponseHelper.get_status_200("episode details found", data=final_response)

    def get_show_data(self, show_id):
        """
        this method gets show list or episode details
        """
        query = {}
        if show_id:
            try:
                query["_id"] = ObjectId(show_id)
            except:
                return ResponseHelper.get_status_400("invalid showId")

        result = db.shows.find(query)

        final_response = []
        for _data in result:
            _data["_id"] = str(_data["_id"])
            final_response.append(_data)

        if not final_response:
            return ResponseHelper.get_status_404("show details not found")

        return ResponseHelper.get_status_200("show details found", data=final_response)
