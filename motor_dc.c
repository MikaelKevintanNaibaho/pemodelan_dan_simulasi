#include <stdio.h>

// Constants
#define VIN 12.0 // Input voltage (in volts)
#define R 2.0    // Motor resistance (in ohms)
#define Ke 0.01  // Back EMF constant (in volts per rad/s)
#define Km 0.1   // Torque constant (in Nm/A)
#define J 0.05    // Moment of inertia (in kg m^2)
#define B 0.1    // Damping coefficient (in Nm s/rad)

// Function to model the DC motor dynamics
void motorDynamics(double Vin, double *theta, double *omega, double dt, FILE *fp) {
    // Calculate motor current
    double I = (Vin - (*omega) * Ke) / R;

    // Calculate motor torque
    double Tm = I * Km;

    // Calculate angular acceleration
    double alpha = (Tm - B * (*omega)) / J;

    // Update angular velocity and position using Euler's method
    *omega += alpha * dt;
    *theta += (*omega) * dt;

    // Write data to file
    fprintf(fp, "%.4f\t%.4f\t%.4f\n", Vin, *theta, *omega);
}

int main() {
    double theta = 0.0;  // Initial position (in radians)
    double omega = 0.0;  // Initial velocity (in rad/s)
    double dt = 0.01;    // Time step (in seconds)
    double simTime = 5.0; // Simulation time (in seconds)

    // Open file for writing
    FILE *fp;
    fp = fopen("motor_data.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    printf("Time (s)\tPosition (rad)\tVelocity (rad/s)\n");

    for (double t = 0.0; t <= simTime; t += dt) {
        // Simulate motor dynamics
        motorDynamics(VIN, &theta, &omega, dt, fp);

        // Print simulation results to console
        printf("%.2f\t\t%.4f\t\t%.4f\n", t, theta, omega);
    }

    // Close the file
    fclose(fp);

    return 0;
}
