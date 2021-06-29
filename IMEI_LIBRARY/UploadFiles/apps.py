from django.apps import AppConfig


class UploadfilesConfig(AppConfig):
    name = 'UploadFiles'
    
    def ready(self):
        import UploadFiles.signals