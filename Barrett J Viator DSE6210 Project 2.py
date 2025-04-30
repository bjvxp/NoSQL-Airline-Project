"""
Created on Thurs Oct  17 2024
DSE6210 Project 2

@author: Barrett J. Viator
"""


from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://viatorb:Learningmongodb@cluster0.sz2tw.mongodb.net/') 

# Name the new database and the new collection name
project_2_database = 'Airline'
agent_collection = 'travel agent'
itin_res_collection = 'itinerary reservations'
res_payment_collection = 'reservation payments'
pass_collection = 'passengers'
itin_leg_collection = 'itinerary legs'
flight_legs_collection = 'flight legs'
airport_collection = 'airports'
flight_sched_collection =  'flight schedule'
ref_cal_collection = 'reference callendar'
flight_cost_collection = "flight cost"

# Create a new database
new_database = client[project_2_database]

db = client['Airline']

# Create a new collection
agent_col = new_database[agent_collection]
res_pay_col = new_database[res_payment_collection]
pass_col = new_database[pass_collection]
itiner_leg_col = new_database[itin_leg_collection]
itin_res_col = new_database[itin_res_collection]
flight_leg_col = new_database[flight_legs_collection]
airport_col = new_database[airport_collection]
flight_cost_col = new_database[flight_cost_collection]
flight_sched_col = new_database[flight_sched_collection]
ref_cal_col = new_database[ref_cal_collection]
                           
# booking agents collection

travel_agents = [
    {
        "_id": "045231",
        "agent_name": "Sue Jones",
        "agent_details": "Associate"
    },
    {
        "_id": "067456",
        "agent_name": "Brad Collins",
        "agent_details": "VP"
    },
    {
        "_id": "036524",
        "agent_name": "Ann Rice",
        "agent_details": "Associate"
    }
]
inserted_agent_data = agent_col.insert_many(travel_agents)



#itinerary reservations collection

itin_res = [
    {
        "_id": "15457568",
        "agent_id": "045231",
        "passenger_id": "7463826",
        "reservation_status_code": "01",
        "payment_amount": 982,
        "usual_aircraft_type_code": "B747",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "ticket_type_code": "01",
        "travel_class_code": "75",
        "date_reservation_made": "2023-10-12",
        "number_in_party": 1
    },
    {
        "_id": "24668346",
        "agent_id": "067456",
        "passenger_id": "5885922",
        "reservation_status_code": "01",
        "payment_amount": 473,
        "usual_aircraft_type_code": "B360",
        "origin_airport_code": "LFT",
        "destination_airport_code": "DFW",
        "ticket_type_code": "01",
        "travel_class_code":"75",
        "date_reservation_made": "2023-10-12",
        "number_in_party": 1
    },
    {
        "_id": "35635773",
        "agent_id": "045231",
        "passenger_id": "9284293",
        "reservation_status_code": "01",
        "payment_amount": 564,
        "usual_aircraft_type_code": "564",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "ticket_type_code": "01",
        "travel_class_code": "75",
        "date_reservation_made": "2023-10-12",
        "number_in_party": 1
    },
    {
        "_id": "36725613",
        "agent_id": "036524",
        "passenger_id": "7375758",
        "reservation_status_code": "01",
        "payment_amount": 638,
        "usual_aircraft_type_code": "638",
        "origin_airport_code": "MSY",
        "destination_airport_code": "ATL",
        "ticket_type_code": "01",
        "travel_class_code":"75",
        "date_reservation_made": "2023-10-12",
        "number_in_party": 1
    },
    {
        "_id": "74677424",
        "agent_id": "045231",
        "passenger_id": "2772849",
        "reservation_status_code": "01",
        "payment_amount": 342,
        "usual_aircraft_type_code": "342",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "ticket_type_code": "01",
        "travel_class_code": "75",
        "date_reservation_made": "2023-10-12",
        "number_in_party": 1
    }
]


