# Worm simulation test.
import sys
sys.path.insert(1, 'x64/Release')
import wormpy
wormpy.init()
for i in range(6):
   wormpy.step(0.0)
   angles = []
   activations = []
   for segment in range(12) :
        angles.append(wormpy.get_segment_angle(segment))
        activations.append(wormpy.get_ventral_muscle_activation(segment))
   print(angles)
   #print activations
wormpy.term()

