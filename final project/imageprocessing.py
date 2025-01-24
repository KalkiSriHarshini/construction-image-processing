import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(file_path):
    """Load an image from the given path."""
    img = cv2.imread(file_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {file_path}. Check the path or file integrity.")
    return img

def display_image(window_name, img):
    """Display an image using matplotlib."""
    # Convert BGR (OpenCV default) to RGB for matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(window_name)
    plt.axis("off")
    plt.show()

def resize_image(img, width, height):
    """Resize the image to the specified width and height."""
    return cv2.resize(img, (width, height))

def detect_edges(img):
    """Detect edges in the image using the Canny edge detector."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def convert_to_grayscale(img):
    """Convert the image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def process_images(option, img1):
    """Perform the selected image processing task."""
    if option == 1:  # Resize Image
        try:
            width = int(input("Enter the new width (in pixels): "))
            height = int(input("Enter the new height (in pixels): "))
            resized = resize_image(img1, width, height)
            display_image("Resized Image", resized)
        except ValueError:
            print("Invalid input. Please enter numeric values for width and height.")

    elif option == 2:  # Edge Detection
        edges = detect_edges(img1)
        # Display edges as a grayscale image
        plt.imshow(edges, cmap="gray")
        plt.title("Edges")
        plt.axis("off")
        plt.show()

    elif option == 3:  # Convert to Grayscale
        grayscale = convert_to_grayscale(img1)
        # Display grayscale image
        plt.imshow(grayscale, cmap="gray")
        plt.title("Grayscale Image")
        plt.axis("off")
        plt.show()

    elif option == 4:  # Display Original Image
        display_image("Original Image", img1)

    else:
        print("Invalid option selected.")

def main():
    print("Welcome to the Interactive Image Processing Tool!")

    # Update file path to use a raw string
    file_path1 = r"C:\Users\kalki\OneDrive\Pictures\Screenshots\Screenshot 2025-01-21 054620.png"
    print(f"Using file path: {file_path1}")

    try:
        img1 = load_image(file_path1)
        print("Image loaded successfully.")
    except FileNotFoundError as e:
        print(e)
        return

    # Display menu options
    while True:
        print("\nSelect an Image Processing Task:")
        print("1. Resize Image")
        print("2. Detect Edges")
        print("3. Convert to Grayscale")
        print("4. Display Original Image")
        print("5. Exit")

        try:
            option = int(input("Enter your choice (1-5): "))
            if option == 5:
                print("Exiting the tool. Goodbye!")
                break
            process_images(option, img1)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
