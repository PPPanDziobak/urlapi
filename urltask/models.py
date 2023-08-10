import random
import string
from django.db import models


class Url(models.Model):
    """
    in this model we're storing input(long) and output(short) urls, it is necessary to retrieve original url when needed
    """
    input_url = models.URLField(max_length=300)
    output_url = models.URLField(max_length=300, unique=True, blank=True)

    def __str__(self):
        return self.output_url if self.output_url else self.input_url

    def save(self, *args, **kwargs):
        if not self.output_url:
            self.output_url = self.generate_unique_url()
        super().save(*args, **kwargs)

    @classmethod
    def generate_unique_url(cls):
        """
        this method is designed to create unique url when we are using api to make given long url shorter
        and then save it to model
        """
        while True:
            random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
            unique_url = f'http://127.0.0.1:8003/{random_string}'
            if not cls.objects.filter(output_url=unique_url).exists():
                return unique_url
