import os
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from gcloud import storage


@deconstructible
class GoogleCloudStorage(Storage):

    def __init__(self, project=None, bucket=None):
        if project is None:
            project = os.getenv('GOOGLE_PROJECT')
        if bucket is None:
            bucket = os.getenv('GOOGLE_BUCKET')
        client = storage.Client.from_service_account_json(
            os.getenv('GOOGLE_APPLICATION_CREDENTIALS'), project)
        self.bucket = client.get_bucket(bucket)

    def _open(self, name, mode='rb'):
        return ContentFile(self.bucket.get_blob(name))

    def _save(self, name, content):
        blob = self.bucket.blob(content.name)
        blob.upload_from_file(content.file, size=content.size)
        blob.make_public()
        return blob.public_url

    def _name(self, name):
        return name.split('/')[-1]

    def delete(self, name):
        self.bucket.get_blob(self._name(name)).delete()

    def exists(self, name):
        return self.bucket.blob('name').exists()

    def get_available_name(self, name):
        return self._name(name)

    def get_valid_name(self, name):
        return name

    def size(self, name):
        return self.bucket.get_blob(self._name(name)).size

    def url(self, name):
        return self.bucket.get_blob(self._name(name)).public_url
