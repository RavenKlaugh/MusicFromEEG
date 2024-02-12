import time
from pythonosc import udp_client

# Define a major scale in terms of MIDI note numbers (C major for simplicity)
major_scale = [60, 62, 64, 65, 67, 69, 71]

# Define the octave shift: 1 for one octave up, -1 for one octave down, 0 for no shift.
octave_shift = 0  # Change this as needed to shift the octave

# Chord patterns in terms of scale degrees
chord_patterns = {
    1: [0, 2, 4],  # I   Major (C)
    2: [1, 3, 5],  # ii  Minor (Dm)
    3: [2, 4, 6],  # iii Minor (Em)
    4: [3, 5, 0],  # IV  Major (F)
    5: [4, 6, 1],  # V   Major (G)
    6: [5, 0, 2],  # vi  Minor (Am)
    7: [6, 1, 3]   # vii Diminished (Bdim) - You can treat this as Bm for simplicity
}

# Setup the OSC client for Sonic Pi
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

# Assuming your EEG software is running this script and setting the `ratio` variable
# For demonstration purposes, I'm simulating the ratio with random numbers here
import random
while True:
    # Simulate the ratio of beta to alpha waves
    ratio = random.uniform(0, 2)  # Replace this with actual data from your EEG

    # Map the ratio to a scale degree (1 to 7)
    scale_degree = int((ratio / 2) * 7) + 1
    scale_degree = max(1, min(scale_degree, 7))  # Ensure scale_degree is between 1 and 7
    
    # Get the chord pattern for the scale degree
    chord_pattern = chord_patterns[scale_degree]
    
    # Convert the scale degrees to MIDI notes based on the C major scale and apply octave shift
    chord_notes = [(major_scale[i] + (octave_shift * 12)) for i in chord_pattern]
    
    # Send the chord to Sonic Pi
    sender.send_message('/trigger/prophet/muse/elements/alpha_absolute', chord_notes)
    print('Just sent chord based on ratio {}:'.format(ratio), chord_notes)
    
    time.sleep(0.5)
