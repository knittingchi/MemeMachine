from PIL import Image, ImageDraw, ImageFont

# Create a list to hold the frames of the GIF
frames = []

# Create the frames with text
for i in range(10):
    # Create a new image
    img = Image.new("RGB", (400, 200), color="white")

    # Draw "Just Married" on the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    text = "Just Married!"
    draw.text((100, 80), text, fill="red", font=font)

    # Append the image to the frames list
    frames.append(img)

# Save the frames as an animated GIF
frames[0].save("just_married.gif", save_all=True, append_images=frames[1:], duration=200, loop=0)
