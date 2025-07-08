import sys

if len(sys.argv) != 3:
    print("Usage: python chunker.py <inputfile> <outputfile>")
    print("This script reads a binary file and converts it into a C-style string "
          "representation suitable for use as shellcode.")
    sys.exit(1)

INFILENAME = sys.argv[1]
OUTFILENAME = sys.argv[2]
WIDTH = 40

infile = open(INFILENAME, 'rb')
data = infile.read()
length = len(data)


def chunkToStr(chunk):
    chunkstr = ""
    for byte in chunk:
        thisByteStr = str(hex(byte))[2:]
        if len(thisByteStr) < 2:
            thisByteStr = '0'+thisByteStr
        chunkstr += '\\x' + thisByteStr
    return chunkstr

start = 0
outstring = 'unsigned char shellcode[] = '
while ((start + WIDTH) < length):
    chunk = data[start:start+WIDTH]
    chunkstr = chunkToStr(chunk)
    outstring += '"' + chunkstr + '"\n'
    start += WIDTH

# one last chunk
chunk = data[start:]
chunkstr = chunkToStr(chunk)
outstring += '"' + chunkstr + '";\n'

print(outstring)

outfile = open(OUTFILENAME, "w")
outfile.write(outstring)
outfile.close()