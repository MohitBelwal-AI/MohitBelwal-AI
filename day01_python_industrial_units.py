# ============================================================
#  Industrial Unit Converter — Day 01
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Variables, Data Types, print(), f-strings,
#            Comments, Basic Arithmetic
#  Goal    : Convert common industrial electrical units
# ============================================================

# --- Project Info ---
project_name    = "Industrial Unit Converter"
author          = "Mohit Belwal"
qualification   = "B.Tech Electrical Engineering"
day             = 1
language        = "Python"

print("=" * 52)
print(f"  {project_name}")
print(f"  Author : {author}")
print(f"  Day    : {day} of Python Journey")
print("=" * 52)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Voltage Conversions
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Voltage Conversions")
print("-" * 40)

voltage_kv  = 11.0          # 11 kV supply line (float)
voltage_v   = voltage_kv * 1000
voltage_mv  = voltage_v  * 1000

print(f"  Input Voltage : {voltage_kv} kV")
print(f"  In Volts      : {voltage_v:.0f} V")
print(f"  In Millivolts : {voltage_mv:.0f} mV")
print()

# ─────────────────────────────────────────────
# SECTION 2 — Power Conversions
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Power Conversions")
print("-" * 40)

motor_power_kw  = 7.5       # Standard industrial motor (float)
motor_power_w   = motor_power_kw * 1000
motor_power_hp  = motor_power_kw * 1.341          # 1 kW = 1.341 HP

print(f"  Motor Rating  : {motor_power_kw} kW")
print(f"  In Watts      : {motor_power_w:.1f} W")
print(f"  In Horsepower : {motor_power_hp:.2f} HP")
print()

# ─────────────────────────────────────────────
# SECTION 3 — Current Calculation  (P = V × I)
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Full-Load Current (FLC)")
print("-" * 40)

supply_voltage  = 415       # 3-phase line voltage in Volts (int)
power_factor    = 0.85      # Typical industrial PF (float)
efficiency      = 0.90      # Motor efficiency 90 % (float)

# Formula: I = P / (√3 × V × PF × η)
import math
flc = (motor_power_w) / (math.sqrt(3) * supply_voltage * power_factor * efficiency)

print(f"  Supply Voltage : {supply_voltage} V (3-phase)")
print(f"  Power Factor   : {power_factor}")
print(f"  Efficiency     : {efficiency * 100:.0f} %")
print(f"  Full-Load Amps : {flc:.2f} A")
print()

# ─────────────────────────────────────────────
# SECTION 4 — Energy & Cost Estimation
# ─────────────────────────────────────────────
print(">>> SECTION 4 : Energy Cost Estimation")
print("-" * 40)

operating_hours_per_day = 8             # int
days_per_month          = 26            # int  (working days)
tariff_per_unit         = 7.50          # ₹ per kWh (float)

energy_per_day_kwh   = motor_power_kw * operating_hours_per_day
energy_per_month_kwh = energy_per_day_kwh * days_per_month
monthly_cost_inr     = energy_per_month_kwh * tariff_per_unit

print(f"  Operating Hours/Day  : {operating_hours_per_day} hrs")
print(f"  Working Days/Month   : {days_per_month}")
print(f"  Energy per Day       : {energy_per_day_kwh:.1f} kWh")
print(f"  Energy per Month     : {energy_per_month_kwh:.1f} kWh")
print(f"  Monthly Energy Cost  : ₹ {monthly_cost_inr:,.2f}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — Data Types Summary (learning log)
# ─────────────────────────────────────────────
print(">>> SECTION 5 : Data Types Used Today")
print("-" * 40)

print(f"  voltage_kv   → type: {type(voltage_kv).__name__}   | value: {voltage_kv}")
print(f"  supply_voltage → type: {type(supply_voltage).__name__}     | value: {supply_voltage}")
print(f"  author       → type: {type(author).__name__}    | value: '{author}'")
print(f"  language     → type: {type(language).__name__}    | value: '{language}'")
print(f"  day          → type: {type(day).__name__}     | value: {day}")
print()

print("=" * 52)
print("  Day 1 Complete — Variables & Print mastered!")
print(f"  Next: Operators, Input(), Conditionals")
print("=" * 52)
