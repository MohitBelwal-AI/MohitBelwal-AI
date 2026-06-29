# ============================================================
#  Motor Report Generator — Day 05
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Functions (def), Return values, Parameters,
#            Lists, if-elif-else, f-strings (Revision)
#  Goal    : Generate professional motor health report
#            using reusable functions
# ============================================================

import math

print("=" * 58)
print("   MOTOR HEALTH REPORT GENERATOR v2.0")
print("   Author : Mohit Belwal | Day 05 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Functions (New Concept Day 05)
# ─────────────────────────────────────────────

# Function 1 — Calculate Full Load Current
def calculate_flc(power_kw, voltage=415, pf=0.85, efficiency=0.90):
    power_w = power_kw * 1000
    flc = power_w / (math.sqrt(3) * voltage * pf * efficiency)
    return round(flc, 2)

# Function 2 — Check Voltage Status
def check_voltage(voltage):
    if voltage < 380:
        return "LOW VOLTAGE ⚠️", False
    elif voltage > 450:
        return "HIGH VOLTAGE ⚠️", False
    else:
        return "NORMAL ✅", True

# Function 3 — Check Temperature Status
def check_temperature(temp):
    if temp < 60:
        return "COOL ✅", True
    elif temp < 75:
        return "NORMAL ✅", True
    elif temp < 85:
        return "HOT — Monitor ⚠️", True
    else:
        return "CRITICAL 🔴", False

# Function 4 — Check Current Status
def check_current(current, flc):
    limit = flc * 1.15
    if current <= limit:
        return f"NORMAL ✅ (Limit: {limit:.2f}A)", True
    else:
        return f"OVERCURRENT ⚠️ (Limit: {limit:.2f}A)", False

# Function 5 — Calculate Energy Cost
def calculate_cost(power_kw, hours, tariff=7.50):
    energy = power_kw * hours
    cost   = energy * tariff
    return energy, cost

# Function 6 — Generate Alarm List
def generate_alarms(v_safe, c_safe, t_safe, voltage, current, temp):
    alarms = []
    if not v_safe:
        alarms.append(f"Voltage Fault — {voltage}V")
    if not c_safe:
        alarms.append(f"Overcurrent — {current}A")
    if not t_safe:
        alarms.append(f"Temperature Critical — {temp}°C")
    return alarms

# ─────────────────────────────────────────────
# SECTION 2 — Take Input
# ─────────────────────────────────────────────
print(">>> Enter Motor Parameters:")
print("-" * 45)

motor_name  = input("  Motor Name         : ")
motor_kw    = float(input("  Motor Rating (kW)  : "))
voltage     = float(input("  Supply Voltage (V) : "))
current     = float(input("  Current (A)        : "))
temperature = float(input("  Temperature (°C)   : "))
run_hours   = float(input("  Run Hours Today    : "))
print()

# ─────────────────────────────────────────────
# SECTION 3 — Call Functions
# ─────────────────────────────────────────────
flc                    = calculate_flc(motor_kw)
v_status, v_safe       = check_voltage(voltage)
t_status, t_safe       = check_temperature(temperature)
c_status, c_safe       = check_current(current, flc)
energy, cost           = calculate_cost(motor_kw, run_hours)
alarms                 = generate_alarms(v_safe, c_safe, t_safe,
                                          voltage, current, temperature)

# ─────────────────────────────────────────────
# SECTION 4 — Print Report
# ─────────────────────────────────────────────
print("=" * 58)
print(f"   MOTOR REPORT — {motor_name.upper()}")
print("=" * 58)
print(f"  Rating         : {motor_kw} kW")
print(f"  Full Load Amps : {flc} A")
print()
print(f"  Voltage        : {voltage} V     → {v_status}")
print(f"  Current        : {current} A     → {c_status}")
print(f"  Temperature    : {temperature} °C   → {t_status}")
print()
print(f"  Energy Today   : {energy:.2f} kWh")
print(f"  Cost Today     : ₹ {cost:.2f}")
print()

# Alarm Log
print(">>> ALARM LOG")
print("-" * 45)
if len(alarms) == 0:
    print("  ✅ No Alarms — All systems normal!")
else:
    print(f"  {len(alarms)} Active Alarm(s):")
    for i, alarm in enumerate(alarms):
        print(f"    [{i+1}] {alarm}")
print()

# Final Status
print("=" * 58)
if v_safe and c_safe and t_safe:
    print("  ✅  MOTOR STATUS : HEALTHY")
else:
    print("  🔴  MOTOR STATUS : ATTENTION REQUIRED")
print("=" * 58)
print()
print("  Day 5 Complete — Functions (def, return) mastered!")
print("  Next: Dictionary, File Handling")
print("=" * 58)