inserted_itin_res_data = itin_res_col.insert_many(itin_res)


# reservation payments collection

res_pay = [
    {
        "_id": "AV6345",
        "pass_id": "7463826",
        "flight_number": "AA321",
        "reservation_id": "15457568",
        "payment_status_code": "05",
        "payment_date": "10-12-2023",
        "payment_amount": 982
    },
    {
        "_id": "SD3267",
        "pass_id": "5885922",
        "flight_number": "AA321",
        "reservation_id": "24668346",
        "payment_status_code": "05",
        "payment_date": "02-04-2024",
        "payment_amount": 473
    },
    {
        "_id": "DF3585",
        "pass_id": "9284293",
        "flight_number": "AA985",
        "reservation_id": "35635773",
        "payment_status_code": "05",
        "payment_date": "05-11-2024",
        "payment_amount": 564
    },
    {
        "_id": "LP3563",
        "pass_id": "7375758",
        "flight_number": "AA642",
        "reservation_id": "36725613",
        "payment_status_code": "05",
        "payment_date": "08-06-2023",
        "payment_amount": 638
    },
    {
        "_id": "RF2573",
        "pass_id": "2772849",
        "flight_number": "AA321",
        "reservation_id": "74677424",
        "payment_status_code": "05",
        "payment_date": "09-05-2024",
        "payment_amount": 342
    }
]


inserted_res_payment_data = res_pay_col.insert_many(res_pay)

# passenger collection

pass_collection = [
    {
        "_id": "7463826",
        "first_name": "Mila",
        "second_name": "Dina",
        "last_name": "Romanova",
        "phone_number": "19287256",
        "email_address": "mdr@live.com",
        "address_lines": "2782 1st St",
        "city": "New York",
        "state_province_county": "NY",
        "country": "USA",
        "other_passenger_details": "Member"
    },
    {
        "_id": "5885922",
        "first_name": "Laura",
        "second_name": "Kelly",
        "last_name": "Juarez",
        "phone_number": "17389390",
        "email_address": "lkj25@gmail.com",
        "address_lines": "1080 Tree Cove",
        "city": "Dallas",
        "state_province_county": "TX",
        "country": "USA",
        "other_passenger_details": "Gold Status"
    },
    {
        "_id": "9284293",
        "first_name": "Frank",
        "second_name": "Will",
        "last_name": "Craft",
        "phone_number": "18373845",
        "email_address": "fwk6@apple.com",
        "address_lines": "25 Smith St",
        "city": "Tempe",
        "state_province_county": "AZ",
        "country": "USA",
        "other_passenger_details": "guest checkout"
    },
    {
        "_id": "7375758",
        "first_name": "Jian",
        "second_name": "Li",
        "last_name": "Cho",
        "phone_number": "12384658",
        "email_address": "jlc@yahoo.com",
        "address_lines": "9876 Rue Verdun",
        "city": "Montreal",
        "state_province_county": "CAN",
        "country": "Canada",
        "other_passenger_details": "Member"
    },
    {
        "_id": "2772849",
        "first_name": "Joe",
        "second_name": "Preston",
        "last_name": "Hue",
        "phone_number": "13458293",
        "email_address": "jph@windows.com",
        "address_lines": "47 Turnpike Lane",
        "city": "LA",
        "state_province_county": "USA",
        "country": "USA",
        "other_passenger_details": "Gold Status"
    }
]

inserted_passenger_data = pass_col.insert_many(pass_collection)


# itinerary legs collection

