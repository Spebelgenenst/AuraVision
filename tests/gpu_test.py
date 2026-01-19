import torch

# Prüfe, ob CUDA verfügbar ist
print(torch.cuda.is_available())  # Sollte True ausgeben

# Verschiebe einen Tensor auf die GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor = torch.randn(3, 3).to(device)
print(tensor.device)  # Sollte 'cuda:0' ausgeben
