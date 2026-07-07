# ============================================================
#  Industrial Plant Monitor — Day 07
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: while loop, loop counter, break, continue,
#            infinite loop with condition exit
#  Goal    : Simulate continuous plant monitoring using
#            while loop — just like a real SCADA scan cycle
# ============================================================

import random  # to simulate live sensor readings

print("=" * 58)
print("   INDUSTRIAL PLANT MONITOR — SCADA SCAN SIMULATOR")
print("   Author : Mohit Belwal | Day 07 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Basic While Loop
#             Print motor numbers 1 to 6
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Motor List (Basic While Loop)")
print("-" * 45)

i = 1
while i <= 6:
    print(f"  Motor-{i} : Online")
    i = i + 1   # i += 1

print()

# ─────────────────────────────────────────────
# SECTION 2 — While loop with List
#             Print all sensor values from list
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Sensor Readings from List")
print("-" * 45)

temp_readings = [62.5, 78.3, 55.1, 91.2, 70.8, 45.6]
index = 0

while index < len(temp_readings):
    temp = temp_readings[index]
    status = "✅ Normal" if temp < 85 else "🔴 CRITICAL"
    print(f"  Motor-{index+1} Temperature : {temp}°C  →  {status}")
    index += 1

print()

# ─────────────────────────────────────────────
# SECTION 3 — While loop with break
#             Stop scan when critical fault found
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Fault Scan — Stop on Critical (break)")
print("-" * 45)

voltages = [415, 420, 410, 350, 418, 422]  # 350V is fault
i = 0

while i < len(voltages):
    v = voltages[i]
    if v < 380:
        print(f"  ⚠️  CRITICAL FAULT at Bus-{i+1} : {v}V — SCAN STOPPED!")
        break   # exit loop immediately
    else:
        print(f"  Bus-{i+1} : {v}V ✅")
    i += 1

print()

# ─────────────────────────────────────────────
# SECTION 4 — While loop with continue
#             Skip offline motors, log only active
# ─────────────────────────────────────────────
print(">>> SECTION 4 : Active Motor Log (continue)")
print("-" * 45)

motor_status = ["Online", "Offline", "Online", "Offline", "Online", "Online"]
i = 0
active_count = 0

while i < len(motor_status):
    if motor_status[i] == "Offline":
        i += 1
        continue    # skip offline motors
    active_count += 1
    print(f"  Motor-{i+1} : {motor_status[i]} — Logged ✅")
    i += 1

print(f"  Total Active Motors : {active_count}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — SCADA Scan Cycle Simulator
#             Scans 5 times then stops
# ─────────────────────────────────────────────
print(">>> SECTION 5 : SCADA Scan Cycle (5 Cycles)")
print("-" * 45)

scan_cycle  = 1
max_cycles  = 5
fault_found = False

while scan_cycle <= max_cycles:
    # Simulate random temperature reading
    temp = round(random.uniform(50, 95), 1)
    print(f"  Scan {scan_cycle} → Temperature : {temp}°C", end="  ")

    if temp >= 85:
        print("🔴 FAULT DETECTED — Triggering Alarm!")
        fault_found = True
        break
    else:
        print("✅ Normal")

    scan_cycle += 1

if fault_found:
    print("  >>> Alarm sent to SCADA! Motor tripped.")
else:
    print(f"  >>> All {max_cycles} scans complete. Plant Normal.")

print()

# ─────────────────────────────────────────────
# SECTION 6 — User Input Loop
#             Keep asking until valid input given
# ─────────────────────────────────────────────
print(">>> SECTION 6 : Input Validation Loop")
print("-" * 45)

while True:
    try:
        motor_kw = float(input("  Enter Motor Rating (1 to 100 kW) : "))
        if 1 <= motor_kw <= 100:
            print(f"  ✅ Valid input — {motor_kw} kW motor accepted!")
            break
        else:
            print("  ❌ Out of range! Enter between 1 and 100.")
    except:
        print("  ❌ Invalid! Enter a number only.")

print()
print("=" * 58)
print("  Day 7 Complete — while loop, break, continue mastered!")
print("  Next: for loop, range()")
print("=" * 58)
