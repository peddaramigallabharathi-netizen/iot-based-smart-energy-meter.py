import csv
import random
import time
from datetime import datetime

# Energy meter settings
TARIFF_PER_KWH = 6.00       # Example tariff in Rs/kWh
SAMPLE_INTERVAL = 2         # Seconds
TOTAL_SAMPLES = 20


def calculate_power(voltage, current, power_factor):
    """Calculate real power in watts."""
    return voltage * current * power_factor


def calculate_energy(power_watts, time_seconds):
    """Calculate energy in kWh."""
    return (power_watts * time_seconds) / (1000 * 3600)


def save_data(timestamp, voltage, current, power_factor,
              power, energy, cost):
    """Save energy data to CSV file."""
    with open("energy_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            round(voltage, 2),
            round(current, 2),
            round(power_factor, 2),
            round(power, 2),
            round(energy, 6),
            round(cost, 4)
        ])


def main():
    print("=" * 60)
    print("          IoT BASED SMART ENERGY METER")
    print("=" * 60)

    # Create CSV file and header
    with open("energy_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "Voltage_V",
            "Current_A",
            "PowerFactor",
            "Power_W",
            "Energy_kWh",
            "Cost_Rs"
        ])

    total_energy = 0

    print("\nStarting energy monitoring...\n")

    for _ in range(TOTAL_SAMPLES):

        # Simulated IoT sensor readings
        voltage = random.uniform(220, 240)
        current = random.uniform(1, 10)
        power_factor = random.uniform(0.80, 0.99)

        # Calculate power
        power = calculate_power(
            voltage,
            current,
            power_factor
        )

        # Calculate energy
        energy = calculate_energy(
            power,
            SAMPLE_INTERVAL
        )

        total_energy += energy

        # Calculate cost
        cost = total_energy * TARIFF_PER_KWH

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Save data
        save_data(
            timestamp,
            voltage,
            current,
            power_factor,
            power,
            energy,
            cost
        )

        # Display readings
        print(
            f"Time: {timestamp} | "
            f"Voltage: {voltage:.1f} V | "
            f"Current: {current:.2f} A | "
            f"Power: {power:.2f} W | "
            f"Energy: {total_energy:.6f} kWh | "
            f"Cost: Rs.{cost:.4f}"
        )

        time.sleep(SAMPLE_INTERVAL)

    print("\n" + "=" * 60)
    print("             FINAL ENERGY REPORT")
    print("=" * 60)
    print(f"Total Energy : {total_energy:.6f} kWh")
    print(f"Energy Cost  : Rs.{total_energy * TARIFF_PER_KWH:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
