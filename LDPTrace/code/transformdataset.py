def transform_dataset(original_dataset):
    transformed_dataset = []
    trajectory_id = -1  # Initialize the trajectory ID to -1

    for line in original_dataset:
        if line.startswith('newpoint'):
            trajectory_id += 1  # Increment the trajectory ID for new points
            transformed_dataset.append(f"#{trajectory_id}:")
            transformed_dataset.append(f">0: {line.split()[5]},{line.split()[6]}")
        elif line.startswith('point'):
            transformed_dataset[-1] += f"; {line.split()[5]},{line.split()[6]}"
        else:
            # Handling additional cases if any specific action is required
            pass

    return transformed_dataset


if __name__ == "__main__":
    # Read the original dataset
    with open('/LDPTrace-implementation/LDPTrace/data/original_oldenburg.dat', 'r') as file:
        original_dataset = file.readlines()

    # Transform the dataset
    transformed_dataset = transform_dataset(original_dataset)

    # Save the transformed dataset
    with open('/LDPTrace-implementation/LDPTrace/data/oldenburg.dat', 'w') as file:
        file.write('\n'.join(transformed_dataset))
    print("\n[+] The dataset was processed and stored as : /LDPTrace-implementation/LDPTrace/data/oldenburg.dat")
