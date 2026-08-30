class Solution:
    def removeComments(self, source: list[str]) -> list[int]:
        res = []
        in_block = False
        current_line = []

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                # If currently inside a block comment, look for the closing '*/'
                if in_block:
                    if i + 1 < n and line[i : i + 2] == "*/":
                        in_block = False
                        i += 1  # Skip the next character
                else:
                    # Line comment starts: ignore rest of the line
                    if i + 1 < n and line[i : i + 2] == "//":
                        break
                    # Block comment starts
                    elif i + 1 < n and line[i : i + 2] == "/*":
                        in_block = True
                        i += 1  # Skip the next character
                    # Normal character
                    else:
                        current_line.append(line[i])
                i += 1

            # Only append to results if not still inside a multi-line block comment
            # and there are characters on the current line
            if not in_block and current_line:
                res.append("".join(current_line))
                current_line = []

        return res