import time

import mongoengine as me
from database.models.short_urls import UrlStore
from env import ENV


class UrlStoreRepository:
    """
    This class handles all DB operations for MongoDB.
    """

    def __init__(self) -> None:
        self.connection = me.connect(db=ENV.mongo_db_name,
                                     username=ENV.mongo_db_username,
                                     password=ENV.mongo_db_password,
                                     host=ENV.mongo_db_host,
                                     port=ENV.mongo_db_host_port)

    def save_new_url(self, short_url_code: str, original_url: str) -> dict:
        """
        This function is used to add new urls to db.
        """
        url_store_data = UrlStore(
            short_url_code=short_url_code, original_url=original_url, created_at=int(time.time()*1000))
        try:
            saved_url_data = UrlStore.objects().insert(url_store_data)
            return saved_url_data.to_mongo().to_dict()
        except Exception as e:
            print(
                f"Failed to add URL : {original_url} to db with exception as {e}")
            return {}

    def register_url_hit(self, short_url_code: str, country_code: str, hour_of_click: int) -> None:
        """
        This function updates db-entries for link-clicks.
        """
        try:
            UrlStore.objects(short_url_code=short_url_code).update_one(__raw__={
                "$inc": {
                    "click_count": 1,
                    f"country_wise_click_count.{country_code}": 1,
                    f"hour_wise_click_count.{hour_of_click}": 1

                },
            }, upsert=False)
        except Exception as e:
            print(
                f'failed to register link click for url-code : {short_url_code}  with Exception as {e}')

    def get_original_url_data_from_code(self, url_code: str) -> dict:
        try:
            original_url = UrlStore.objects(short_url_code=url_code).get().to_mongo().to_dict()
            return original_url
        except Exception as e:
            print(e)
            return {}
