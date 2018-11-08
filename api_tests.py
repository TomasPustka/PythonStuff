import requests
import json

my_api_key = 'd95KZrCVKzJIK1PPFjQpFVORhhpWbg8Sn549I1OI'
base_address = 'https://api.nasa.gov/DONKI/CME'
# format of YYYY-MM-DD
start_date = '2000-01-01'
# format of YYYY-MM-DD
end_date = '2017-12-31'

output_file_name = 'cme_json.json'


def build_api_address(my_api_key, base_address, start_date, end_date, most_accurate_only = 'true', complete_entry_only = 'true', speed = '0', half_angle = '0', catalog = 'ALL', keyword = 'NONE'):
    return "{0}?startDate={1}&endDate={2}&mostAccurateOnly={3}&completeEntryOnly={4}" \
           "&speed={5}&halfAngle={6}&catalog={7}&keyword={8}&api_key={9}"\
        .format(base_address, start_date, end_date, most_accurate_only, complete_entry_only,
                speed, half_angle, catalog, keyword, my_api_key)


def save_json_data(json_data, output_file_name):
    with open(output_file_name, 'w') as json_file:
        json.dump(json_data, json_file)


built_api_address = build_api_address(my_api_key, base_address, start_date, end_date)

json_data = requests.get(built_api_address).json()

save_json_data(json_data, output_file_name)


#print(json_data)
