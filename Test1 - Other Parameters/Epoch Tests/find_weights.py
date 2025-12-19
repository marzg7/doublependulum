import torch

def extract_weights_biases(pth_file_path):
    # Load the state dictionary from the .pth file
    # Use map_location='cpu' if you are loading a GPU-trained model on a CPU machine
    try:
        checkpoint = torch.load(pth_file_path, map_location=torch.device('cpu'))
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # A .pth file might save only the state_dict, or a whole checkpoint dictionary
    # Check if the loaded object is a dictionary and contains a 'state_dict' key
    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']
    elif isinstance(checkpoint, dict):
         state_dict = checkpoint
    else:
        print("Loaded object is not a recognized state dictionary format.")
        return

    print(f"Successfully loaded state dictionary with {len(state_dict.keys())} parameter sets.")

    # Iterate through the state dictionary to access and print weights and biases
    for key, value in state_dict.items():
        print(f"\nLayer Name: {key}")
        print(f"Shape: {value.shape}")
        print(f"Values (first 5 elements): {value.flatten()[:5].tolist()}")
        
        # You can also save these values to a file or a different format if needed
        # Example: if 'weight' in key: save_to_csv(value.numpy())

# Usage example:
# Replace 'your_model.pth' with the actual path to your file

# Function definitions and class definitions go here
if __name__ == "__main__":
    extract_weights_biases('Neural_ODE_train_Trial2+Trial3_test_Trial1_dopri5_500epochs.pth')


