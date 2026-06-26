# ============================================================
#  Industrial Sensor Data Monitor — Day 03
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Lists, Tuples, Indexing, Slicing,
#            List Methods, for loop with list,
#            Mutable vs Immutable
#  Goal    : Store & analyze sensor readings from
#            an industrial plant using Lists & Tuples
# ============================================================

print("=" * 56)
print("   INDUSTRIAL SENSOR DATA MONITOR")
print("   Author : Mohit Belwal | Day 03 of Python Journey")
print("=" * 56)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Tuples (Fixed / Immutable Data)
# Use Tuple when data should NOT change
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Plant Configuration (Tuple — Fixed Data)")
print("-" * 50)

# Tuple — plant configuration (never changes)
plant_info      = ("Mohit Belwal Power Plant", "Uttarakhand", 415, 50)
motor_ratings   = (3.7, 5.5, 7.5, 11.0, 15.0)   # kW ratings available

plant_name      = plant_info[0]
plant_location  = plant_info[1]
supply_voltage  = plant_info[2]
frequency       = plant_info[3]

print(f"  Plant Name     : {plant_name}")
print(f"  Location       : {plant_location}")
print(f"  Supply Voltage : {supply_voltage} V")
print(f"  Frequency      : {frequency} Hz")
print(f"  Motor Ratings  : {motor_ratings} kW")
print(f"  Largest Motor  : {motor_ratings[-1]} kW")
print(f"  Smallest Motor : {motor_ratings[0]} kW")
print()

# ─────────────────────────────────────────────
# SECTION 2 — Lists (Live Sensor Readings)
# Use List when data keeps changing
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Live Temperature Sensor Readings (List)")
print("-" * 50)

# List — temperature readings from 6 motors (°C)
temp_readings = [62.5, 78.3, 55.1, 91.2, 70.8, 45.6]
motor_names   = ["Motor-1", "Motor-2", "Motor-3",
                 "Motor-4", "Motor-5", "Motor-6"]

print("  Current Readings:")
for i in range(len(temp_readings)):
    status = "✅ Normal" if temp_readings[i] < 85 else "🔴 CRITICAL"
    print(f"    {motor_names[i]} : {temp_readings[i]} °C  →  {status}")
print()

# ─────────────────────────────────────────────
# SECTION 3 — List Operations
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Sensor Data Analysis")
print("-" * 50)

max_temp   = max(temp_readings)
min_temp   = min(temp_readings)
avg_temp   = sum(temp_readings) / len(temp_readings)
fault_count = 0

for temp in temp_readings:
    if temp >= 85:
        fault_count += 1

print(f"  Highest Temp   : {max_temp} °C  ← Motor-{temp_readings.index(max_temp)+1}")
print(f"  Lowest Temp    : {min_temp} °C  ← Motor-{temp_readings.index(min_temp)+1}")
print(f"  Average Temp   : {avg_temp:.2f} °C")
print(f"  Motors in Fault: {fault_count}")
print()

# ─────────────────────────────────────────────
# SECTION 4 — List Methods (Real Use Case)
# ─────────────────────────────────────────────
print(">>> SECTION 4 : Live Update — New Sensor Added")
print("-" * 50)

# New motor installed — add to list
temp_readings.append(66.4)
motor_names.append("Motor-7")
print(f"  Motor-7 added  : {temp_readings[-1]} °C")
print(f"  Total Motors   : {len(temp_readings)}")
print()

# Motor-3 removed for maintenance
temp_readings.pop(2)
motor_names.pop(2)
print(f"  Motor-3 removed for maintenance")
print(f"  Remaining Motors: {len(temp_readings)}")
print()

# Sort readings
sorted_temps = sorted(temp_readings)
print(f"  Sorted Temps   : {sorted_temps}")
print()

# ─────────────────────────────────────────────
# SECTION 5 — Slicing
# ─────────────────────────────────────────────
print(">>> SECTION 5 : Slicing — First 3 & Last 2 Readings")
print("-" * 50)

first_three = temp_readings[:3]
last_two    = temp_readings[-2:]

print(f"  First 3 readings : {first_three}")
print(f"  Last 2 readings  : {last_two}")
print()

# ─────────────────────────────────────────────
# SECTION 6 — Tuple vs List Summary
# ─────────────────────────────────────────────
print(">>> SECTION 6 : Tuple vs List — When to Use What?")
print("-" * 50)
print("  TUPLE  → Fixed data   : Plant config, Motor specs, GPS coords")
print("  LIST   → Dynamic data : Sensor readings, Alarms, Log entries")
print()

print("=" * 56)
print("  Day 3 Complete — Lists & Tuples mastered!")
print("  Next: Dictionary, Functions")
print("=" * 56)
