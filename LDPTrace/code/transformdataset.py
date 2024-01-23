
def transform_dataset(original_dataset):
    transformed_dataset = []

    print("len(original_dataset) =", len(original_dataset))

    d = dict()

    for line in original_dataset:
        trajectory_id = line.split()[1]
        if line.startswith('newpoint'):
            d[trajectory_id] = [(line.split()[5], line.split()[6])]
        elif line.startswith('point'):
            d[trajectory_id].append((line.split()[5], line.split()[6]))
        elif line.startswith('disappearpoint'):
            d[trajectory_id].append((line.split()[5], line.split()[6]))
            transformed_dataset.append(f"#{trajectory_id}:")
            coords = d.pop(trajectory_id)
            transformed_dataset.append(f">0: {coords[0][0]}, {coords[0][1]}")
            for coord in coords[1:]:
                transformed_dataset[-1] += f"; {coord[0]}, {coord[1]}"
        else:
            pass

    print("len(transformed_dataset) =", len(transformed_dataset)/2)

    return transformed_dataset



if __name__ == "__main__":
    # Read the original dataset
    print("\n[*] Datset has been loaded for preprocessing..")

    with open('/LDPTrace-implementation/LDPTrace/data/original_oldenburg.dat', 'r') as file:
        original_dataset = file.readlines()

    # Transform the dataset
    transformed_dataset = transform_dataset(original_dataset)

    # Save the transformed dataset
    with open('/LDPTrace-implementation/LDPTrace/data/oldenburg.dat', 'w') as file:
        file.write('\n'.join(transformed_dataset))
    print("\n[+] The dataset was processed and stored as : /LDPTrace-implementation/LDPTrace/data/oldenburg.dat\n")
