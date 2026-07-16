# ============================================================
#  Industrial Motor Management System — Day 10
#  Author  : Mohit Belwal
#  Domain  : Electrical Engineering & Industrial Automation
#  Concepts: Class, Class Attributes, Instance Attributes,
#            self parameter, Object Instantiation,
#            Methods, __init__
#  Goal    : Model real industrial motors as Python objects
#            using OOP — just like SCADA does internally!
# ============================================================

import math

print("=" * 58)
print("   INDUSTRIAL MOTOR MANAGEMENT SYSTEM v1.0")
print("   Author : Mohit Belwal | Day 10 of Python Journey")
print("=" * 58)
print()

# ─────────────────────────────────────────────
# SECTION 1 — Class with Class Attributes
#             Attributes common to ALL motors
# ─────────────────────────────────────────────
print(">>> SECTION 1 : Class Attributes (Common to All Motors)")
print("-" * 50)

class Motor:
    # Class Attributes — same for every motor in plant
    plant_name   = "Mohit Belwal Industries"
    supply_voltage = 415        # V — same for whole plant
    frequency    = 50           # Hz
    pf           = 0.85         # standard power factor
    efficiency   = 0.90         # standard efficiency

    def get_plant_info(self):
        print(f"  Plant     : {Motor.plant_name}")
        print(f"  Voltage   : {Motor.supply_voltage} V")
        print(f"  Frequency : {Motor.frequency} Hz")

# Create object and access class attribute
m1 = Motor()
m1.get_plant_info()
print()

# Class attribute accessible via class name too
print(f"  Via class  : Motor.plant_name = {Motor.plant_name}")

# Change class attribute — affects ALL objects
Motor.plant_name = "Mohit Belwal Power Plant"
print(f"  After change : Motor.plant_name = {Motor.plant_name}")
print()

# ─────────────────────────────────────────────
# SECTION 2 — Instance Attributes
#             Attributes unique to each motor
# ─────────────────────────────────────────────
print(">>> SECTION 2 : Instance Attributes (Unique per Motor)")
print("-" * 50)

class Motor:
    # Class Attributes
    plant_name     = "Mohit Belwal Power Plant"
    supply_voltage = 415
    frequency      = 50
    pf             = 0.85
    efficiency     = 0.90

    def __init__(self, name, power_kw, location, motor_id):
        # Instance Attributes — unique to each motor object
        self.name      = name
        self.power_kw  = power_kw
        self.location  = location
        self.motor_id  = motor_id
        self.status    = "Stopped"      # default status
        self.run_hours = 0              # default run hours

    def get_flc(self):
        """Calculate Full Load Current — uses self + class attrs"""
        power_w = self.power_kw * 1000
        flc = power_w / (math.sqrt(3) * Motor.supply_voltage
                         * Motor.pf * Motor.efficiency)
        return round(flc, 2)

    def get_info(self):
        """Print motor details — self refers to this object"""
        print(f"  ID        : {self.motor_id}")
        print(f"  Name      : {self.name}")
        print(f"  Location  : {self.location}")
        print(f"  Rating    : {self.power_kw} kW")
        print(f"  FLC       : {self.get_flc()} A")
        print(f"  Status    : {self.status}")
        print(f"  Run Hours : {self.run_hours} hrs")
        print()

# Create different motor objects — each has own instance attrs
pump_motor      = Motor("Pump Motor",      7.5,  "Ground Floor", "MTR-001")
conveyor_motor  = Motor("Conveyor Motor",  11.0, "First Floor",  "MTR-002")
compressor      = Motor("Compressor",      15.0, "Roof Top",     "MTR-003")

pump_motor.get_info()
conveyor_motor.get_info()
compressor.get_info()

# ─────────────────────────────────────────────
# SECTION 3 — Instance attrs take preference
#             over class attrs
# ─────────────────────────────────────────────
print(">>> SECTION 3 : Instance vs Class Attribute Priority")
print("-" * 50)

# Give pump motor a custom power factor (special motor)
pump_motor.pf = 0.92    # Instance attribute created
print(f"  pump_motor.pf  = {pump_motor.pf}   ← instance attribute")
print(f"  Motor.pf       = {Motor.pf}   ← class attribute unchanged")
print(f"  conveyor.pf    = {conveyor_motor.pf}   ← still uses class attr")
print()

