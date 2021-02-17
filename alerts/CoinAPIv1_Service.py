

api_key = "5EF0AE48-B470-47FD-83E3-93343A1F775F"


class CoinAPIv1_subscribe(object):
    def __init__(self, apikey):
        self.type = "hello"
        self.apikey = apikey
        self.heartbeat = False
        self.subscribe_filter_asset_id = ["BTC"]
        self.subscribe_data_type = ["trade"]