itin_leg = [
    {
        "_id": {
            "reservation_id": "15457568",
            "leg_id": "056432"
        },
        "flight_number": "AA321",
        "airline_code": "LFT",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "departure_date_time":'2024-01-01 17:00:00',
        "arrival_date_time": '2024-01-01 20:00:00',
        "actual_departure_time": '2024-01-01 17:30:00',
        "actual_arrival_time": '2024-01-01 20:30:00',
        "departure_efficiency": False
    },
    {
        "_id": {
            "reservation_id": "24668346",
            "leg_id": "056432"
        },
        "flight_number": "AA321",
        "airline_code": "LFT",
        "origin_airport_code": "MSY",
        "destination_airport_code": "DFW",
        "departure_date_time": '2024-01-01 17:00:00',
        "arrival_date_time": '2024-01-01 20:00:00',
        "actual_departure_time": '2024-01-01 17:30:00',
        "actual_arrival_time": '2024-01-01 20:30:00',
        "departure_efficiency": False
    },
    {
        "_id": {
            "reservation_id": "35635773",
            "leg_id": "656833"
        },
        "flight_number": "AA642",
        "airline_code": "MSY",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "departure_date_time": '2024-01-02 14:00:00',
        "arrival_date_time": '2024-01-02 15:00:00',
        "actual_departure_time": '2024-01-02 14:00:00',
        "actual_arrival_time": '2024-01-02 15:00:00',
        "departure_efficiency": True
    },
    {
        "_id": {
            "reservation_id": "36725613",
            "leg_id": "345795"
        },
        "flight_number": "AA985",
        "airline_code": "MSY",
        "origin_airport_code": "MSY",
        "destination_airport_code": "ATL",
        "departure_date_time": '2024-01-03 15:00:00',
        "arrival_date_time": '2024-01-02 17:00:00',
        "actual_departure_time":'2024-01-03 15:00:00',
        "actual_arrival_time": '2024-01-02 17:00:00',
        "departure_efficiency": True
    },
    {
        "_id": {
            "reservation_id": "74677424",
            "leg_id": "056432"
        },
        "flight_number": "AA321",
        "airline_code": "LFT",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "departure_date_time": '2024-01-01 17:00:00',
        "arrival_date_time": '2024-01-01 20:00:00',
        "actual_departure_time": '2024-01-01 17:30:00',
        "actual_arrival_time": '2024-01-01 20:30:00',
        "departure_efficiency": False
    }
]


inserted_itin_leg_data = itiner_leg_col.insert_many(itin_leg)

# legs collection

flight_leg = [
    {
        "_id": "056432",
        "flight_number": "AA321",
        "airline_code": "LFT",
        "origin_airport_code": "LFT",
        "destination_airport_code": "JFK",
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    },
    {
        "_id": "656833",
        "flight_number": "AA642",
        "airline_code": "MSY",
        "origin_airport_code": "LFT",
        "destination_airport_code": "DFW",
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    },
    {
        "_id": "345795",
        "flight_number": "AA985",
        "airline_code": "MSY",
        "origin_airport_code": "MSY",
        "destination_airport_code": "ATL",
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    }
]

inserted_flight_leg_data = flight_leg_col.insert_many(flight_leg)


#airports collection
airports = [
    {
        "_id": "LFT",
        "airport_name": "Lafayette Regional",
        "airport_location": "Lafayette",
        "other_details": "Regional"
    },
    {
        "_id": "MSY",
        "airport_name": "Louis Armstrong Airport",
        "airport_location": "New Orleans",
        "other_details": "International"
    },
    {
        "_id": "JFK",
        "airport_name": "John F. Kennedy Airport",
        "airport_location": "New York City",
        "other_details": "International"
    },
    {
        "_id": "DFW",
        "airport_name": "Dallas International Airport",
        "airport_location": "Dallas",
        "other_details": "International"
    },
    {
        "_id": "ATL",
        "airport_name": "Atlanta International Airport",
        "airport_location": "Atlanta",
        "other_details": "International"
    }
]


inserted_airport_data = airport_col.insert_many(airports)


#flights cost collection

