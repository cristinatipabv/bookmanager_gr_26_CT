# https://docs.djangoproject.com/en/6.0/topics/signals/

import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Book


@receiver(pre_save, sender=Book)
def my_signal_pre_save(sender, instance:Book, **kwargs):
    print("System is preparing to save a book! Hope it succeeds")
    # we can modify an instance before saveing
    # instance.title += "Haha Funny"
    print("Saving book!")


# @receiver(pre_delete, sender=Book)
# def cleanup_image(sender, instance:Book, **kwargs):
#     # when a book is about to be deleted, alosi delete teh image saved in the hard drive
#     if instance.image is not None and instance.image.name is not None:
#         # try:
#         #
#         #     if os.path.isfile(instance.image.path):
#         #         os.remove(instance.image.path)
#         # except ValueError as e:
#         #     # silent try-catch - nu sunt recomandate deoarece nu pot fi urmarite
#         #     pass
#
#

@receiver(pre_delete, sender=Book)
def cleanup_image(sender, instance: Book, **kwargs):
    # when a book is about to be deleted, also delete the image saved in the hard drive.
    if instance.image is not None:
        try:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)
        except ValueError as e:
            # Silent try-catch.
            pass

        # second option:
        # if instance.image.name is not None:
        #     if os.path.isfile(instance.image.path):
        #         os.remove(instance.image.path)