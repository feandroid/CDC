Project Name: Data Science PS

Project Objective:
This project implements a Late-Fusion Multimodal Neural Network to predict house prices. It leverages two distinct data sources:

1. Tabular Data: Numerical features describing house characteristics (e.g., sqft_living, grade, zipcode).

2. Visual Data: Static map images (224x224 pixels) retrieved via the Geoapify API based on the latitude and longitude of the properties.

Key Features:
Automated Data Pipeline: Downloads satellite/map imagery dynamically using property coordinates.

Custom Dataset Class: A robust PyTorch Dataset that handles simultaneous loading of normalized tabular tensors and transformed images.

Transfer Learning: Utilizes a pre-trained ResNet18 (ImageNet weights) as a feature extractor for the visual branch, as well as MLP(Multi-layer-perceptron) which are later fused together using regression.

Scalable Architecture: Easily expandable to include more features or larger vision backbones.

Setup & Requirements:
Provide your Geoapify API key in the Colab secrets/environment variables.

Ensure your train.xlsx is uploaded to the specified path.
