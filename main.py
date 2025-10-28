import qrcode
import os
import argparse
from datetime import datetime

def generate_qr_code(url: str, output_dir: str = "qr_codes") -> str:
    """Generates a QR code for the given URL and saves it."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_name = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = os.path.join(output_dir, file_name)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    print(f"✅ QR code generated and saved at: {file_path}")
    return file_path

def main():
    parser = argparse.ArgumentParser(description="Generate QR code for a given URL.")
    parser.add_argument("--url", type=str, required=True, help="URL to encode")
    args = parser.parse_args()
    generate_qr_code(args.url)

if __name__ == "__main__":
    main()
