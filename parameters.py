# Detailing the parameters

base_url = 'https://api.idealista.com/3.5/'  # Base search url
country = 'es'  # Search country (es, it, pt)
language = 'es'  # Search language (es, it, pt, en, ca)
max_items = '50'  # Max items per call, the maximum set by Idealista is 50
operation = 'sale'  # Kind of operation (sale, rent)
property_type = 'homes'  # Type of property (homes, offices, premises, garages, bedrooms)
order = 'publicationDate'  # Order of the listings, consult documentation for all the available orders
center = '37.404762,-5.973923'  # Coordinates of the search center
distance = '900'  # Max distance from the center
sort = 'desc'  # How to sort the found items
maxprice = '190000'  # Max price of the listings


# Creating the URL with the parameters I want

def define_search_url():
    url = (base_url +
           country +
           '/search?operation=' + operation +
           '&maxItems=' + max_items +
           '&order=' + order +
           '&center=' + center +
           '&distance=' + distance +
           '&propertyType=' + property_type +
           '&sort=' + sort +
           '&numPage=%s' +
           '&maxPrice=' + maxprice +
           '&language=' + language)
    return url


url = define_search_url()
