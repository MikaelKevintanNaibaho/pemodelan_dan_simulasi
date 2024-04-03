# Plotting script for motor data
set xlabel "Time (s)"
set ylabel "Position (rad), Velocity (rad/s)"
set title "DC Motor Simulation"
plot "motor_data.txt" using 1:2 with lines title "Position", \
     "motor_data.txt" using 1:3 with lines title "Velocity"
