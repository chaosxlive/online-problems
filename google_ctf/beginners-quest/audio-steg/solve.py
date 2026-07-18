# Put mk.wav in the same directory

import numpy as np
import wave
import pathlib

file_path = pathlib.Path(__file__).parent

print(file_path)

with wave.open(str(file_path / 'mk.wav'), 'rb') as wav:
    frames = wav.readframes(wav.getnframes())

raw_bits = np.frombuffer(frames, dtype=np.uint8)
byte_lsbs = raw_bits & 1

result = []
for i in range(0, len(byte_lsbs), 8):
    byte_lsbs[i:i+8]
    b = 0
    for j in range(8):
        b = (b << 1) | int(byte_lsbs[i + j])
    result.append(b)

result_bytes = bytes(result)
start_idx = result_bytes.find(b'CTF')
end_idx = result_bytes.find(b'}', start_idx + 1)
print(result_bytes[start_idx:end_idx+1])