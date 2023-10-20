from backend.load_data import (
    read_restaurants_data,
    from_geojson_to_restaurant_json,
    from_restaurant_json_to_pydantic,
)
from pathlib import Path
import pytest
import os


@pytest.mark.fail_slow("300milliseconds")
def test_read_restaurants_data():
    read_restaurants_data(
        Path(os.environ["DATA_DIRECTORY"]) / "restaurants_paris.geojson"
    )


def test_from_geojson_to_restaurant_json():
    input = {
        "type": "Feature",
        "properties": {
            "full_id": "n175539450",
            "osm_id": "175539450",
            "osm_type": "node",
            "addr:housenumber": "8",
            "addr:postcode": "75014",
            "addr:street": "Rue des Plantes",
            "amenity": "restaurant",
            "cuisine": "french",
            "name": "Le Severo",
            "opening_hours": "Mo-Fr 12:00-13:30, 19:30-21:30",
            "addr:city": "",
            "outdoor_seating": "",
            "phone": "",
            "toilets:wheelchair": "",
            "wheelchair": "",
            "wheelchair:description": "",
            "website": "",
            "description": "",
            "internet_access": "",
            "contact:facebook": "",
            "contact:phone": "",
            "contact:website": "",
            "level": "",
            "smoking": "",
            "diet:vegetarian": "",
            "start_date": "",
            "name:zh": "",
            "wikidata": "",
            "email": "",
            "addr:country": "",
            "check_date:opening_hours": "",
            "old_name": "",
            "wikipedia": "",
            "survey:date": "",
            "delivery": "",
            "heritage": "",
            "heritage:operator": "",
            "mhs:inscription_date": "",
            "ref:mhs": "",
            "source:heritage": "",
            "takeaway": "",
            "bar": "",
            "internet_access:ssid": "",
            "reservation": "",
            "access:covid19": "",
            "opening_hours:covid19": "",
            "takeaway:covid19": "",
            "name:fr": "",
            "brand": "",
            "brand:wikidata": "",
            "brand:wikipedia": "",
            "operator": "",
            "name:ru": "",
            "operator:wikidata": "",
            "operator:wikipedia": "",
            "shop": "",
            "cuisine:fr": "",
            "air_conditioning": "",
            "capacity": "",
            "diet:gluten_free": "",
            "diet:halal": "",
            "diet:vegan": "",
            "brand:website": "",
            "toilets": "",
            "description:covid19": "",
            "toilets:access": "",
            "toilets:disposal": "",
            "toilets:position": "",
            "brewery": "",
            "tourism": "",
            "name:es": "",
            "alt_name": "",
            "delivery:covid19": "",
            "drive_through:covid19": "",
            "drive_through": "",
            "branch": "",
            "internet_access:fee": "",
            "happy_hours": "",
            "opening_hours:signed": "",
            "speciality": "",
            "contact:instagram": "",
            "name:zh_pinyin": "",
            "contact:housenumber": "",
            "contact:postcode": "",
            "contact:street": "",
            "type": "",
            "restaurant": "",
            "stars": "",
            "all_you_can_eat": "",
            "cuisine:zh": "",
            "cocktails": "",
            "changing_table": "",
            "fax": "",
            "contact:city": "",
            "ref:FR:SIREN": "",
            "ref:FR:SIRET": "",
            "wifi": "",
            "was:name": "",
            "image": "",
            "official_name": "",
            "name:en": "",
            "microbrewery": "",
            "terrace": "",
            "organic": "",
            "diet:kosher": "",
            "payment:visa": "",
            "name:ar": "",
            "food": "",
            "vegetarian": "",
            "was:cuisine:fr": "",
            "short_name": "",
            "self_service": "",
            "name:ko": "",
            "payment:american_express": "",
            "payment:cash": "",
            "payment:credit_cards": "",
            "payment:debit_cards": "",
            "payment:mastercard": "",
            "disused:amenity": "",
            "diet:healthy": "",
            "diet:lactose_free": "",
            "diet:meat": "",
            "diet:raw": "",
            "noname": "",
            "name:he": "",
            "tobacco": "",
            "atm": "",
            "birds": "",
            "entrance": "",
            "description:zh": "",
            "payment:cards": "",
            "payment:cb": "",
            "payment:cheque": "",
            "payment:contactless": "",
            "payment:meal_voucher": "",
            "disused:name": "",
            "wheelchair:description:de": "",
            "coffeehouse": "",
            "survey": "",
            "ref": "",
            "craft": "",
            "facebook": "",
            "happycow:id": "",
            "website_1": "",
            "website_2": "",
            "contact:email": "",
            "addr:housename": "",
            "checked": "",
            "name:zh-CN": "",
            "name:zh-TW": "",
            "name:cn": "",
            "takeaway:lunchbox": "",
            "int_name": "",
            "layer": "",
            "drive_in": "",
            "diet:pescetarian": "",
            "name:ja": "",
            "contact:country": "",
            "open": "",
            "source:amenity": "",
            "source:cuisine": "",
            "source:name": "",
            "contact:housename": "",
            "opening_hours:kitchen": "",
            "note:fr": "",
            "name:signed": "",
            "description:fr": "",
            "description:it": "",
            "name:tr": "",
            "shop_1": "",
            "addr:state": "",
            "architect": "",
            "source:architect": "",
            "gay": "",
            "old_name_1": "",
            "was": "",
            "construction": "",
            "url": "",
            "alt_name_1": "",
            "name:vi": "",
            "depth": "",
            "sells:tobacco": "",
            "payment:bitcoin": "",
            "disused": "",
            "disused:craft": "",
            "disused:shop": "",
            "halal": "",
            "name:it": "",
            "source:addr": "",
            "source:email": "",
            "source:phone": "",
            "capacity:disabled": "",
            "contact:twitter": "",
            "website:menu:en": "",
            "website:menu:fr": "",
            "diet:organic": "",
            "brewery:note": "",
            "sushi": "",
            "drink:wine": "",
            "origin": "",
            "name:ro": "",
            "cuisine_1": "",
            "full_name": "",
            "contact:fax": "",
            "service": "",
            "alt_website": "",
            "website_3": "",
            "payment:electronic_purses": "",
            "contact:tripadvisor": "",
            "contact:yelp": "",
            "owner": "",
            "phone_1": "",
            "highchair": "",
            "bicycle_parking": "",
            "covered": "",
            "cuisine:homemade": "",
            "changing_table:fee": "",
            "language:ar": "",
            "payment:coins": "",
            "payment:notes": "",
            "cash_withdrawal": "",
            "karaoke": "",
            "addr:suburb": "",
            "was:amenity": "",
            "was:brewery": "",
            "lunch": "",
            "service:bicycle:rental": "",
            "indoor": "",
            "seating": "",
            "brand:en": "",
            "brand:zh": "",
            "drink": "",
            "office": "",
            "coffee": "",
            "diet:dairy_free": "",
            "drink:tea": "",
            "source:opening_hours": "",
            "leisure": "",
            "payment:titre_restaurant": "",
            "kids_area": "",
            "phone:FR": "",
            "fee": "",
            "name:de": "",
            "ele": "",
            "payment:ticket_restaurant": "",
            "amenity_1": "",
            "comment": "",
            "dog": "",
            "clothes": "",
            "diet:egg_free": "",
            "disabled:amenity": "",
            "source:ref:FR:SIREN": "",
            "name:nl": "",
            "indoor_seating": "",
            "genus": "",
            "natural": "",
            "name:tw": "",
            "contact:mobile": "",
            "drink:beer": "",
            "drink:coffee": "",
            "payment:visa_electron": "",
            "payment:maestro": "",
            "mapillary": "",
            "diet:sugar_free": "",
            "addr:district": "",
            "name:sr": "",
            "name:sr-Latn": "",
            "instagram": "",
            "opening_hours:url": "",
            "twitter": "",
            "disabled": "",
            "payment:apple_pay": "",
            "payment:credit_card": "",
        },
        "geometry": {"type": "Point", "coordinates": [2.3245488, 48.8319929]},
    }
    result = from_geojson_to_restaurant_json(input)
    assert {
        "id": "n175539450",
        "name": "Le Severo",
        "coordinates": (2.3245488, 48.8319929),
    } == result


def test_from_restaurant_json_to_pydantic():
    from_restaurant_json_to_pydantic(
        {
            "id": "n175539450",
            "name": "Le Severo",
            "coordinates": (2.3245488, 48.8319929),
        }
    )
