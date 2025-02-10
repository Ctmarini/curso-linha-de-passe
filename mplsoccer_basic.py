import matplotlib.pyplot as plt
from mplsoccer import Pitch

pitch = Pitch(pitch_color='grass',line_color='k', goal_type='box', corner_arcs=True)
fig, ax = pitch.draw(nwors=2)
plt.show()