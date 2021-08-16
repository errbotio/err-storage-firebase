import logging
from typing import Any

from errbot.storage.base import StorageBase, StoragePluginBase
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from jsonpickle import decode, encode

log = logging.getLogger("errbot.storage.firebase")

SECRET_ENTRY = "secret"
DATA_URL_ENTRY = "data_url"
EMAIL = "email"


class FirebaseStorage(StorageBase):
    def __init__(self, firebase_app, namespace):
        self.fb = firebase_app
        self.ns = namespace

    def get(self, key: str) -> Any:
        result = self.fb.get("/%s" % self.ns, key)
        if result is None:
            raise KeyError("%s doesn't exists." % key)
        return decode(result)

    def remove(self, key: str):
        self.fb.delete("/%s" % self.ns, key)

    def set(self, key: str, value: Any) -> None:
        log.debug("Setting value '/%s/%s' at %s" % (self.ns, key, encode(value)))
        self.fb.put("/%s" % self.ns, key, encode(value))

    def len(self):
        return len(self.keys())  # terrible TODO improve

    def keys(self):
        result = self.fb.get("/%s" % self.ns, None)
        if result is None:
            return set()
        return result.keys()

    def close(self) -> None:
        pass


class FirebasePlugin(StoragePluginBase):
    def __init__(self, bot_config):
        super().__init__(bot_config)
        if not all(
            k in self._storage_config for k in (EMAIL, SECRET_ENTRY, DATA_URL_ENTRY)
        ):
            raise Exception(
                "You need to specify an email, a secret firebase key and a firebase data url in your config.py like this:\n"
                "STORAGE_CONFIG={\n"
                '"email": "foo@bar.com"\n'
                '"secret":"4e45fd3..."\n'
                '"data_url": "https://radiant-bear-6338.firebaseio.com/",\n'
                "}"
            )

    def open(self, namespace: str) -> StorageBase:
        config = self._storage_config
        auth = FirebaseAuthentication(config[SECRET_ENTRY], config[EMAIL])
        fb = FirebaseApplication(config[DATA_URL_ENTRY], auth)

        return FirebaseStorage(fb, namespace)
