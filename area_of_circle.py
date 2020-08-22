def circle():
    from math import pi
    value = input("Give me diameter (d) or radius (r): " )
    if value == str('r'):
        v1 = input("what is the radius of circle?: ")
        r1 = float(v1)
        area = round(pi*(r1)**2)
        print(f"area of circle is:{area} sq. units")
    elif value == str('d'):
        v2 = input("what is the diameter of circle?: ")
        d1 = float(v2)
        area = round(pi*((d1)/2)**2)
        print(f"area of circle is:{area} sq. units")

circle()

