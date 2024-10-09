from django.contrib import admin

from .models import Animal, AnimalBreed, AnimalPurchase, AnimalSale, AnimalType


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalBreed)
class AnimalBreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalPurchase)
class AnimalPurchaseAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalSale)
class AnimalSaleAdmin(admin.ModelAdmin):
    pass
