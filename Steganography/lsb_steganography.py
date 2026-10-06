from PIL import Image

def to_bits(data):
    return ''.join(f'{byte:08b}' for byte in data)

def bits_to_bytes(bits):
    return bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))

def encode():
    cover_path = input('Cover image: ')
    message = input('Secret message: ')
    output_path = input('Output image: ')

    try:
        image = Image.open(cover_path).convert('RGB')
    except Exception:
        print('Cover image tidak dapat dibuka.')
        return

    pixels = list(image.getdata())
    secret = message.encode('utf-8')
    data = len(secret).to_bytes(4, 'big') + secret
    bits = to_bits(data)

    capacity = len(pixels) * 3

    if len(bits) > capacity:
        print('Message terlalu panjang untuk gambar tersebut.')
        return

    new_pixels = []
    index = 0

    for pixel in pixels:
        new_pixel = list(pixel)

        for channel in range(3):
            if index < len(bits):
                new_pixel[channel] = (new_pixel[channel] & 254) | int(bits[index])
                index += 1

        new_pixels.append(tuple(new_pixel))

    stego = Image.new('RGB', image.size)
    stego.putdata(new_pixels)
    stego.save(output_path, 'PNG')

    print('Encoding berhasil.')
    print('Stego image:', output_path)

def decode():
    stego_path = input('Stego image: ')

    try:
        image = Image.open(stego_path).convert('RGB')
    except Exception:
        print('Stego image tidak dapat dibuka.')
        return

    pixels = list(image.getdata())
    bits = ''.join(str(channel & 1) for pixel in pixels for channel in pixel)

    if len(bits) < 32:
        print('Data tersembunyi tidak ditemukan.')
        return

    message_length = int.from_bytes(bits_to_bytes(bits[:32]), 'big')
    total_bits = 32 + message_length * 8

    if total_bits > len(bits):
        print('Data tersembunyi tidak valid.')
        return

    try:
        message = bits_to_bytes(bits[32:total_bits]).decode('utf-8')
    except UnicodeDecodeError:
        print('Data tersembunyi tidak valid.')
        return

    print('Pesan:', message)

while True:
    print('\n=== LSB Steganography ===')
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')

    choice = input('Pilih: ')

    if choice == '1':
        encode()
    elif choice == '2':
        decode()
    elif choice == '3':
        print('Program selesai.')
        break
    else:
        print('Pilihan tidak valid.')