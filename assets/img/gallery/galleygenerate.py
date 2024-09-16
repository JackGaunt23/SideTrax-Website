import os

# Define the directory where your images are stored
directory = "C:\Users\jackg\Pictures\iCloud Photos\Shared\Website photos"

# Get a sorted list of all image files
files = sorted(os.listdir(directory))

# Initialize a variable to hold the HTML code
html_output = ""

# Loop through each file and generate the HTML structure
for index, file in enumerate(files):
    if file.endswith(('.jpg', '.jpeg', '.png')):  # Adjust this for your file types
        image_number = index + 1
        html_output += f'''
        <div class="col-lg-4 col-md-6">
            <div class="gallery-item">
                <a href="assets/img/gallery/{image_number}.jpg" class="popup-gallery">
                    <img src="assets/img/gallery/{image_number}.jpg" alt="Gallery Image">
                </a>
            </div>
        </div>
        '''

# Output the generated HTML
print(html_output)