flight_cost = [
    {
        "_id": {
            "flight_number": "AA321",
            "aircraft_type_code": "B747"
        },
        "valid_from_date": "2023-01-01",
        "valid_to_date": "2025-01-01",
        "flight_cost": 9845
    },
    {
        "_id": {
            "flight_number": "AA642",
            "aircraft_type_code": "B360"
        },
        "valid_from_date": "2023-01-01",
        "valid_to_date": "2025-01-01",
        "flight_cost": 2478
    },
    {
        "_id": {
            "flight_number": "AA985",
            "aircraft_type_code": "S823"
        },
        "valid_from_date": "2023-01-01",
        "valid_to_date": "2025-01-01",
        "flight_cost": 3675
    }
]



inserted_flight_cost_data = flight_cost_col.insert_many(flight_cost)





#flights schedule collection

flight_sched = [
    {
        "_id": {
            "flight_number": "AA321",
            "airline_code": "JK35748",
            "usual_aircraft_type_code": "B747",
            "origin_airport_code": "LFT",
            "destination_airport_code": "JFK"
        },
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    },
    {
        "_id": {
            "flight_number": "AA642",
            "airline_code": "JK26747",
            "usual_aircraft_type_code": "B360",
            "origin_airport_code": "MSY",
            "destination_airport_code": "DFW"
        },
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    },
    {
        "_id": {
            "flight_number": "AA985",
            "airline_code": "JK10832",
            "usual_aircraft_type_code": "S823",
            "origin_airport_code": "MSY",
            "destination_airport_code": "ATL"
        },
        "departure_date_time": "2023-10-12T10:00:00",
        "arrival_date_time": "2023-10-12T12:00:00"
    }
]



inserted_flight_sched_data = flight_sched_col.insert_many(flight_sched)



#ref calendar collection

ref_calendar = [
    {
        "_id": "765354",
        "day_number": 4,
        "business_day_yn": "09-04-2024"
    },
    {
        "_id": "794524",
        "day_number": 12,
        "business_day_yn": "08-12-2024"
    },
    {
        "_id": "165424",
        "day_number": 9,
        "business_day_yn": "07-09-2024"
    }
]

inserted_ref_cal_data = ref_cal_col.insert_many(ref_calendar)

# Customer view itinerary

# Define which passenger 

passenger_id = "7463826"

# Pipeline to retreive necessary information

cust_itin_pipeline = [
    {
        '$match': {
            '_id': passenger_id
        }
    },
    {
        '$lookup': {
            'from': 'itinerary reservations',
            'localField': 'passenger_id',
            'foreignField': 'passenger_id',
            'as': 'res'
        }
    },
    {
        '$unwind': {
            'path': '$reservations',
            'preserveNullAndEmptyArrays': True 
        }
    },
    {
        '$lookup': {
            'from': 'itinerary legs',
            'localField': 'res._id',
            'foreignField': 'reservation_id',
            'as': 'legs'
        }
    },
    {
        '$project': {
            'first_name': 1,
            'last_name': 1,
            'reservations': {
                'reservation_id': '$reservations._id',
                'payment_amount': '$reservations.payment_amount',
                'origin': '$res.origin_airport_code',
                'destination': '$res.destination_airport_code',
                'date_reservation_made': '$res.date_reservation_made',
                'legs': '$legs'
            }
        }
    }
]

# Aggregate and list the information

cust_itinerary = list(db['passengers'].aggregate(cust_itin_pipeline))

# Find  all seats on a given flight

# Determine which flight to look up 

flight_number = "AA321"

# Pipeline to find the names of passengers 

pass_on_flight_pipeline = [
    {
        '$lookup': {
            'from': 'reservation payments',
            'localField': 'passenger_id',
            'foreignField': 'pass_id',
            'as': 'payment_info'
        }
    },
    {
        '$unwind': {
            'path': '$payment_info',
            'preserveNullAndEmptyArrays': True
        }
    },
    {
        '$lookup': {
            'from': 'itinerary reservations',
            'localField': 'passenger_id',
            'foreignField': 'passenger_id',
            'as': 'res_info'
        }
    },
    {
        '$unwind': {
            'path': '$res_info',
            'preserveNullAndEmptyArrays': True
        }
    },
    {
        '$lookup': {
            'from': 'itinerary legs',
            'localField': 'res_info._id',
            'foreignField': 'reservation_id',
            'as': 'itin_leg'
        }
    },
    {
        '$match': {
            'itin_leg.flight_number': flight_number
        }
    },
    {
        '$project': {
            'first_name': '$first_name',
            'last_name': '$last_name',
            'flight_number': '$itin_leg.flight_number'
        }
    }
]

