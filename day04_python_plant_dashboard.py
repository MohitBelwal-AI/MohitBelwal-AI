# ============================================================
#  Industrial Plant Dashboard — Day 04 (Practice Day)
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: REVISION — Variables, input(), if-elif-else,
#            Lists, Tuples, f-strings, Loops, Functions
#  Goal    : Mini dashboard that combines all Day 1-3 concepts
#            into one real industrial use case
# ============================================================

# ─────────────────────────────────────────────
# Day 1 Concept — Variables & f-strings
# ─────────────────────────────────────────────
print("=" * 58)
print("   INDUSTRIAL PLANT DASHBOARD v1.0")
print("   Author : Mohit Belwal | Day 04 — Practice Day")
print("=" * 58)
print()

# Plant info — Tuple (Day 3)
plant_info = ("Mohit Belwal Industries", "Uttarakhand", 415, 50)
print(f"  Plant  : {plant_info[0]}")
print(f"  Location : {plant_info[1]} | {plant_info[2]}V | {plant_info[3]}Hz")
print()

# ─────────────────────────────────────────────
# Day 2 Concept — input() + if-elif-else
# ─────────────────────────────────────────────
print(">>> STEP 1 : Enter Motor Details")
print("-" * 45)

motor_name  = input("  Motor Name (e.g. Pump Motor) : ")
voltage     = float(input("  Supply Voltage (V)          : "))
current     = float(input("  Running Current (A)         : "))
temperature = float(input("  Temperature (°C)            : "))
motor_kw    = float(input("  Motor Rating (kW)           : "))
run_hours   = float(input("  Hours Running Today         : "))

print()

# ─────────────────────────────────────────────
# Day 1 Concept — Calculations
# ─────────────────────────────────────────────
import math

flc          = (motor_kw * 1000) / (math.sqrt(3) * 415 * 0.85 * 0.90)
energy_today = motor_kw * run_hours
cost_today   = energy_today * 7.50

# ─────────────────────────────────────────────
# Day 2 Concept — if-elif-else checks
# ─────────────────────────────────────────────

# Voltage check
if voltage < 380:
    v_status = "⚠️  LOW VOLTAGE"
    v_safe = False
elif voltage > 450:
    v_status = "⚠️  HIGH VOLTAGE"
    v_safe = False
else:
    v_status = "✅ NORMAL"
    v_safe = True

# Temperature check
if temperature < 60:
    t_status = "✅ COOL"
    t_safe = True
elif temperature < 85:
    t_status = "✅ NORMAL"
    t_safe = True
else:
    t_status = "🔴 CRITICAL"
    t_safe = False

# Current check
if current <= flc * 1.15:
    c_status = "✅ NORMAL"
    c_safe = True
else:
    c_status = "⚠️  OVERCURRENT"
    c_safe = False

# ─────────────────────────────────────────────
# Day 3 Concept — Lists (Store alarm log)
# ─────────────────────────────────────────────
alarm_log = []

if not v_safe:
    alarm_log.append(f"Voltage Fault — {voltage}V detected")
if not t_safe:
    alarm_log.append(f"Temperature Critical — {temperature}°C detected")
if not c_safe:
    alarm_log.append(f"Overcurrent — {current}A detected")

# ─────────────────────────────────────────────
# DASHBOARD OUTPUT
# ─────────────────────────────────────────────
print("=" * 58)
print(f"   MOTOR REPORT — {motor_name.upper()}")
print("=" * 58)
print()
print(f"  Supply Voltage   : {voltage} V        {v_status}")
print(f"  Running Current  : {current} A        {c_status}")
print(f"  Temperature      : {temperature} °C      {t_status}")
print(f"  Full Load Amps   : {flc:.2f} A")
print()
print(f"  Energy Today     : {energy_today:.2f} kWh")
print(f"  Cost Today       : ₹ {cost_today:.2f}")
print()

# ─────────────────────────────────────────────
# Alarm Log — List (Day 3)
# ─────────────────────────────────────────────
print(">>> ALARM LOG")
print("-" * 45)

if len(alarm_log) == 0:
    print("  ✅ No Alarms — All parameters normal!")
else:
    print(f"  ⚠️  {len(alarm_log)} Alarm(s) Active:")
    for i in range(len(alarm_log)):
        print(f"    [{i+1}] {alarm_log[i]}")

print()

# Final verdict
print("=" * 58)
if v_safe and t_safe and c_safe:
    print("  ✅  MOTOR STATUS : HEALTHY — Safe to run")
else:
    print("  🔴  MOTOR STATUS : ATTENTION REQUIRED")
print("=" * 58)
print()
print("  Day 4 Complete — All Day 1-3 concepts combined!")
print("  Variables + input() + if-else + Lists + Tuples")
print("=" * 58)
