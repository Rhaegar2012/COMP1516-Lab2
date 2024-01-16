# author: Jose Tellez and Joey Tran
import math


def calculate_circle_area(circle_radius):
    """
    Calculates area of circle
    :param circle_radius: radius of the circle in cm
    :return: area of circle
    """
    circle_area = math.pi * circle_radius ** 2
    return circle_area


def calculate_sphere_volume(sphere_radius):
    """
    Calculates volume of sphere
    :param sphere_radius: radius of the sphere in cm
    :return: volume of sphere
    """
    sphere_volume = 4/3 * math.pi * sphere_radius ** 3
    return sphere_volume


def calculate_BMI():
    """
    Calculates Body Mass Index
    :return: body mass index
    """
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))
    body_mass_index = weight_kg / (height_m * height_m)
    return body_mass_index


def calculate_hypotenuse():
    """
    Calculates hypotenuse length of right triangle
    :return: hypotenuse length of right triangle
    """
    side_a_length = float(input("Enter the length of side A in cm"))
    side_b_length = float(input("Enter the length of side B in cm"))
    hypotenuse_length = math.hypot(side_a_length, side_b_length)
    return hypotenuse_length
