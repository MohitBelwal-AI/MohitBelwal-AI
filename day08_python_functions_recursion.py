# ============================================================
#  Industrial Calculation Engine — Day 08
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Functions (def, return, parameters, defaults),
#            Recursion, Recursive base case,
#            Function calling function
#  Goal    : Build reusable industrial calculation engine
#            using functions and recursion
# ============================================================

import math

print("=" * 58)
print("   INDUSTRIAL CALCULATION ENGINE v3.0")
print("   Author : Mohit Belwal | Day 08 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Basic Functions with Parameters
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Basic Functions")
print("-" * 45)

def calculate_flc(power_kw, voltage=415, pf=0.85, eff=0.90):
    """Calculate Full Load Current of 3-phase motor"""
    power_w = power_kw * 1000
    flc = power_w / (math.sqrt(3) * voltage * pf * eff)
    return round(flc, 2)

def calculate_cable_size(current, derating=0.8):
    """Suggest cable size based on current rating"""
    required = current / derating
    if required <= 16:
        return "2.5 sq.mm"
    elif required <= 25:
        return "4 sq.mm"
    elif required <= 32:
        return "6 sq.mm"
    elif required <= 50:
        return "10 sq.mm"
    elif required <= 63:
        return "16 sq.mm"
    else:
        return "25 sq.mm or higher"

def calculate_energy_cost(power_kw, hours, tariff=7.50):
    """Calculate daily energy cost"""
    units = power_kw * hours
    cost  = units * tariff
    return units, round(cost, 2)

# Call functions
motor_kw  = 7.5
flc       = calculate_flc(motor_kw)
cable     = calculate_cable_size(flc)
units, cost = calculate_energy_cost(motor_kw, 8)

print(f"  Motor Rating   : {motor_kw} kW")
print(f"  Full Load Amps : {flc} A")
print(f"  Cable Size     : {cable}")
print(f"  Daily Units    : {units} kWh")
print(f"  Daily Cost     : ₹ {cost}")
print()

# ─────────────────────────────────────────────
# SECTION 2 — Function calling Function
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Function Calling Function")
print("-" * 45)

def motor_full_report(name, power_kw, hours):
    """Master function — calls all sub functions"""
    flc         = calculate_flc(power_kw)
    cable       = calculate_cable_size(flc)
    units, cost = calculate_energy_cost(power_kw, hours)

    print(f"  Motor         : {name}")
    print(f"  Power         : {power_kw} kW")
    print(f"  FLC           : {flc} A")
    print(f"  Cable         : {cable}")
    print(f"  Daily Cost    : ₹ {cost}")
    print()

motor_full_report("Pump Motor",     7.5,  8)
motor_full_report("Conveyor Motor", 11.0, 12)
motor_full_report("Compressor",     15.0, 16)

# ─────────────────────────────────────────────
# SECTION 3 — Recursion
#             Factorial — used in probability &
#             permutation calculations in quality control
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Recursion — Factorial")
print("-" * 45)

def factorial(n):
    """Recursive factorial — base case: n == 1"""
    if n == 1 or n == 0:    # Base case — stops recursion
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

print("  Factorial calculations:")
for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")
print()

# ─────────────────────────────────────────────
# SECTION 4 — Recursion Real Use Case
#             Countdown timer simulation
#             (Like PLC timer counting down)
# ─────────────────────────────────────────────
print(">>> SECTION 4 : Recursion — Motor Startup Countdown")
print("-" * 45)

def startup_countdown(seconds):
    """Recursive countdown — simulates PLC timer"""
    if seconds == 0:        # Base case
        print("  🟢 MOTOR STARTED — Full Speed!")
        return
    print(f"  ⏱  Starting in {seconds} seconds...")
    startup_countdown(seconds - 1)   # Recursive call

startup_countdown(5)
print()

# ─────────────────────────────────────────────
# SECTION 5 — Recursion — Power Calculation
#             V^n without using ** operator
# ─────────────────────────────────────────────
print(">>> SECTION 5 : Recursion — Power Function")
print("-" * 45)

def power(base, exp):
    """Recursive power: base^exp"""
    if exp == 0:            # Base case
        return 1
    return base * power(base, exp - 1)

print(f"  415^2 (voltage squared) = {power(415, 2)}")
print(f"  2^10  (binary bits)     = {power(2, 10)}")
print(f"  3^3   (3-phase factor)  = {power(3, 3)}")
print()

# ─────────────────────────────────────────────
# SECTION 6 — Recursion — Sum of sensor readings
# ─────────────────────────────────────────────
print(">>> SECTION 6 : Recursion — Sum of Sensor Readings")
print("-" * 45)

def sum_sensors(readings, index=0):
    """Recursively sum all sensor readings in list"""
    if index == len(readings):   # Base case — end of list
        return 0
    return readings[index] + sum_sensors(readings, index + 1)

temps = [62.5, 78.3, 55.1, 70.8, 45.6]
total = sum_sensors(temps)
avg   = round(total / len(temps), 2)

print(f"  Sensor Readings : {temps}")
print(f"  Total (recursive sum) : {total}")
print(f"  Average Temperature   : {avg} °C")
print()

print("=" * 58)
print("  Day 8 Complete — Functions & Recursion mastered!")
print("  Next: File Handling, Exception Handling")
print("=" * 58)