# ─────────────────────────────────────────────
# SECTION 4 — self parameter in detail
# ─────────────────────────────────────────────
print(">>> SECTION 4 : self Parameter")
print("-" * 50)

class Motor:
    plant_name     = "Mohit Belwal Power Plant"
    supply_voltage = 415
    pf             = 0.85
    efficiency     = 0.90

    def __init__(self, name, power_kw, location, motor_id):
        self.name      = name
        self.power_kw  = power_kw
        self.location  = location
        self.motor_id  = motor_id
        self.status    = "Stopped"
        self.run_hours = 0
        self.temp      = 25.0

    def start(self):
        """self = the motor object calling this method"""
        self.status = "Running"
        print(f"  {self.name} [{self.motor_id}] → STARTED ✅")

    def stop(self):
        self.status = "Stopped"
        print(f"  {self.name} [{self.motor_id}] → STOPPED 🔴")

    def update_temp(self, new_temp):
        self.temp = new_temp
        status = "⚠️ HIGH" if new_temp >= 85 else "✅ Normal"
        print(f"  {self.name} Temp updated : {self.temp}°C → {status}")

    def get_status(self):
        print(f"  {self.name} : {self.status} | Temp: {self.temp}°C")

# Object instantiation
pump    = Motor("Pump Motor",     7.5,  "Ground Floor", "MTR-001")
conv    = Motor("Conveyor Motor", 11.0, "First Floor",  "MTR-002")

# Call methods — self is automatically passed
pump.start()            # equivalent to Motor.start(pump)
conv.start()            # equivalent to Motor.start(conv)
pump.update_temp(72.5)
conv.update_temp(91.2)  # critical!
pump.get_status()
conv.get_status()
print()
pump.stop()
pump.get_status()
print()

# ─────────────────────────────────────────────
# SECTION 5 — Plant Dashboard using Objects
# ─────────────────────────────────────────────
print(">>> SECTION 5 : Full Plant Dashboard")
print("-" * 50)

class Motor:
    plant_name     = "Mohit Belwal Power Plant"
    supply_voltage = 415
    pf             = 0.85
    efficiency     = 0.90
    motor_count    = 0      # class attr — counts all motors

    def __init__(self, name, power_kw, location, motor_id):
        self.name      = name
        self.power_kw  = power_kw
        self.location  = location
        self.motor_id  = motor_id
        self.status    = "Stopped"
        self.temp      = 25.0
        Motor.motor_count += 1   # increment class counter

    def start(self):
        self.status = "Running"

    def get_flc(self):
        return round((self.power_kw * 1000) /
                     (math.sqrt(3) * 415 * 0.85 * 0.90), 2)

# Create plant with 4 motors
motors = [
    Motor("Pump Motor",      7.5,  "Ground Floor", "MTR-001"),
    Motor("Conveyor Motor",  11.0, "First Floor",  "MTR-002"),
    Motor("Compressor",      15.0, "Roof Top",     "MTR-003"),
    Motor("Cooling Fan",     3.7,  "Ground Floor", "MTR-004"),
]

# Start some motors
motors[0].start()
motors[1].start()
motors[2].start()
motors[0].temp = 68.5
motors[1].temp = 91.2
motors[2].temp = 72.0

# Dashboard
print(f"  Plant : {Motor.plant_name}")
print(f"  Total Motors : {Motor.motor_count}")
print()
print(f"  {'ID':<10} {'Name':<18} {'kW':<6} {'FLC':<8} {'Status':<10} {'Temp'}")
print("  " + "-" * 60)
for m in motors:
    temp_flag = "🔴" if m.temp >= 85 else "✅"
    print(f"  {m.motor_id:<10} {m.name:<18} {m.power_kw:<6} "
          f"{m.get_flc():<8} {m.status:<10} {m.temp}°C {temp_flag}")

print()
print("=" * 58)
print("  Day 10 Complete — OOP Basics mastered!")
print("  Class attrs, Instance attrs, self, Methods, __init__")
print("  Next: Inheritance, Polymorphism")
print("=" * 58)
