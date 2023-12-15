import os
import uuid

from djangoProject import settings


def save_file(file):
    file_name = f"{uuid.uuid4().hex}{os.path.splitext(file.name)[1]}"
    save_path = os.path.join(settings.MEDIA_ROOT, file_name)

    with open(save_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return {
        "file_name": file_name,
        "file_path": save_path,
    }


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
