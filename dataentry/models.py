from django.db import models
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid

# Create your models here.


class AddRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender_list = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    registration_type = models.CharField(max_length=120, default="New")
    registration_no = models.CharField(
        max_length=120, default="2947388", null=True, blank=True
    )

    # personal Information
    name = models.CharField(max_length=120)
    arabic_name = models.CharField(max_length=120, null=True, blank=True)
    date_of_birth = models.CharField(
        max_length=100, default="14/12/2022", null=True, blank=True
    )
    nationality = models.CharField(max_length=120, default="Oman")
    sex = models.CharField(max_length=100, choices=gender_list, default="Male")
    passport_no = models.CharField(max_length=120, default="B00806552")
    civil_id = models.CharField(
        max_length=120, default="128240750", null=True, blank=True
    )
    sponsor = models.CharField(max_length=120, default="////////")
    category = models.CharField(
        max_length=200, default="Employment (labour card & Resident card)"
    )

    # sanad_ref_no = models.CharField(max_length=120, default="H013927VKC005")
    # mobile_no = models.IntegerField()

    # Medical Date Information
    validity_of_the_medical = models.CharField(max_length=120, default="21/11/2022")
    to = models.CharField(max_length=120, default="21/12/2022")
    medical_center = models.CharField(
        max_length=120, default="BADR AL SAMAA HOSPITAL - SALALAH"
    )

    # Print Information
    qr_code = models.ImageField(upload_to="images/QR_CODE", null=True, blank=True)

    def __str__(self):
        return self.name
    
    def generate_qr_code(self):
        qr_code_content = f"http://www.cdcmohgovernment.com/single_record_information/{self.id}"
        qr_code_image = qrcode.make(qr_code_content)
        buffer = BytesIO()
        qr_code_image.save(buffer, format='PNG')
        buffer.seek(0)
        filename = f"qr_code_{self.id}.png"
        file = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.getbuffer().nbytes, None
        )
        return file

    def save(self, *args, **kwargs):
        if not self.qr_code:  # Only generate and save the QR code if it doesn't exist
            qr_code_file = self.generate_qr_code()
            if qr_code_file:
                self.qr_code.save(qr_code_file.name, qr_code_file, save=False)
        
        super().save(*args, **kwargs)