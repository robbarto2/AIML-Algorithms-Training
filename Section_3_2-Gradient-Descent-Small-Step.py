import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate training data with 10000 samples
np.random.seed(0)
torch.manual_seed(0)
x_train = torch.linspace(-4, 4, 10000).unsqueeze(1)
y_train = torch.sin(x_train) - 0.1 * x_train**2

# Define the neural network architecture
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(1, 4)  # Input to hidden layer
        self.layer2 = nn.Linear(4, 1)  # Hidden to output layer

    def forward(self, x):
        x = torch.sigmoid(self.layer1(x))
        x = self.layer2(x)
        return x

# Implement the training loop with real-time plot
def train_model_with_real_time_plot(model, x_train, y_train, num_epochs=10000, learning_rate=0.02):
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x_train, y_train, label='Training data', color='green', s=10)
    ax.plot(x_train, y_train, label='True function', color='blue')
    line, = ax.plot([], [], label='Trained Model', color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Supervised Learning Fit: sin(x) - 0.1x^2')
    ax.legend()

    epoch_text = ax.text(-5, 0.75, f'Epoch 0', fontsize=12, ha='left')

    def update(frame, model, x_train, line, epoch_text):
        if frame == 0:
            line.set_data([], [])
            return line, epoch_text

        y_pred = model(x_train)
        loss = criterion(y_pred, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if frame % 1 == 0:  # Update the plot every 1 epochs
            line.set_data(x_train, y_pred.detach().numpy())
            epoch = frame * 10
            epoch_text.set_text(f'Epoch {epoch}')
            epoch_text.set_position((-5, 0.75))

        return line, epoch_text

    ani = animation.FuncAnimation(fig, update, fargs=(model, x_train, line, epoch_text), frames=num_epochs // 10 + 1, blit=True, interval=100, repeat=False)
    plt.show()

# Create the model and train it with real-time plot
model = NeuralNetwork()
train_model_with_real_time_plot(model, x_train, y_train)
