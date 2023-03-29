#!/bin/bash

# Function to send two Enter keypresses
send_enter() {
  sleep 0.5
  echo
  sleep 0.5
  echo
}

# Run the oc command with the Enter keypresses as input
send_enter | oc