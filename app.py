from chalice import Chalice

import json
import requests
import datetime

BART_API_KEY = "REMOVED FOR PUBLIC REPOSITORY"

app = Chalice(app_name='bartquery')

stations = [{'api_ai_value': 'twelfth street oakland city center',
             'written_name': '12th St. Oakland City Center',
             'abbr': '12TH',
             'spoken_name': 'twelfth street oakland city center',
             'synonyms': ['twelfth street',
                          'oakland city center',
                          'twelfth street oakland',
                          'oakland twelfth street']},
            {'api_ai_value': 'sixteenth street mission',
             'written_name': '16th St. Mission',
             'abbr': '16TH',
             'spoken_name': 'sixteenth street mission',
             'synonyms': ['sixteenth street mission', 'sixteenth street',
                          'sixteenth mission',
                          'sixteen mission']},
            {'api_ai_value': 'nineteenth street oakland',
             'written_name': '19th St. Oakland',
             'abbr': '19TH',
             'spoken_name': 'nineteeth street oakland',
             'synonyms': ['nineteenth oakland']},
            {'api_ai_value': '24th street mission',
             'written_name': '24th St. Mission',
             'abbr': '24TH',
             'spoken_name': '24th street mission',
             'synonyms': ['twenty fourth street mission']},
            {'api_ai_value': 'ashby',
             'written_name': 'Ashby',
             'abbr': 'ASHB',
             'spoken_name': 'ashby',
             'synonyms': []},
            {'api_ai_value': 'balboa park',
             'written_name': 'Balboa Park',
             'abbr': 'BALB',
             'spoken_name': 'balboa park',
             'synonyms': []},
            {'api_ai_value': 'bay fair',
             'written_name': 'Bay Fair',
             'abbr': 'BAYF',
             'spoken_name': 'bay fair',
             'synonyms': ['Bayfair']},
            {'api_ai_value': 'castro valley',
             'written_name': 'Castro Valley',
             'abbr': 'CAST',
             'spoken_name': 'castro valley',
             'synonyms': ['Castro']},
            {'api_ai_value': 'civic center u n plaza',
             'written_name': 'Civic Center/UN Plaza',
             'abbr': 'CIVC',
             'spoken_name': 'civic center u n plaza',
             'synonyms': ['Civic Center', 'UN Plaza']},
            {'api_ai_value': 'coliseum',
             'written_name': 'Coliseum',
             'abbr': 'COLS',
             'spoken_name': 'coliseum',
             'synonyms': []},
            {'api_ai_value': 'colma',
             'written_name': 'Colma',
             'abbr': 'COLM',
             'spoken_name': 'colma',
             'synonyms': []},
            {'api_ai_value': 'concord',
             'written_name': 'Concord',
             'abbr': 'CONC',
             'spoken_name': 'concord',
             'synonyms': []},
            {'api_ai_value': 'daly city',
             'written_name': 'Daly City',
             'abbr': 'DALY',
             'spoken_name': 'daly city',
             'synonyms': []},
            {'api_ai_value': 'downtown berkeley',
             'written_name': 'Downtown Berkeley',
             'abbr': 'DBRK',
             'spoken_name': 'downtown berkeley',
             'synonyms': ['Berkeley']},
            {'api_ai_value': 'dublin pleasanton',
             'written_name': 'Dublin/Pleasanton',
             'abbr': 'DUBL',
             'spoken_name': 'dublin pleasanton',
             'synonyms': ['Dublin', 'Pleasanton']},
            {'api_ai_value': 'el cerrito del norte',
             'written_name': 'El Cerrito del Norte',
             'abbr': 'DELN',
             'spoken_name': 'el cerrito del norte',
             'synonyms': ['El cerrito norte', 'el cerrito north', 'cerrito norte']},
            {'api_ai_value': 'el cerrito plaza',
             'written_name': 'El Cerrito Plaza',
             'abbr': 'PLZA',
             'spoken_name': 'el cerrito plaza',
             'synonyms': ['cerrito plaza']},
            {'api_ai_value': 'embarcadero',
             'written_name': 'Embarcadero',
             'abbr': 'EMBR',
             'spoken_name': 'embarcadero',
             'synonyms': []},
            {'api_ai_value': 'fremont',
             'written_name': 'Fremont',
             'abbr': 'FRMT',
             'spoken_name': 'fremont',
             'synonyms': []},
            {'api_ai_value': 'fruitvale',
             'written_name': 'Fruitvale',
             'abbr': 'FTVL',
             'spoken_name': 'fruitvale',
             'synonyms': []},
            {'api_ai_value': 'glen park',
             'written_name': 'Glen Park',
             'abbr': 'GLEN',
             'spoken_name': 'glen park',
             'synonyms': []},
            {'api_ai_value': 'hayward',
             'written_name': 'Hayward',
             'abbr': 'HAYW',
             'spoken_name': 'hayward',
             'synonyms': []},
            {'api_ai_value': 'lafayette',
             'written_name': 'Lafayette',
             'abbr': 'LAFY',
             'spoken_name': 'lafayette',
             'synonyms': []},
            {'api_ai_value': 'lake merritt',
             'written_name': 'Lake Merritt',
             'abbr': 'LAKE',
             'spoken_name': 'lake merritt',
             'synonyms': []},
            {'api_ai_value': 'macarthur',
             'written_name': 'MacArthur',
             'abbr': 'MCAR',
             'spoken_name': 'macarthur',
             'synonyms': []},
            {'api_ai_value': 'millbrae',
             'written_name': 'Millbrae',
             'abbr': 'MLBR',
             'spoken_name': 'millbrae',
             'synonyms': []},
            {'api_ai_value': 'montgomery',
             'written_name': 'Montgomery St.',
             'abbr': 'MONT',
             'spoken_name': 'montgomery',
             'synonyms': ['Montgomery Street', 'Montgomory']},
            {'api_ai_value': 'north berkeley',
             'written_name': 'North Berkeley',
             'abbr': 'NBRK',
             'spoken_name': 'north berkeley',
             'synonyms': []},
            {'api_ai_value': 'north concord/martinez',
             'written_name': 'North Concord/Martinez',
             'abbr': 'NCON',
             'spoken_name': 'north concord/martinez',
             'synonyms': ['North Concord', 'Martinez']},
            {'api_ai_value': "oakland international airport",
             'written_name': "Oakland Int'l Airport",
             'abbr': 'OAKL',
             'spoken_name': "oakland international airport",
             'synonyms': ['O.A.K', 'Oakland Airport', 'Oakland International Airport']},
            {'api_ai_value': 'orinda',
             'written_name': 'Orinda',
             'abbr': 'ORIN',
             'spoken_name': 'orinda',
             'synonyms': []},
            {'api_ai_value': 'pittsburg bay point',
             'written_name': 'Pittsburg/Bay Point',
             'abbr': 'PITT',
             'spoken_name': 'pittsburg bay point',
             'synonyms': ['Pittsburg', 'Pittsburg Bay Point', 'Bay Point']},
            {'api_ai_value': 'pleasant hill/contra costa centre',
             'written_name': 'Pleasant Hill Contra Costa Centre',
             'abbr': 'PHIL',
             'spoken_name': 'pleasant hill contra costa centre',
             'synonyms': ['Pleasant Hill', 'Contra Costa Centre']},
            {'api_ai_value': 'powell street',
             'written_name': 'Powell St.',
             'abbr': 'POWL',
             'spoken_name': 'powell street',
             'synonyms': ['Powell']},
            {'api_ai_value': 'richmond',
             'written_name': 'Richmond',
             'abbr': 'RICH',
             'spoken_name': 'richmond',
             'synonyms': []},
            {'api_ai_value': 'rockridge',
             'written_name': 'Rockridge',
             'abbr': 'ROCK',
             'spoken_name': 'rockridge',
             'synonyms': []},
            {'api_ai_value': 'san bruno',
             'written_name': 'San Bruno',
             'abbr': 'SBRN',
             'spoken_name': 'san bruno',
             'synonyms': []},
            {'api_ai_value': "san francisco international airport",
             'written_name': "San Francisco Int'l Airport",
             'abbr': 'SFIA',
             'spoken_name': "san francisco international airport",
             'synonyms': ['SFO', 'S.F.O.']},
            {'api_ai_value': 'san leandro',
             'written_name': 'San Leandro',
             'abbr': 'SANL',
             'spoken_name': 'san leandro',
             'synonyms': []},
            {'api_ai_value': 'south hayward',
             'written_name': 'South Hayward',
             'abbr': 'SHAY',
             'spoken_name': 'south hayward',
             'synonyms': []},
            {'api_ai_value': 'south san francisco',
             'written_name': 'South San Francisco',
             'abbr': 'SSAN',
             'spoken_name': 'south san francisco',
             'synonyms': []},
            {'api_ai_value': 'union city',
             'written_name': 'Union City',
             'abbr': 'UCTY',
             'spoken_name': 'union city',
             'synonyms': []},
            {'api_ai_value': 'walnut creek',
             'written_name': 'Walnut Creek',
             'abbr': 'WCRK',
             'spoken_name': 'walnut creek',
             'synonyms': []},
            {'api_ai_value': 'west dublin pleasanton',
             'written_name': 'West Dublin/Pleasanton',
             'abbr': 'WDUB',
             'spoken_name': 'west dublin pleasanton',
             'synonyms': ['West Dublin']},
            {'api_ai_value': 'west oakland',
             'written_name': 'West Oakland',
             'abbr': 'WOAK',
             'spoken_name': 'west oakland',
             'synonyms': []},
            {'api_ai_value': 'warm springs south fremont',
             'written_name': 'Warm Springs/South Fremont',
             'abbr': 'WARM',
             'spoken_name': 'warm springs south fremont',
             'synonyms': ['Warm Springs', 'South Fremont']}
            ]

