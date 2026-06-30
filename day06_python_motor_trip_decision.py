# ============================================================
#  Motor Trip Decision System — Day 06
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Relational Operators (==, >, <, >=, <=, !=),
#            Logical Operators (and, or, not),
#            elif Ladder (multiple conditions)
#  Goal    : Decide motor trip/run status using combined
#            relational + logical conditions — like a real
#            protection relay does in industry
# ============================================================

print("=" * 58)
print("   MOTOR PROTECTION RELAY — TRIP DECISION SYSTEM")
print("   Author : Mohit Belwal | Day 06 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Take Input
# ─────────────────────────────────────────────
print(">>> Enter Live Motor Readings:")
print("-" * 45)

voltage     = float(input("  Voltage (V)        : "))
current     = float(input("  Current (A)        : "))
temperature = float(input("  Temperature (°C)   : "))
vibration   = float(input("  Vibration (mm/s)   : "))
earth_fault = input("  Earth Fault? (yes/no): ").lower()

print()

# ─────────────────────────────────────────────
# SECTION 2 — Relational Operators (Basic Checks)
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Relational Operator Checks")
print("-" * 45)

# == equals, > greater, < less, >= , <=, != not equal
is_voltage_low   = voltage < 380
is_voltage_high  = voltage > 450
is_current_high  = current > 20          # assume 20A is rated limit
is_temp_critical = temperature >= 85     # >= relational operator
is_vibration_bad = vibration > 7.1       # ISO 10816 limit mm/s
is_earth_fault   = earth_fault == "yes"  # == relational operator

print(f"  voltage < 380        → {is_voltage_low}")
print(f"  voltage > 450        → {is_voltage_high}")
print(f"  current > 20         → {is_current_high}")
print(f"  temperature >= 85    → {is_temp_critical}")
print(f"  vibration > 7.1      → {is_vibration_bad}")
print(f"  earth_fault == 'yes' → {is_earth_fault}")
print()

# ─────────────────────────────────────────────
# SECTION 3 — Logical Operators (Combine Conditions)
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Logical Operator Combinations")
print("-" * 45)

# AND — both conditions must be true
voltage_problem = is_voltage_low or is_voltage_high
# OR — at least one true
mechanical_issue = is_vibration_bad or is_temp_critical
# NOT — inverts the condition
is_voltage_normal = not voltage_problem
# Combined AND + OR
critical_combo = is_earth_fault and (is_current_high or is_temp_critical)

print(f"  voltage_problem  = is_voltage_low OR is_voltage_high  → {voltage_problem}")
print(f"  mechanical_issue = is_vibration_bad OR is_temp_critical → {mechanical_issue}")
print(f"  voltage_normal   = NOT voltage_problem                 → {is_voltage_normal}")
print(f"  critical_combo   = earth_fault AND (current OR temp)   → {critical_combo}")
print()

# ─────────────────────────────────────────────
# SECTION 4 — elif Ladder (Priority-Based Decision)
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Protection Relay Decision (elif Ladder)")
print("-" * 45)

# elif ladder stops at FIRST true condition — priority matters!
if is_earth_fault and is_current_high:
    trip_status = "🔴 EMERGENCY TRIP — Earth Fault + Overcurrent!"
    priority    = "HIGHEST"

elif is_temp_critical and is_vibration_bad:
    trip_status = "🔴 TRIP — Critical Temp + Abnormal Vibration!"
    priority    = "HIGH"

elif is_voltage_low or is_voltage_high:
    trip_status = "⚠️  WARNING — Voltage out of safe range"
    priority    = "MEDIUM"

elif is_current_high:
    trip_status = "⚠️  WARNING — Overcurrent detected"
    priority    = "MEDIUM"

elif is_vibration_bad:
    trip_status = "⚠️  WARNING — High vibration, check bearings"
    priority    = "LOW"

elif is_temp_critical:
    trip_status = "⚠️  WARNING — Temperature critical"
    priority    = "LOW"

else:
    trip_status = "✅ NORMAL — Motor running safely"
    priority    = "NONE"

print(f"  Decision : {trip_status}")
print(f"  Priority : {priority}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — Final Report
# ─────────────────────────────────────────────
print("=" * 58)
print("   FINAL PROTECTION RELAY REPORT")
print("=" * 58)
print(f"  Voltage      : {voltage} V")
print(f"  Current      : {current} A")
print(f"  Temperature  : {temperature} °C")
print(f"  Vibration    : {vibration} mm/s")
print(f"  Earth Fault  : {earth_fault.upper()}")
print()
print(f"  >>> {trip_status}")
print("=" * 58)
print()
print("  Day 6 Complete — Relational + Logical Operators + elif!")
print("  Next: while loop, break, continue")
print("=" * 58)
