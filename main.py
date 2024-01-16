# author: Jose Tellez and Joey Tran
import utilities


def main():
    circle_radius = float(input("Enter the radius of a circle in cm: "))
    circle_area = utilities.calculate_circle_area(circle_radius)
    print(f"The area of the circle is: {circle_area}")

    sphere_radius = float(input("Enter the radius of a sphere in cm: "))
    sphere_volume = utilities.calculate_sphere_volume(sphere_radius)
    print(f"The volume of the sphere is: {sphere_volume}")

    print(f"The Body Mass Index is: {utilities.calculate_BMI()}")
    print(f"The hypotenuse length of the right triangle is: {utilities.calculate_hypotenuse()}")


if __name__ == "__main__":
    main()
