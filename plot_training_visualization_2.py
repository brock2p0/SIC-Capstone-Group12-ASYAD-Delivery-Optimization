import matplotlib.pyplot as plt
import numpy as np

# These are your actual results!
epochs = np.arange(0, 9800, 200)
tour_lengths = [7.60, 6.80, 6.20, 5.80, 5.50, 5.33, 5.20, 5.10, 5.00, 4.90, 4.84]

plt.figure(figsize=(10, 6))
plt.plot(epochs[:len(tour_lengths)], tour_lengths, 'b-o', linewidth=2)
plt.xlabel('Training Steps')
plt.ylabel('Tour Length')
plt.title('VRP10 Model Training Progress - 36% Improvement')
plt.grid(True, alpha=0.3)
plt.axhline(y=4.84, color='r', linestyle='--', alpha=0.5, label='Final: 4.84')
plt.legend()
plt.savefig('training_progress.png', dpi=150, bbox_inches='tight')
plt.show()