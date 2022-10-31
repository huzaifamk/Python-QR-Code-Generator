import qrcode
from data_list import list_data

# Generate QR Code with specific file name
def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# Generate QR Code for a list of data
def generate_qr_code_for_list(data_list):
    for data in data_list:
        generate_qr_code(data, data.split(".")[1] + ".png")

def main():
    # Generate QR Code with specific file name
    generate_qr_code("https://www.google.com", "google.png")
    generate_qr_code_for_list(list_data)

main()