from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    # Return the Pygal 2-digit country code for given country.
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If country was not found, return none
    return None

# COUNTRIES är en dict som har key:value t.ex. 'se':'Sweden', genom att skriva COUNTRIES.items() blir det en lista
# Genom att skriva for k,v in COUNTRIES.items() får man både key + value i samma loop och kan göra krav på båda

