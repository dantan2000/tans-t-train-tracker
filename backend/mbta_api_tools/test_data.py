# Example data for Tests


# Mock data for for routes API call
routesData = {
    "data": [
        {
            "attributes": {
                "color": "DA291C",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Ashmont/Braintree",
                    "Alewife"
                ],
                "direction_names": [
                    "South",
                    "North"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Red Line",
                "short_name": "",
                "sort_order": 10010,
                "text_color": "FFFFFF",
                "type": 1
            },
            "id": "Red",
            "links": {
                "self": "/routes/Red"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Red",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "DA291C",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Mattapan",
                    "Ashmont"
                ],
                "direction_names": [
                    "Outbound",
                    "Inbound"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Mattapan Trolley",
                "short_name": "",
                "sort_order": 10011,
                "text_color": "FFFFFF",
                "type": 0
            },
            "id": "Mattapan",
            "links": {
                "self": "/routes/Mattapan"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Mattapan",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "ED8B00",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Forest Hills",
                    "Oak Grove"
                ],
                "direction_names": [
                    "South",
                    "North"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Orange Line",
                "short_name": "",
                "sort_order": 10020,
                "text_color": "FFFFFF",
                "type": 1
            },
            "id": "Orange",
            "links": {
                "self": "/routes/Orange"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Orange",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "00843D",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Boston College",
                    "Government Center"
                ],
                "direction_names": [
                    "West",
                    "East"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Green Line B",
                "short_name": "B",
                "sort_order": 10032,
                "text_color": "FFFFFF",
                "type": 0
            },
            "id": "Green-B",
            "links": {
                "self": "/routes/Green-B"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Green",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "00843D",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Cleveland Circle",
                    "Government Center"
                ],
                "direction_names": [
                    "West",
                    "East"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Green Line C",
                "short_name": "C",
                "sort_order": 10033,
                "text_color": "FFFFFF",
                "type": 0
            },
            "id": "Green-C",
            "links": {
                "self": "/routes/Green-C"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Green",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "00843D",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Riverside",
                    "North Station"
                ],
                "direction_names": [
                    "West",
                    "East"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Green Line D",
                "short_name": "D",
                "sort_order": 10034,
                "text_color": "FFFFFF",
                "type": 0
            },
            "id": "Green-D",
            "links": {
                "self": "/routes/Green-D"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Green",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "00843D",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Heath Street",
                    "Union Square"
                ],
                "direction_names": [
                    "West",
                    "East"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Green Line E",
                "short_name": "E",
                "sort_order": 10035,
                "text_color": "FFFFFF",
                "type": 0
            },
            "id": "Green-E",
            "links": {
                "self": "/routes/Green-E"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Green",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        },
        {
            "attributes": {
                "color": "003DA5",
                "description": "Rapid Transit",
                "direction_destinations": [
                    "Bowdoin",
                    "Wonderland"
                ],
                "direction_names": [
                    "West",
                    "East"
                ],
                "fare_class": "Rapid Transit",
                "long_name": "Blue Line",
                "short_name": "",
                "sort_order": 10040,
                "text_color": "FFFFFF",
                "type": 1
            },
            "id": "Blue",
            "links": {
                "self": "/routes/Blue"
            },
            "relationships": {
                "line": {
                    "data": {
                        "id": "line-Blue",
                        "type": "line"
                    }
                }
            },
            "type": "route"
        }
    ],
    "jsonapi": {
        "version": "1.0"
    }
}

# Mock Data for stops API call
stopsData = {
    "data": [
        {
            "attributes": {
                "address": "Heath St and South Huntington Ave, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.328316,
                "location_type": 1,
                "longitude": -71.110252,
                "municipality": "Boston",
                "name": "Heath Street",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-hsmnl",
            "links": {
                "self": "/stops/place-hsmnl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-hsmnl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "100 South Huntington Ave, Boston, MA 02130",
                "at_street": None,
                "description": None,
                "latitude": 42.330139,
                "location_type": 1,
                "longitude": -71.111313,
                "municipality": "Boston",
                "name": "Back of the Hill",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-bckhl",
            "links": {
                "self": "/stops/place-bckhl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-bckhl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "South Huntington Ave and Huntington Ave, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.331684,
                "location_type": 1,
                "longitude": -71.111931,
                "municipality": "Boston",
                "name": "Riverway",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-rvrwy",
            "links": {
                "self": "/stops/place-rvrwy"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-rvrwy"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Mission Park Dr, Boston, MA 02115",
                "at_street": None,
                "description": None,
                "latitude": 42.333195,
                "location_type": 1,
                "longitude": -71.109756,
                "municipality": "Boston",
                "name": "Mission Park",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-mispk",
            "links": {
                "self": "/stops/place-mispk"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-mispk"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Fenwood Rd, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.333706,
                "location_type": 1,
                "longitude": -71.105728,
                "municipality": "Boston",
                "name": "Fenwood Road",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-fenwd",
            "links": {
                "self": "/stops/place-fenwd"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-fenwd"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Francis St, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.334229,
                "location_type": 1,
                "longitude": -71.104609,
                "municipality": "Boston",
                "name": "Brigham Circle",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-brmnl",
            "links": {
                "self": "/stops/place-brmnl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-brmnl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Longwood Ave, Boston, MA 02115",
                "at_street": None,
                "description": None,
                "latitude": 42.33596,
                "location_type": 1,
                "longitude": -71.100052,
                "municipality": "Boston",
                "name": "Longwood Medical Area",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-lngmd",
            "links": {
                "self": "/stops/place-lngmd"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-lngmd"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Ruggles St, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.337711,
                "location_type": 1,
                "longitude": -71.095512,
                "municipality": "Boston",
                "name": "Museum of Fine Arts",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-mfa",
            "links": {
                "self": "/stops/place-mfa"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-mfa"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Opera Pl, Boston, MA 02115",
                "at_street": None,
                "description": None,
                "latitude": 42.340401,
                "location_type": 1,
                "longitude": -71.088806,
                "municipality": "Boston",
                "name": "Northeastern University",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-nuniv",
            "links": {
                "self": "/stops/place-nuniv"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-nuniv"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Massachusetts Ave and Huntington Ave, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.342687,
                "location_type": 1,
                "longitude": -71.085056,
                "municipality": "Boston",
                "name": "Symphony",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-symcl",
            "links": {
                "self": "/stops/place-symcl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-symcl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Huntington Ave and Belvidere St, Boston, MA 02199",
                "at_street": None,
                "description": None,
                "latitude": 42.34557,
                "location_type": 1,
                "longitude": -71.081696,
                "municipality": "Boston",
                "name": "Prudential",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-prmnl",
            "links": {
                "self": "/stops/place-prmnl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-prmnl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Boylston St and Dartmouth St, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.349974,
                "location_type": 1,
                "longitude": -71.077447,
                "municipality": "Boston",
                "name": "Copley",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-coecl",
            "links": {
                "self": "/stops/place-coecl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-coecl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Arlington St and Boylston St, Boston, MA 02116",
                "at_street": None,
                "description": None,
                "latitude": 42.351902,
                "location_type": 1,
                "longitude": -71.070893,
                "municipality": "Boston",
                "name": "Arlington",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-armnl",
            "links": {
                "self": "/stops/place-armnl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-armnl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Boylston St and Tremont St, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.35302,
                "location_type": 1,
                "longitude": -71.06459,
                "municipality": "Boston",
                "name": "Boylston",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 2
            },
            "id": "place-boyls",
            "links": {
                "self": "/stops/place-boyls"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-boyls"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Tremont St and Winter St, Boston, MA 02108",
                "at_street": None,
                "description": None,
                "latitude": 42.356395,
                "location_type": 1,
                "longitude": -71.062424,
                "municipality": "Boston",
                "name": "Park Street",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-pktrm",
            "links": {
                "self": "/stops/place-pktrm"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-pktrm"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Cambridge St and Court St, Boston, MA",
                "at_street": None,
                "description": None,
                "latitude": 42.359705,
                "location_type": 1,
                "longitude": -71.059215,
                "municipality": "Boston",
                "name": "Government Center",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-gover",
            "links": {
                "self": "/stops/place-gover"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-gover"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "136 Blackstone St, Boston, MA 02109",
                "at_street": None,
                "description": None,
                "latitude": 42.363021,
                "location_type": 1,
                "longitude": -71.05829,
                "municipality": "Boston",
                "name": "Haymarket",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-haecl",
            "links": {
                "self": "/stops/place-haecl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-haecl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "135 Causeway St, Boston, MA 02114",
                "at_street": None,
                "description": None,
                "latitude": 42.365577,
                "location_type": 1,
                "longitude": -71.06129,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-north",
            "links": {
                "self": "/stops/place-north"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-north"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": {
                        "id": "CR-zone-1A",
                        "type": "zone"
                    }
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "Leverett Circle and Nashua St, Boston, MA 02114",
                "at_street": None,
                "description": None,
                "latitude": 42.366664,
                "location_type": 1,
                "longitude": -71.067666,
                "municipality": "Boston",
                "name": "Science Park/West End",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-spmnl",
            "links": {
                "self": "/stops/place-spmnl"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-spmnl"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "3 North First St, Cambridge, MA 02141",
                "at_street": None,
                "description": None,
                "latitude": 42.371572,
                "location_type": 1,
                "longitude": -71.076584,
                "municipality": "Cambridge",
                "name": "Lechmere",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-lech",
            "links": {
                "self": "/stops/place-lech"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-lech"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        },
        {
            "attributes": {
                "address": "50 Prospect St, Somerville, MA 02143",
                "at_street": None,
                "description": None,
                "latitude": 42.377359,
                "location_type": 1,
                "longitude": -71.094761,
                "municipality": "Somerville",
                "name": "Union Square",
                "on_street": None,
                "platform_code": None,
                "platform_name": None,
                "vehicle_type": None,
                "wheelchair_boarding": 1
            },
            "id": "place-unsqu",
            "links": {
                "self": "/stops/place-unsqu"
            },
            "relationships": {
                "facilities": {
                    "links": {
                        "related": "/facilities/?filter[stop]=place-unsqu"
                    }
                },
                "parent_station": {
                    "data": None
                },
                "zone": {
                    "data": None
                }
            },
            "type": "stop"
        }
    ],
    "jsonapi": {
        "version": "1.0"
    }
}

# Mock Data for predictions API call
predictionsData = {
    "data": [
        {
            "attributes": {
                "arrival_time": "2022-07-31T18:10:23-04:00",
                "departure_time": "2022-07-31T18:10:35-04:00",
                "direction_id": 0,
                "schedule_relationship": None,
                "status": None,
                "stop_sequence": 670
            },
            "id": "prediction-52145302-70257-670",
            "relationships": {
                "route": {
                    "data": {
                        "id": "Green-E",
                        "type": "route"
                    }
                },
                "stop": {
                    "data": {
                        "id": "70257",
                        "type": "stop"
                    }
                },
                "trip": {
                    "data": {
                        "id": "52145302",
                        "type": "trip"
                    }
                },
                "vehicle": {
                    "data": {
                        "id": "G-10015",
                        "type": "vehicle"
                    }
                }
            },
            "type": "prediction"
        },
        {
            "attributes": {
                "arrival_time": "2022-07-31T18:18:52-04:00",
                "departure_time": "2022-07-31T18:19:04-04:00",
                "direction_id": 0,
                "schedule_relationship": None,
                "status": None,
                "stop_sequence": 670
            },
            "id": "prediction-52145303-70257-670",
            "relationships": {
                "route": {
                    "data": {
                        "id": "Green-E",
                        "type": "route"
                    }
                },
                "stop": {
                    "data": {
                        "id": "70257",
                        "type": "stop"
                    }
                },
                "trip": {
                    "data": {
                        "id": "52145303",
                        "type": "trip"
                    }
                },
                "vehicle": {
                    "data": {
                        "id": "G-10029",
                        "type": "vehicle"
                    }
                }
            },
            "type": "prediction"
        },
        {
            "attributes": {
                "arrival_time": "2022-07-31T18:26:23-04:00",
                "departure_time": "2022-07-31T18:26:35-04:00",
                "direction_id": 0,
                "schedule_relationship": None,
                "status": None,
                "stop_sequence": 670
            },
            "id": "prediction-52145304-70257-670",
            "relationships": {
                "route": {
                    "data": {
                        "id": "Green-E",
                        "type": "route"
                    }
                },
                "stop": {
                    "data": {
                        "id": "70257",
                        "type": "stop"
                    }
                },
                "trip": {
                    "data": {
                        "id": "52145304",
                        "type": "trip"
                    }
                },
                "vehicle": {
                    "data": {
                        "id": "G-10184",
                        "type": "vehicle"
                    }
                }
            },
            "type": "prediction"
        },
        {
            "attributes": {
                "arrival_time": "2022-07-31T18:35:45-04:00",
                "departure_time": "2022-07-31T18:35:57-04:00",
                "direction_id": 0,
                "schedule_relationship": None,
                "status": None,
                "stop_sequence": 670
            },
            "id": "prediction-52145305-70257-670",
            "relationships": {
                "route": {
                    "data": {
                        "id": "Green-E",
                        "type": "route"
                    }
                },
                "stop": {
                    "data": {
                        "id": "70257",
                        "type": "stop"
                    }
                },
                "trip": {
                    "data": {
                        "id": "52145305",
                        "type": "trip"
                    }
                },
                "vehicle": {
                    "data": {
                        "id": "G-10071",
                        "type": "vehicle"
                    }
                }
            },
            "type": "prediction"
        }
    ],
    "jsonapi": {
        "version": "1.0"
    }
}

# Mock Empty Data
# Used for queries with invalid routes, stops, and directions
emptyData = {
    "data": [],
    "jsonapi": {
        "version": "1.0"
    }
}
