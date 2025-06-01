import os
from typing import List, Tuple, Dict
from functools import lru_cache, reduce

def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content

def read_races(input: str):
    def strip(input):
        return input.strip()
    
    def split_values_from_str(string):
        trash, values = string.split(":")
        values: List[int] = list(map(strip, values.split()))
        return values
    
    time, distance = input.splitlines()
    times = split_values_from_str(time)
    distances = split_values_from_str(distance)
    struct = dict()

    for i in range(len(times)):
        struct[i] = {
            "time": int(times[i]),
            "distance": int(distances[i])
        }

    return struct


def read_races_2(input: str):
    def strip(input):
        return input.strip()
    
    def split_values_from_str(string):
        trash, values = string.split(":")
        values = "".join(list(map(strip, values.split())))
        return values
    
    time, distance = input.splitlines()
    times = split_values_from_str(time)
    distances = split_values_from_str(distance)
    struct = dict()
    struct[0]= {
            "time": int(times),
            "distance": int(distances)
        }

    return struct

@lru_cache
def calc_distance(time_pressed, remaining_time, total_time, highest_distance):
    results = []
    distance = time_pressed * remaining_time

    print(f"With time pressed: {time_pressed} and remaining time: {remaining_time}, the distance would be: {distance}, and required distance is {highest_distance}")

    if time_pressed >= total_time:
        return results
    if distance > highest_distance:
        results.append(1)

    result = calc_distance(time_pressed+1, remaining_time-1, total_time, highest_distance)
    results.extend(result)

    return results

def calc_distance_3(remaining_time, total_time, highest_distance):

    min_time_pressed = (highest_distance // total_time)+1
    min_time_pressed_2 = 0
    for i in range(min_time_pressed, total_time):
        if  min_time_pressed_2 == 0:
            remaining_game_time = (total_time - i)
            current_distance = (i * remaining_game_time)
            if current_distance > highest_distance:
                min_time_pressed_2 = i
    
    max_remaining_time = remaining_time - min_time_pressed_2

    margine_for_error = (max_remaining_time - min_time_pressed_2)+1
    return margine_for_error

def multiply(accumulator, number):
    return accumulator * number

def parse_result(actual_result, expected_result, inputfile):
    if expected_result == actual_result:
        print("Success!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
    else: 
        print("Catastrophic Failure!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
        print(f"diff: {expected_result-actual_result}")


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    race_info = read_races(read_file(inputfile))
    margine_for_error = []
    for race in race_info:
        print("*"*24)
        result = calc_distance(0, race_info[race]['time'], race_info[race]['time'], race_info[race]['distance'])
        margine_for_error.append(len(result))
    actual_result = reduce(multiply, margine_for_error)
    print("="*12)
    print(f"Running in main1")
    parse_result(actual_result, expected_result_1, inputfile)

def main1_2(inputfile, expected_result_1=0, expected_result_2=0):
    race_info = read_races(read_file(inputfile))
    margine_for_error = []
    for race in race_info:
        print("*"*24)
        result = calc_distance_3(race_info[race]['time'], race_info[race]['time'], race_info[race]['distance'])
        margine_for_error.append(result)
    actual_result = reduce(multiply, margine_for_error)
    print("="*12)
    print(f"Running in main1_2")
    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    race_info = read_races_2(read_file(inputfile))
    for race in race_info:
        print("*"*24)
        result = calc_distance_3(race_info[race]['time'], race_info[race]['time'], race_info[race]['distance'])
    actual_result_2 = result
    print("="*12)
    print(f"Running in main2")
    parse_result(actual_result_2, expected_result_2, inputfile)

if __name__=="__main__":
    for inputfile in (
        ("example", 288, 71503), 
        ("input", 1660968, 26499773),
    ):
        main1(*inputfile)
        main1_2(*inputfile)
        main2(*inputfile)
    
    print('\n')

