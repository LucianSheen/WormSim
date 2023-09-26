# Worm simulation.
import sys
sys.path.insert(1, 'x64/Release')
import wormpy
wormpy.init()
wormpy.step(0.0)
activations = []
for segment in range(12) :
    activations.append(wormpy.get_ventral_muscle_activation(segment));
print(activations)
wormpy.term()
