import strawberry
from schema import Weather
from data import read_data


@strawberry.type
class Query:
    @strawberry.field
    def city_temp(self, city: str) -> Weather:
        data = read_data()
        for row in data:
            if row["city"] == city:
                return Weather(**row)
        return Weather(city=city, temperature="not found in the sequence")
        }




