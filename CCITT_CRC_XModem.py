import struct

class ccitt_crc_xmodem:
    def __init__(self, seed, init_crc_value): 
        self.seed = seed
        self.init_crc_value = init_crc_value


    def ccitt_crc16(self, data: bytes) -> int:

        # Inicializamos el CRC con el valor inicial predeterminado
        crc = self.init_crc_value

         # Iteramos sobre cada byte de datos
        for byte in data:
            # Aplicamos una operación XOR en el byte actual y el CRC actual
            crc ^= byte << 8

            # Realizamos un bucle de 8 iteraciones para calcular el CRC
            for _ in range(8):
                # Si el valor más significativo del CRC es 1, entonces aplicamos la
                # fórmula de CCITT para calcular el CRC
                if crc & 0x8000:
                    crc = (crc << 1) ^ self.seed
                # Si el valor más significativo del CRC es 0, entonces solo
                # desplazamos el CRC a la izquierda
                else:
                    crc <<= 1

        # Aplicamos una máscara al CRC final para obtener solo los 16 bits más significativos
        return crc & 0xFFFF

    def int2bytes(self, data):
        return data.to_bytes(2, 'big')

    def mostrar_CRC(self, bytes):
        print([bytes.hex()[x:x+2] for x in range(0, len(bytes.hex()), 2)])


    
CntMessage  = int('0x00', 16)     # 1 byte
Command     = int('0x00', 16)     # 1 byte
OpCodMSB    = int('0x00', 16)     # 1 byte
OpCodLSB    = int('0x04', 16)     # 1 byte

    
a_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   

OpCodLSB    = int('0x06', 16)     # 1 byte

b_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   

OpCodLSB    = int('0x03', 16)     # 1 byte

c_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   

OpCodLSB    = int('0x05', 16)     # 1 byte

d_bytesToSend =  (struct.pack('B', CntMessage)  +
                  struct.pack('B', Command)     +
                  struct.pack('B', OpCodMSB)    +
                  struct.pack('B', OpCodLSB))   

obj = ccitt_crc_xmodem(0x1021, 0x0000)

CRC_a_int = obj.ccitt_crc16(a_bytesToSend) 
CRC_b_int = obj.ccitt_crc16(b_bytesToSend)
CRC_c_int = obj.ccitt_crc16(c_bytesToSend)
CRC_d_int = obj.ccitt_crc16(d_bytesToSend)

CRC_a_bytes = obj.int2bytes(CRC_a_int)
CRC_b_bytes = obj.int2bytes(CRC_b_int)
CRC_c_bytes = obj.int2bytes(CRC_c_int)
CRC_d_bytes = obj.int2bytes(CRC_d_int)

assert CRC_a_bytes == bytearray([0x40, 0x84])
print('El CRC: {} es correcto'.format([CRC_a_bytes.hex()[x:x+2] for x in range(0, len(CRC_a_bytes.hex()), 2)]))

assert CRC_b_bytes == bytearray([0x60, 0xC6])
print('El CRC: {} es correcto'.format([CRC_b_bytes.hex()[x:x+2] for x in range(0, len(CRC_b_bytes.hex()), 2)]))

assert CRC_c_bytes == bytearray([0x30, 0x63])
print('El CRC: {} es correcto'.format([CRC_c_bytes.hex()[x:x+2] for x in range(0, len(CRC_c_bytes.hex()), 2)]))

assert CRC_d_bytes == bytearray([0x50, 0xA5])
print('El CRC: {} es correcto'.format([CRC_d_bytes.hex()[x:x+2] for x in range(0, len(CRC_d_bytes.hex()), 2)]))

print("\nCRCs calculados correctamente..\n")
