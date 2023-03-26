import json

dict_obj = { "States Data":[
    {
        "State":"Uttar Pradesh",
        "Capital":"Lucknow"
        },
    {
        "State":"Manipur",
        "Capital":"Imphal"
        },
    {
        "State":"Nagaland",
        "Capital":"Kohima"
        },
    {
        "State":"Rajasthan",
        "Capital":"Jaipur"
        },
    {
        "State":"Punjab",
        "Capital":"Chandigarh"
        },
    {
        "State":"Sikkim",
        "Capital":"Gangtok"
        },
    {
        "State":"Jharkhand",
        "Capital":"Ranchi"
        }
]
    }

write_file = open("/Users/macbook/Documents/python files/python assignment 6/state.json","w")
json.dump(dict_obj,write_file)
