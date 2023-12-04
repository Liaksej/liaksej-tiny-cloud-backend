import os.path
import uuid

from djangoProject import settings


def save_file(file):
    file_name = f"{uuid.uuid4().hex}{os.path.splitext(file.name)[1]}"
    save_path = os.path.join(settings.STATIC_ROOT, file_name)

    with open(save_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return {
        "file_name": file_name,
        "file_path": os.path.join(settings.STATIC_URL, file_name),
    }
