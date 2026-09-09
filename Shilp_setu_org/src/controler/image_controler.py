from src.model.image_model import Image
from src.services.image_services import upload_image

def save_image(db, file, file_name):
    uploaded = upload_image(file, file_name)

    image = Image(
        name=uploaded["file_name"],
        url=uploaded["url"],
        file_id=uploaded["file_id"],
    )
    db.add(image)
    db.commit()
    db.refresh(image)
    return image