# Execute the aggregation
pass_on_flight = list(db['passengers'].aggregate(pass_on_flight_pipeline))


# All flights from JFK

# Define the airport code for JFK

jfk_airport_code = 'JFK'

# Pipeline to retreive flights from JFK 

jfk_flight_pipeline = [
    {
        '$match': {
            '$or': [
                {'origin_airport_code': jfk_airport_code},
                {'destination_airport_code': jfk_airport_code}
            ]
        }
    },
    {
        '$lookup': {
            'from': 'airports',
            'localField': 'origin_airport_code',
            'foreignField': '_id',
            'as': 'origin_airport'
        }
    },
    {
        '$lookup': {
            'from': 'airports',
            'localField': 'destination_airport_code',
            'foreignField': '_id',
            'as': 'destination_airport'
        }
    },
    {
        '$unwind': '$origin_airport'
    },
    {
        '$unwind': '$destination_airport'
    },
    {
        '$project': {
            'flight_number': '$flight_number',
            'departure_airport': '$origin_airport.airport_name',
            'arrival_airport': '$destination_airport.airport_name',
            'departure_time': '$departure_date_time',
            'arrival_time': '$arrival_date_time'
        }
    }
]

# Execute the aggregation and list results

flights_at_jfk = db['itinerary legs'].aggregate(jfk_flight_pipeline)

jfk_flight = list(flights_at_jfk)

# View flight schedules

# Pipeline to create a list of flight schedules 

flight_sched_pipeline = [
    {
        '$lookup': {
            'from': 'airports',
            'localField': 'departure_airport_code',
            'foreignField': 'airport_code',
            'as': 'dep_apt'
        }
    },
    {
        '$lookup': {
            'from': 'airports',
            'localField': 'arrival_airport_code',
            'foreignField': 'airport_code',
            'as': 'arr_apt'
        }
    },
    {
        '$project': {
            'flight_number': 1,
            'departure_time': 1,
            'arrival_time': 1,
        }
    },
    {
        '$sort': {
            'departure_time': 1  # Sort by departure time
        }
    }
]

# Aggregate and list the flight schedules 

flight_schedules = list(db['flight schedule'].aggregate(flight_sched_pipeline))


# Determine delayed or on time flights

# Pipeline to check flight timeliness

time_check_pipeline = [
    {
        '$match': {
            '$or': [
                {'departure_efficiency': True},  # On-time
                {'departure_efficiency': False}  # Delayed
            ]
        }
    },
    {
        '$project': {
            'flight_number': '$flight_number',
            'departure_time': '$departure_date_time',
            'arrival_time': '$arrival_date_time',
            'status': {
                '$cond': {
                    'if': {'$eq': ['$departure_efficiency', True]},
                    'then': 'On Time',
                    'else': 'Delayed'
                }
            }
        }
    }
]

# Execute the aggregation

flight_status = db['itinerary legs'].aggregate(time_check_pipeline)

# List the results

delay_vs_timely = list(flight_status)



# Calculate total sales on given flight

# Pipeline to sum sales for a given flight 

sum_pipeline = [
    {
        '$match': {
            'flight_number': 'AA321' 
        }
    },
    {
        '$group': {
            '_id': '$flight_number',
            'total_sales': { '$sum': '$payment_amount' }
        }
    }
]

# Execute the aggregation

salesaa321 = list(db['reservation payments'].aggregate(sum_pipeline))



