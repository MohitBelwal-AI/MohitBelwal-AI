# ============================================================
#  Motor Safety Checker — Day 02
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: input(), Type Casting, if-elif-else,
#            Comparison Operators, Logical Operators
#  Goal    : Check if a motor is safe to run based on
#            voltage, current and temperature inputs
# ============================================================

# --- Project Info ---
print("=" * 55)
print("   INDUSTRIAL MOTOR SAFETY CHECKER")
print("   Author : Mohit Belwal | Day 02 of Python Journey")
print("=" * 55)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Take Input from User
# ─────────────────────────────────────────────
print(">>> Enter Motor Parameters:")
print("-" * 40)

voltage     = float(input("  Supply Voltage (V)        : "))
current     = float(input("  Running Current (A)       : "))
temperature = float(input("  Motor Temperature (°C)    : "))
motor_kw    = float(input("  Motor Rating (kW)         : "))

print()

# ─────────────────────────────────────────────
# SECTION 2 — Define Safe Limits
# ─────────────────────────────────────────────
# Standard industrial limits
VOLTAGE_MIN     = 380.0     # Volts  (±10% of 415V)
VOLTAGE_MAX     = 450.0     # Volts
TEMP_MAX        = 85.0      # °C     (Class F insulation limit)
CURRENT_LIMIT   = motor_kw * 1000 / (1.732 * 415 * 0.85 * 0.90) * 1.15  # 115% of FLC

# ─────────────────────────────────────────────
# SECTION 3 — Voltage Check
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Voltage Check")
print("-" * 40)

if voltage < VOLTAGE_MIN:
    voltage_status = "LOW VOLTAGE ⚠️"
    voltage_safe   = False
elif voltage > VOLTAGE_MAX:
    voltage_status = "HIGH VOLTAGE ⚠️"
    voltage_safe   = False
else:
    voltage_status = "NORMAL ✅"
    voltage_safe   = True

print(f"  Input Voltage  : {voltage} V")
print(f"  Safe Range     : {VOLTAGE_MIN}V — {VOLTAGE_MAX}V")
print(f"  Status         : {voltage_status}")
print()

# ─────────────────────────────────────────────
# SECTION 4 — Current Check
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Current Check")
print("-" * 40)

if current <= CURRENT_LIMIT:
    current_status = "NORMAL ✅"
    current_safe   = True
else:
    current_status = "OVERCURRENT ⚠️  — Check load!"
    current_safe   = False

print(f"  Running Current : {current} A")
print(f"  Max Allowed     : {CURRENT_LIMIT:.2f} A  (115% of FLC)")
print(f"  Status          : {current_status}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — Temperature Check
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Temperature Check")
print("-" * 40)

if temperature < 60:
    temp_status = "COOL — Excellent ✅"
    temp_safe   = True
elif temperature < 75:
    temp_status = "WARM — Normal ✅"
    temp_safe   = True
elif temperature < TEMP_MAX:
    temp_status = "HOT — Monitor Closely ⚠️"
    temp_safe   = True
else:
    temp_status = "CRITICAL — SHUTDOWN REQUIRED 🔴"
    temp_safe   = False

print(f"  Temperature  : {temperature} °C")
print(f"  Max Limit    : {TEMP_MAX} °C  (Class F Insulation)")
print(f"  Status       : {temp_status}")
print()

# ─────────────────────────────────────────────
# SECTION 6 — Final Verdict
# ─────────────────────────────────────────────
print("=" * 55)
print(">>> FINAL SAFETY VERDICT")
print("=" * 55)

if voltage_safe and current_safe and temp_safe:
    print("  ✅  MOTOR IS SAFE TO RUN")
    print("  All parameters within acceptable limits.")
elif not temp_safe:
    print("  🔴  IMMEDIATE SHUTDOWN REQUIRED!")
    print("  Motor temperature exceeded critical limit.")
elif not voltage_safe and not current_safe:
    print("  ⚠️   DANGER — Voltage & Current both abnormal!")
    print("  Do NOT start motor. Check power supply & load.")
elif not voltage_safe:
    print("  ⚠️   WARNING — Voltage out of range!")
    print("  Check incoming supply before running motor.")
elif not current_safe:
    print("  ⚠️   WARNING — Overcurrent detected!")
    print("  Check for overload or mechanical jam.")

print("=" * 55)
print("  Day 2 Complete — input(), if-elif-else mastered!")
print("  Next: Loops (for, while), Lists")
print("=" * 55)
