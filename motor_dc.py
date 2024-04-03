#include <stdio.h>

// Constants
#define VIN 12.0 // Input voltage (in volts)
#define R 2.0    // Motor resistance (in ohms)
#define L 0.5    // Motor inductance (in henrys)
#define Ke 0.01  // Back EMF constant (in volts per rad/s)
#define Km 0.1   // Torque constant (in Nm/A)
#define J 0.05   // Moment of inertia (in kg m^2)
#define B 0.1    // Damping coefficient (in Nm s/rad)

// Function to model the DC motor dynamics
void motorModel(double Vin, double *theta, double *omega, double dt) {
    // Calculate motor current
    double I = (Vin - (*omega) * Ke) / R;

    // Calculate motor torque
    double Tm = I * Km;

    // Calculate angular acceleration
    double alpha = (Tm - B * (*omega)) / J;

    // Update angular velocity and position using Euler's method
    *omega += alpha * dt;
    *theta += (*omega) * dt;
}

int main() {
    double theta = 0.0;  // Initial position (in radians)
    double omega = 0.0;  // Initial velocity (in rad/s)
    double dt = 0.01;    // Time step (in seconds)
    double simTime = 5.0; // Simulation time (in seconds)

    printf("Time (s)\tPosition (rad)\tVelocity (rad/s)\n");

    for (double t = 0.0; t <= simTime; t += dt) {
        // Simulate motor dynamics
        motorModel(VIN, &theta, &omega, dt);

        // Print simulation results
        printf("%.2f\t\t%.4f\t\t%.4f\n", t, theta, omega);
    }

    return 0;
}
