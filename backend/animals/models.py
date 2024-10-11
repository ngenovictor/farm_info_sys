from django.db import models


# Create your models here.
class AnimalType(models.Model):
    """
    Model for Animal Type
    eg Cow, Goat, Sheep
    """

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class AnimalBreed(models.Model):
    """
    Model for Animal Breed
    eg Jersey, Friesian, Merino
    """

    animal_type = models.ForeignKey(AnimalType, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.animal_type.name}"


class Animal(models.Model):
    """
    Model for Animal
    """

    name_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    breed = models.ForeignKey(AnimalBreed, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    father = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="father_animal"
    )
    mother = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="mother_animal"
    )

    def __str__(self) -> str:
        if self.name_id and self.nick_name:
            return f"{self.name_id} ({self.nick_name})"
        if self.nick_name:
            return self.nick_name
        elif self.name_id:
            return self.name_id
        else:
            return "id: " + str(self.id)


class AnimalHeatEvent(models.Model):
    """
    Model for Animal Heat Event
    """

    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    duration = models.DurationField()
    notes = models.TextField(null=True, blank=True)


class AnimalServedEvent(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    serve_type = models.CharField(
        max_length=20, choices=[("AI", "Artificial Insemination"), ("Bull", "Natural Bull")]
    )
    genetics = models.ForeignKey(to=AnimalBreed, on_delete=models.DO_NOTHING)
    notes = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.animal}"


# class AnimalImage(models.Model):
#     image = models.ImageField(upload_to="")


# class AnimalNoteEvent(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     notes = models.TextField(null=True, blank=True)
#     images = models.ForeignKey(to=AnimalImage, on_delete=models.CASCADE)


class AnimalPurchase(models.Model):
    """
    Model for Animal Purchase
    """

    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date_of_purchase = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.CharField(max_length=100)
    buyer_contact = models.CharField(max_length=100)
    buyer_address = models.TextField()
    seller = models.CharField(max_length=100)
    seller_contact = models.CharField(max_length=100)
    seller_address = models.TextField()


class AnimalSale(models.Model):
    """
    Model for Animal Sale
    """

    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date_of_sale = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.CharField(max_length=100)
    buyer_contact = models.CharField(max_length=100)
    buyer_address = models.TextField()
    seller = models.CharField(max_length=100)
    seller_contact = models.CharField(max_length=100)
    seller_address = models.TextField()


# Feeds
# Disease management
# Vaccination
# Milk production
# Meat production
# Wool production
# Egg production
# Fodder management
# Animal weight management
# Animal health management
# Animal breeding management
# Animal purchase management
# Animal sale management
# Breeding
# Production
# feeding
# financial
