import datetime

from django.contrib import admin

from .models import (
    Animal,
    AnimalBreed,
    AnimalHeatEvent,
    AnimalPurchase,
    AnimalSale,
    AnimalServedEvent,
    AnimalType,
)


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalBreed)
class AnimalBreedAdmin(admin.ModelAdmin):
    pass


def compute_age(obj, field_name):
    field_date = getattr(obj, field_name)
    if field_date is None:
        return None
    age_in_years = datetime.datetime.now().year - field_date.year
    if age_in_years == 0:
        age_in_months = datetime.datetime.now().month - field_date.month
        if age_in_months == 0:
            age_in_days = datetime.datetime.now().day - field_date.day
            if age_in_days == 0:
                return "Today"
            elif age_in_days == 1:
                return f"{age_in_days} day"
            return f"{age_in_days} days"
        elif age_in_months == 1:
            return f"{age_in_months} month"
        return f"{age_in_months} months"
    elif age_in_years == 1:
        return f"{age_in_years} year"
    return f"{age_in_years} years"


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    def age(self, obj):
        age = compute_age(obj, "date_of_birth")
        if age is None:
            approx_age = compute_age(obj, "date_of_birth_approximate")
            if approx_age is not None:
                return approx_age + " (approx)"
        return age

    list_display = (
        "name_id",
        "nick_name",
        "breed",
        "sex",
        "date_of_birth",
        "age",
        "father",
        "mother",
    )


@admin.register(AnimalPurchase)
class AnimalPurchaseAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalSale)
class AnimalSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalHeatEvent)
class AnimalHeatEventAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalServedEvent)
class AnimalServedEventAdmin(admin.ModelAdmin):
    def time_since(self, obj):
        return compute_age(obj, "date")

    def expected_delivery_date(self, obj):
        gestation_period_days = obj.animal.breed.animal_type.gestation_period_days
        return obj.date + datetime.timedelta(days=gestation_period_days)

    list_display = (
        "animal",
        "date",
        "time_since",
        "expected_delivery_date",
        "serve_type",
        "genetics",
    )
