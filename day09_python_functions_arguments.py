# ============================================================
#  Industrial Parameter Calculator — Day 09
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Functions with Arguments (positional, keyword,
#            default), Return values, Multiple return values,
#            *args, **kwargs
#  Goal    : Build a complete industrial parameter calculator
#            using advanced function argument techniques
# ============================================================

import math

print("=" * 58)
print("   INDUSTRIAL PARAMETER CALCULATOR v4.0")
print("   Author : Mohit Belwal | Day 09 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Positional Arguments
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Positional Arguments")
print("-" * 45)

def calculate_flc(power_kw, voltage, pf):
    """FLC using positional arguments — order matters!"""
    flc = (power_kw * 1000) / (math.sqrt(3) * voltage * pf)
    return round(flc, 2)

# Arguments passed by position
result = calculate_flc(7.5, 415, 0.85)
print(f"  FLC (7.5kW, 415V, PF=0.85) : {result} A")
print()

# ─────────────────────────────────────────────
# SECTION 2 — Default Arguments
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Default Arguments")
print("-" * 45)

def motor_current(power_kw, voltage=415, pf=0.85, eff=0.90):
    """Default args — voltage/pf/eff have standard values"""
    current = (power_kw * 1000) / (math.sqrt(3) * voltage * pf * eff)
    return round(current, 2)

print(f"  7.5kW  (all defaults)      : {motor_current(7.5)} A")
print(f"  11kW   (all defaults)      : {motor_current(11)} A")
print(f"  15kW   (custom pf=0.90)    : {motor_current(15, pf=0.90)} A")
print(f"  22kW   (custom voltage=400): {motor_current(22, voltage=400)} A")
print()

# ─────────────────────────────────────────────
# SECTION 3 — Keyword Arguments
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Keyword Arguments")
print("-" * 45)

def panel_load(motor_kw, lighting_kw, hvac_kw, spare_kw):
    """Panel load calculation — keyword args, order doesn't matter"""
    total   = motor_kw + lighting_kw + hvac_kw + spare_kw
    demand  = total * 0.75      # 75% demand factor
    return total, round(demand, 2)

# Keyword arguments — any order works!
total, demand = panel_load(
    hvac_kw     = 5.0,
    lighting_kw = 2.5,
    spare_kw    = 1.5,
    motor_kw    = 15.0
)
print(f"  Total Connected Load : {total} kW")
print(f"  Demand Load (75%)    : {demand} kW")
print()

# ─────────────────────────────────────────────
# SECTION 4 — Multiple Return Values
# ─────────────────────────────────────────────
print(">>> SECTION 4 : Multiple Return Values")
print("-" * 45)

def full_motor_analysis(power_kw, hours_per_day, tariff=7.50):
    """Returns multiple values at once"""
    flc          = motor_current(power_kw)
    daily_units  = power_kw * hours_per_day
    daily_cost   = daily_units * tariff
    monthly_cost = daily_cost * 26
    annual_cost  = daily_cost * 312

    return flc, daily_units, round(daily_cost, 2), round(monthly_cost, 2), round(annual_cost, 2)

flc, units, d_cost, m_cost, a_cost = full_motor_analysis(7.5, 8)

print(f"  Full Load Current  : {flc} A")
print(f"  Daily Units        : {units} kWh")
print(f"  Daily Cost         : ₹ {d_cost}")
print(f"  Monthly Cost       : ₹ {m_cost}")
print(f"  Annual Cost        : ₹ {a_cost}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — *args (Variable positional args)
# ─────────────────────────────────────────────
print(">>> SECTION 5 : *args — Variable Motor Loads")
print("-" * 45)

def total_plant_load(*motor_ratings):
    """Accept any number of motor ratings"""
    total = 0
    for kw in motor_ratings:
        total += kw
        print(f"  Added {kw} kW motor → Running total: {total} kW")
    return total

print("  Adding motors one by one:")
total = total_plant_load(3.7, 5.5, 7.5, 11.0, 15.0)
print(f"  Total Plant Load : {total} kW")
print()

# ─────────────────────────────────────────────
# SECTION 6 — **kwargs (Variable keyword args)
# ─────────────────────────────────────────────
print(">>> SECTION 6 : **kwargs — Motor Specifications")
print("-" * 45)

def print_motor_specs(motor_name, **specs):
    """Accept any motor specifications as keyword args"""
    print(f"  Motor : {motor_name}")
    for key, value in specs.items():
        print(f"    {key:20} : {value}")
    print()

print_motor_specs("Pump Motor",
    power_kw      = 7.5,
    voltage       = "415V 3-Phase",
    current       = "14.2A",
    speed         = "1450 RPM",
    insulation    = "Class F",
    protection    = "IP55"
)

print_motor_specs("Conveyor Motor",
    power_kw      = 11.0,
    voltage       = "415V 3-Phase",
    current       = "20.8A",
    speed         = "960 RPM",
    mounting      = "Foot Mounted",
    duty_cycle    = "S1 Continuous"
)

print("=" * 58)
print("  Day 9 Complete — Function Arguments mastered!")
print("  Positional, Default, Keyword, *args, **kwargs")
print("  Next: File Handling, Exception Handling")
print("=" * 58)
