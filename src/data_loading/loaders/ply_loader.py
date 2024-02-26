import struct

class PLYLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_ply(self):
        with open(self.filepath, 'rb') as f:
            format = self._read_header(f)
            if format == 'ascii':
                vertices = self._read_ascii(f)
            elif format == 'binary_little_endian':
                vertices = self._read_binary(f, '<')
            elif format == 'binary_big_endian':
                vertices = self._read_binary(f, '>')
            else:
                raise ValueError("Unsupported PLY format")
            return vertices

    def _read_header(self, f):
        format = None
        line = f.readline().decode().strip()
        while line:
            if 'format' in line:
                format = line.split()[1]
            elif line == 'end_header':
                break
            line = f.readline().decode().strip()
        return format

    def _read_ascii(self, f):
        vertices = []
        for line in f:
            parts = line.decode().strip().split()
            if len(parts) == 3:
                vertices.append(tuple(map(float, parts)))
        return vertices

    def _read_binary(self, f, endian):
        vertices = []
        vertex_format = endian + 'fff'
        vertex_size = struct.calcsize(vertex_format)
        while True:
            buf = f.read(vertex_size)
            if not buf:
                break
            vertices.append(struct.unpack(vertex_format, buf))
        return vertices

# 示例使用
if __name__ == "__main__":
    loader = PLYLoader("path_to_your_ply_file.ply")
    vertices = loader.load_ply()
    print(vertices)