@app.route('/', methods = ['GET'])
def index():
    return {'hello' : 'world'}


@app.route('/webhook', methods = ['POST'])
def webhook():
    return lambda_handler(app.current_request.json_body, None)

def get_origin_name(event):
    """get the station name from the event"""
    return event['result']['parameters']['origin_station']['origin']


def get_direction(event):
    """get the direction from the event"""
    return event['result']['parameters']['direction']


def get_destination(event):
    """get the destination from the event"""
    if event['result']['parameters']['destination_station']:
        return event['result']['parameters']['destination_station']['destination']
    else:
        return ""

def get_direction_bound_routes(direction):
    """finds routes currently direction bound"""

    direction_bound_routes = []
    trains = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 19, 20]

    for track in trains:
        parameters = {'cmd': "routeinfo", 'key': BART_API_KEY, 'route': track, 'date': "now", 'json': "y"}
        response = requests.get('http://api.bart.gov/api/route.aspx', params=parameters)
        route = json.loads(response.text)["root"]["routes"]["route"]
        routeDirection = route["direction"]
        routeID = route["routeID"]
        if routeDirection == direction:
            direction_bound_routes.append(routeID)

    return direction_bound_routes


def get_station_schedule(stationabbr):
    parameters = {'cmd': "stnsched", 'key': BART_API_KEY, 'orig': stationabbr, 'date': "now", 'json': "y"}
    response = requests.get('https://api.bart.gov/api/sched.aspx', params=parameters)
    return json.loads(response.text)['root']['station']['item']


