def compute_vol_of_sphere(radius):
	pi = 3.14
	y=4/3
	volume = y*pi * radius * radius * radius
	return volume

radius1 = 30
volume1 = compute_vol_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 40
area2 = compute_vol_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")


