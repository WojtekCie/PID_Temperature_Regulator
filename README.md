# PID Temperature Regulator

## Laboratory Report
**Academic Year:** 2024/25  
**Subject:** Microprocessor Systems  
**Exercise Topic:** Microprocessor-Based Control and Measurement System - PID Controller   
**Faculty, Field, Semester, Group:** WARiE, AiR, 5, A1-L2  
**Authors:** Łukasz Burdziłowski, Wojciech Ciesiółka  
**Exercise Date:** 23.01.2025  

## Project Overview
The goal of this project is to create a temperature regulation system using a PID controller. The system includes a heating resistor, a microcontroller generating a PWM signal, and a temperature sensor for feedback control.

## Components Used
- **Microcontroller:** Nucleo-L476RG
- **Temperature Sensor:** BMP280
- **Heating Resistor:** 22Ω
- **Transistor:** NPN PN2222a

## System Model
A first-order transfer function with transport delay was identified using Matlab's Curve Fitting Tool:
- **Gain (k):** 7.005
- **Time Constant (T):** 137.8
- **Transport Delay (To):** 1.175

## PID Controller
The PID controller parameters were initially calculated using the SIMC method and fine-tuned experimentally:
- **Kp:** 8.3709
- **Ti:** 9.4
- **Td:** 0.001

## STM32 Implementation
Timers **TIM2** and **TIM3** were initialized for temperature reading and PWM generation. A PID control loop was implemented in the interrupt callback function.

## Performance
- The resistor reaches the set temperature with minor overshoot.
- Settling time: ~400s
- Steady-state error: minimal

## Conclusion
A working PID temperature regulator was successfully implemented. While some overshoot was observed, the primary objective was achieved.

## Repository
[GitHub Repo](https://github.com/WojtekCie/PID_Temperature_Regulator)

