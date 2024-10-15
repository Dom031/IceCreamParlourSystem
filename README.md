# IceCreamParlourSystem

This project is a Python-based system developed for an ice cream parlour, designed to streamline the order-taking process. The system allows servers to log in, take orders for ice cream and toppings, and generate receipts. It was developed as part of an assignment during the first year of my Computer Science degree, and I received a perfect score of 100% for the project.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Technologies](#technologies)
- [Setup](#setup)
- [Credits](#credits)

## Introduction

The aim of this project was to build a functional system for an ice cream parlour, enabling staff to take orders digitally and improve service efficiency. The system logs the server in, takes the table number, number of guests, and allows the server to take customized ice cream orders, including random topping suggestions if none are chosen.

## Features

- **User Authentication**: Server logs in with their name and staff ID.
- **Order Management**: Allows servers to take orders for a specified number of guests, including ice cream flavours and optional toppings.
- **Random Topping Suggestions**: If a topping isn’t selected, the system can suggest one.
- **Receipt Generation**: Automatically generates a detailed receipt for each order, including prices and server information.
- **Input Validation**: Ensures that all inputs are correct (e.g., table number and number of guests).

## Usage

1. The server logs in by entering their name and ID from a predefined list of authorized users.
2. The system prompts the server to enter the table number and number of guests.
3. For each guest, the system displays available ice cream flavours and toppings.
4. If no topping is selected, the system will suggest one at random.
5. A final receipt is printed, summarizing the order for the table, along with the total cost.

## Technologies

- **Python**: The entire system is built using Python and showcases the use of dictionaries, loops, input validation, and randomization for topping suggestions.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/IceCreamParlourSystem.git
