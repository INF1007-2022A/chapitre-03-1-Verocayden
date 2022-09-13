#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def square_root(a: float) -> float:
    a = a**(1/2)
    return a


def square(a: float) -> float:
    a = a**2
    return a


def average(a: float, b: float, c: float) -> float:
    average = (a+b+c)/3
    return average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degs_rads = angle_degs * (math.pi / 180)
    angle_mins_rads = (angle_mins) * (math.pi / 180)
    angle_secs_rads = (angle_secs) * (math.pi / 180)
    return angle_degs_rads, angle_mins_rads, angle_secs_rads


def to_degrees(angle_rads: float) -> tuple:
    angle_rads_to_deg = angle_rads * (180 / math.pi)
    angle_mins = (angle_rads_to_deg - math.floor(angle_rads_to_deg)) * 60 # Enlever partie entiere pour garder decimales.
    angle_secs = (angle_mins - math.floor(angle_mins)) *60
    return math.floor(angle_rads_to_deg), angle_mins, angle_secs # Garder uniquement la partie entiere du degre.


def to_celsius(temperature: float) -> float:
    celsius = temperature / 1.8 - 32
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit = temperature * 1.8 + 32
    return farenheit


def main() -> None:
    print(f"La racine carrée de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
