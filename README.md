# MusicFromEEG

This project is the results of attempting to create programatic prodecurally generated music based on input from a Muse EEG brain scanner. 

It sucks.

I used the Mind Monitor app to forward raw OSC signal data to a python server, which in turn forward the data to a python middleware which transforms the data into MIDI chords and then sends the chords to Sonic Pi. Sonic Pi then incorperates the MIDI notes into its main loop. 