def get_station_abbr(station):

    for place in stations:
        if place['written_name'] == station:
            return place["abbr"]

def get_earliest_time(schedule_or_route, route_type, direction_bound_routes):

    # set route_key to proper dictionary key to index into a schedule json dictionary or
    if route_type == "direction":
        route_key = "@origTime"
    elif route_type == "destination":
        route_key = "@origTimeMin"

    # instantiate time variables (second_earliest_time is after 10 minutes so that getting to station may be feasible)
    earliest_time = float('inf')
    second_earliest_time = float('inf')

    for route in schedule_or_route:

        # checks if not direction bound route or if route is direction bound
        if not direction_bound_routes or route["@line"] in direction_bound_routes:  # checks if route is direction bound
            # set up time stamps and time til departure
            curr_time = datetime.datetime.now().strftime('%H:%M %p')
            depart_time = route[route_key]
            FMT = '%H:%M %p'
            tdelta = datetime.datetime.strptime(depart_time, FMT) - datetime.datetime.strptime(curr_time, FMT)

            # if departure in future
            if (tdelta.seconds // 60) % 60 > 0:

                # earliest time of departure from origin
                if earliest_time > (tdelta.seconds // 60) % 60:
                    earliest_time = (tdelta.seconds // 60) % 60

                # earliest time of departure after 10 minutes
                elif 10 < (tdelta.seconds // 60) % 60 and earliest_time < (tdelta.seconds // 60) % 60:
                    second_earliest_time = min(second_earliest_time, (tdelta.seconds // 60) % 60)

    return earliest_time, second_earliest_time

def dest_route(query_orig, query_dest, station, destination):

    retval = {}

    # retrieves routes from orig to dest
    parameters = {'cmd': 'depart', 'key': BART_API_KEY, 'orig': query_orig, 'dest': query_dest, 'time': 'now', 'json': 'y'}
    response = requests.get('http://api.bart.gov/api/sched.aspx', params=parameters)
    routes = json.loads(response.text)['root']['schedule']['request']['trip']

    # instantiate time variables (second_earliest_time is after 10 minutes so that getting to station may be feasible)
    earliest_time, second_earliest_time = get_earliest_time(routes, "destination", [])

    # format departure time as "shortly" if earliest time is less than 2 minutes
    departure_time = None
    if earliest_time < 2:
        departure_time = " shortly."
    else:
        departure_time = " in " + str(earliest_time) + " minutes."

    # format dictionary
    retval["speech"] = "The next trip from " + station + " station to " + destination + " station leaves" + \
                       departure_time + \
                       " Then, another trip will depart in " + str(second_earliest_time) + " minutes."

    retval["display API"] = "The next trip from " + station.title() + " station to " + destination.title() + \
                            " station leaves" + departure_time + " Then, another trip will depart in " + \
                            str(second_earliest_time) + " minutes."

    retval["Source"] = "BART API"

    return retval


def direction_route(query_orig, query_direction, station):

    retval = {}

    # finds routes currently direction bound and saves into a list of ROUTE IDs
    direction_bound_routes = get_direction_bound_routes(query_direction)

    # receives schedule of routes from origin station
    schedule = get_station_schedule(query_orig)

    # instantiate time variables (second_earliest_time is after 10 minutes so that getting to station may be feasible)
    earliest_time, second_earliest_time = get_earliest_time(schedule, "direction", direction_bound_routes)

    # format departure time as "shortly" if earliest time is less than 2 minutes
    departure_time = None
    if earliest_time < 2:
        departure_time = " shortly."
    else:
        departure_time = " in " + str(earliest_time) + " minutes."

    # format dictionary
    retval["speech"] = "The next " + query_direction + " bound train leaves " + station + " station" + departure_time +\
                       " Then, another " + query_direction + " bound train will depart in " +\
                       str(second_earliest_time) + " minutes."

    retval["display API"] = "The next " + query_direction + " bound train leaves " + station.title() + " station" +\
                            departure_time + " Then, another " + query_direction + " bound train will depart in " +\
                            str(second_earliest_time) + " minutes."

    retval["Source"] = "BART API"

    return retval


def lambda_handler(event, context):
    """Takes in an event from Api.ai, through Api Gateway.
    Returns a dict with keys "speech", "displayText", and "Source".
    Source is always the "BART API"    """

    retval = {}

    # retrieve event information (i.e. station name and direction)
    station = get_origin_name(event)
    destination = get_destination(event)
    query_direction = get_direction(event).title()

    # finds abbreviation for origin and dest station
    query_orig = get_station_abbr(station)
    if destination:
        query_dest = get_station_abbr(destination)
        return dest_route(query_orig, query_dest, station, destination)

    else:
        return direction_route(query_orig, query_direction, station)
