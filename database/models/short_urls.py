import mongoengine as me


class UrlStore(me.Document):
    short_url_code = me.fields.StringField(primary_key=True, required=True)
    original_url = me.fields.URLField(required=True)
    click_count = me.fields.LongField(default=0)
    country_wise_click_count = me.fields.DictField()
    hour_wise_click_count = me.fields.DictField()
    created_at = me.fields.LongField(required=True)

    meta = {
        'collection': 'url_store'
    }
